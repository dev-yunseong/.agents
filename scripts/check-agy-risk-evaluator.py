#!/usr/bin/env python3
"""Exercise the agy PreToolUse risk evaluator with realistic tool calls.

Usage:
    python3 ~/.agents/scripts/check-agy-risk-evaluator.py [path-to-risk_evaluator.py]

Prints the exact JSON sent on stdin and the exact JSON printed back for every
case, then exits non-zero if any decision differs from what the case expects.
The evaluator is a hook, so the only honest way to check it is to run it the
way the hook does: one JSON object in, one decision out.
"""

import json
import os
import subprocess
import sys
import tempfile

DEFAULT_EVALUATOR = os.path.expanduser("~/.gemini/config/risk_evaluator.py")

SAFE_SCRIPT = """\
import json
from pathlib import Path

rows = json.loads(Path("data.json").read_text())
for row in rows:
    print(row["id"], row["name"])
"""

RISKY_SCRIPT = """\
import os
import urllib.request

payload = urllib.request.urlopen("https://example.com/x").read()
os.remove("/tmp/stale.lock")
"""


def run_command_call(command_line, cwd=None):
    args = {"CommandLine": command_line}
    if cwd:
        args["Cwd"] = cwd
    return {"toolCall": {"name": "run_command", "args": args}}


def write_file_call(target):
    return {"toolCall": {"name": "write_to_file", "args": {"TargetFile": target, "CodeContent": "x"}}}


