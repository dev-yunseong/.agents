# Commit Workflow

## Why

Each commit should explain one coherent change and remain safe to review or revert independently.

## Format

Use Conventional Commits:

```text
<type>(<optional-scope>): <한글 요약>
```

Examples:

```text
feat(auth): 세션 만료 기능 추가
fix(api): 빈 업스트림 응답 처리
docs: 로컬 테스트 방법 문서화
```

Use the same types defined in [`branch.md`](branch.md).

## Rules

- Keep subject at 50 characters or fewer when practical.
- Write the summary after `<type>: ` in Korean. Leave code identifiers, API
  names, CLI commands, and error strings in their original form.
- Do not end subject with a period.
- Describe why in body when motivation is not obvious.
- Reference issue in footer when repository automation requires it.
- Do not mix unrelated behavior, formatting, and refactoring.
- Do not commit secrets, generated noise, or local-only configuration.

## Line Endings

A repository stores text with LF. Carry a `.gitattributes` from the first
commit:

```text
* text=auto eol=lf

*.cmd text eol=crlf
*.bat text eol=crlf
```

`text=auto` stores text as LF in the repository and `eol=lf` checks it out as
LF. Windows batch files are the exception: stored as LF, restored as CRLF on
checkout, because `cmd.exe` needs CRLF to run them. `init-project` installs this
file. Without it `core.autocrlf` decides, and its default converts nothing on
Linux or macOS.

When a repository predates the rule, add the file and renormalize the index in
the same commit:

```bash
git add --renormalize .
```

That commit changes line endings and nothing else. Do not mix it with behavior
or refactoring, state the affected file count in the body, and record its hash
in `.git-blame-ignore-revs` when blame history matters. The working tree keeps
its old line endings until the next checkout, so a clean `git status` after
renormalizing is expected.

## Body

Add a body when change has non-obvious constraints or tradeoffs:

```text
fix(cache): 새로고침 중 기존 캐시 값 유지

동시에 새로고침이 겹치면 읽을 수 있던 값까지 비웠다. 교체가 성공할 때까지
이전 값을 남겨 호출부가 예측 가능한 대체 동작을 유지하게 한다.

Refs #123
```