def build_cases(safe_script_path, risky_script_path):
    """Each case is (name, payload or None for empty stdin, expected decision)."""
    return [
        # --- the shell rules that were already there ---
        ("plain ls", run_command_call("ls -la /home/yunseong/dev/artel"), "allow"),
        ("rm -rf", run_command_call("rm -rf /home/yunseong/dev/artel/build"), "ask"),
        ("git push", run_command_call("git push origin main"), "ask"),
        ("edit to a normal source file", write_file_call(
            "/home/yunseong/dev/artel/artel-orchestration-server/src/main/java/Foo.java"), "allow"),
        ("edit to ~/.ssh/config", write_file_call("/home/yunseong/.ssh/config"), "ask"),
        ("edit to a .env file", write_file_call("/home/yunseong/dev/artel/.jira.env"), "ask"),
        ("read-only tool", {"toolCall": {"name": "view_file", "args": {"AbsolutePath": "/etc/hosts"}}}, "allow"),
        ("empty stdin", None, "allow"),

        # --- Python source carried in a heredoc, which is how agy runs Python ---
        ("benign heredoc that reads and prints", run_command_call(
            "python3 - <<'PY'\n"
            "import glob, re\n"
            "for path in sorted(glob.glob('src/**/*.java', recursive=True)):\n"
            "    text = open(path).read()\n"
            "    if re.search(r'@Transactional', text):\n"
            "        print(path, text.count('@Transactional'))\n"
            "PY"), "allow"),
        ("benign heredoc walking a tree", run_command_call(
            "python3 - <<'PY'\n"
            "import os\n"
            "total = 0\n"
            "for root, dirs, files in os.walk('src'):\n"
            "    total += len(files)\n"
            "print(total)\n"
            "PY"), "allow"),
        ("str.replace must not be mistaken for os.replace", run_command_call(
            "python3 - <<'PY'\n"
            "name = 'artel-home'.replace('-', '_')\n"
            "rows = [line.rstrip() for line in open('data.csv')]\n"
            "print(name, len(rows))\n"
            "PY"), "allow"),
        ("heredoc calling shutil.rmtree", run_command_call(
            "python3 - <<'PY'\nimport shutil\nshutil.rmtree('build')\nPY"), "ask"),
        ("heredoc opening a socket", run_command_call(
            "python3 - <<'PY'\n"
            "import socket\ns = socket.socket()\ns.connect(('example.com', 80))\n"
            "PY"), "ask"),
        ("heredoc writing with open(w)", run_command_call(
            "python3 - <<'PY'\nopen('out.txt', 'w').write('hello')\nPY"), "ask"),
        ("heredoc using pathlib write_text", run_command_call(
            "python3 - <<'PY'\nfrom pathlib import Path\nPath('notes.md').write_text('x')\nPY"), "ask"),
        ("heredoc calling subprocess", run_command_call(
            "python3 - <<'PY'\n"
            "import subprocess\n"
            "print(subprocess.run(['git', 'status'], capture_output=True).stdout)\n"
            "PY"), "ask"),
        ("heredoc using requests", run_command_call(
            "python3 - <<'PY'\nimport requests\nprint(requests.get('https://example.com').status_code)\nPY"), "ask"),
        ("heredoc using eval", run_command_call(
            "python3 - <<'PY'\nprint(eval(input()))\nPY"), "ask"),
        ("heredoc using importlib", run_command_call(
            "python3 - <<'PY'\nimport importlib\nm = importlib.import_module('os')\nPY"), "ask"),
        ("os imported under an alias", run_command_call(
            "python3 - <<'PY'\n"
            "import os as operating_system\noperating_system.remove('scratch.txt')\n"
            "PY"), "ask"),
        ("rmtree imported under an alias", run_command_call(
            "python3 - <<'PY'\nfrom shutil import rmtree as drop\ndrop('target')\nPY"), "ask"),
        ("star import hides the bindings", run_command_call(
            "python3 - <<'PY'\nfrom os import *\nsystem('whoami')\nPY"), "ask"),
        ("syntactically broken Python", run_command_call(
            "python3 - <<'PY'\ndef broken(:\n    print('hi'\nPY"), "ask"),
        ("unterminated heredoc", run_command_call("python3 - <<'PY'\nprint('hello')"), "ask"),
        ("unquoted heredoc with shell substitution", run_command_call(
            "python3 - <<PY\nprint('$(cat /etc/passwd)')\nPY"), "ask"),
        ("tab-stripped <<- heredoc is still parsed", run_command_call(
            "python3 - <<-'PY'\n\timport shutil\n\tshutil.rmtree('x')\n\tPY"), "ask"),

        # --- the other shapes a Python invocation takes ---
        ("benign python -c", run_command_call("python3 -c 'import sys; print(sys.version_info[:2])'"), "allow"),
        ("python -c calling os.system", run_command_call(
            "python3 -c 'import os; os.system(\"whoami\")'"), "ask"),
        ("interpreter given by absolute path", run_command_call(
            "/usr/bin/python3 -c 'import socket; socket.gethostname()'"), "ask"),
        ("source piped in on stdin cannot be read", run_command_call("echo 'print(1)' | python3 -"), "ask"),
        ("benign script on disk", run_command_call(f"python3 {safe_script_path}"), "allow"),
        ("risky script on disk", run_command_call(f"python3 {risky_script_path}"), "ask"),
        ("uv run of a script that cannot be read", run_command_call(
            "uv run tools/does-not-exist.py", cwd="/home/yunseong"), "ask"),
        ("python -m runs code this check never reads", run_command_call("python3 -m pytest -q"), "allow"),

        # --- shell shapes that must not be misread ---
        ("a here-string is not a heredoc", run_command_call("grep -c foo <<< 'foo bar'"), "allow"),
        ("prose heredoc fed to cat is not Python", run_command_call(
            "cat <<'MD' > /dev/null\n# Notes\ndef broken(: this is prose\nMD"), "allow"),
        ("two heredocs, only the Python one is inspected", run_command_call(
            "cat <<'MD' > /dev/null\n# notes\nMD\n"
            "python3 - <<'PY'\nimport os\nos.rmdir('x')\nPY"), "ask"),
        ("Python heredoc chained after another command", run_command_call(
            "git status && python3 - <<'PY'\nimport subprocess\nsubprocess.run(['ls'])\nPY"), "ask"),
    ]


def main():
    evaluator = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_EVALUATOR
    if not os.access(evaluator, os.X_OK):
        print(f"evaluator is not executable: {evaluator}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory() as scratch:
        safe_script_path = os.path.join(scratch, "report_safe.py")
        risky_script_path = os.path.join(scratch, "report_risky.py")
        with open(safe_script_path, "w", encoding="utf-8") as handle:
            handle.write(SAFE_SCRIPT)
        with open(risky_script_path, "w", encoding="utf-8") as handle:
            handle.write(RISKY_SCRIPT)

        cases = build_cases(safe_script_path, risky_script_path)
        failures = 0
        for name, payload, expected in cases:
            stdin = "" if payload is None else json.dumps(payload)
            completed = subprocess.run([evaluator], input=stdin, capture_output=True, text=True)
            output = completed.stdout.strip()
            try:
                decision = json.loads(output)["decision"]
            except (ValueError, KeyError):
                decision = "<no decision>"
            matched = decision == expected
            failures += not matched
            print(f"--- [{'OK ' if matched else 'FAIL'}] {name}  (expected {expected})")
            print(f"  stdin : {stdin or '<empty>'}")
            print(f"  stdout: {output}")
            if completed.stderr.strip():
                print(f"  stderr: {completed.stderr.strip()}")
            print()

        print(f"{len(cases) - failures}/{len(cases)} cases matched expectation")
        return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
