---
name: parallel
description: >
  Parallelize development work safely. Use when the user asks to develop
  multiple issues, a batch of priorities, "next several issues", "parallel
  develop", or when a develop request clearly contains 2+ independent work
  tracks. For issue-driven work, select only tasks with disjoint write scopes
  or clean ownership boundaries, then spawn worker subagents to implement them
  in parallel. If scope overlap is likely, do not force parallelism; fall back
  to serial development.
---

1. Resolve the worklist before spawning anything.
   - If the request names issue numbers, fetch each issue and read enough local code to map likely files.
   - If the request says "next priorities" or similar, read `./.agents/PRIORITY.md` and pick the highest-priority ready items.
   - If `./.agents/handoffs/LATEST.md` exists and is relevant, read it before planning.

2. Run a conflict check.
   - For each candidate issue or work track, identify:
     - likely files and packages
     - likely shared abstractions
     - required migrations, configs, and tests
   - Parallelize only when ownership can be made explicit and the write scopes are meaningfully disjoint.
   - Treat these as conflict risks by default:
     - the same file or class
     - the same Gradle or runtime config
     - the same SQL seed or migration file
     - the same shared DTO, protocol, or game rule surface
     - one task depending on unfinished output from another

3. Choose the execution shape.
   - If fewer than 2 safe tracks remain, do the work serially and say why parallelism was rejected.
   - If 2+ safe tracks remain, keep the coordination task locally and spawn worker subagents for the implementation tracks.
   - Keep blocking architecture or decomposition work in the main agent. Delegate bounded execution, not the critical planning step.

4. Select the lowest model sufficient for each task.
   - Follow `~/.agents/docs/subagent-model.md` for the tiers and the
     environment mapping.
   - Respect an explicit user model choice first.
   - Keep the coordination, decomposition, and integration review on the
     parent model.
   - Model selection never relaxes ownership, validation, or review
     requirements.

5. Choose the engine for each worker.
   - Route by cost first, following the engine routing in
     `~/.agents/docs/subagent-model.md`. The CLIs draw on separate accounts, so
     a track sent to one does not spend the Claude budget. Keep decomposition
     and integration in Claude and send the bounded execution out.
   - `codex exec` takes a track that has to run commands. It edits files,
     runs shell commands, and reports back. `--cd <worktree>` sets its
     working root, `-m` its model,
     `-c model_reasoning_effort="low|medium|high"` its depth, `--json` a JSONL
     event stream, and `--output-last-message <file>` just the final answer.
   - `agy -p "<prompt>"` takes the rest. It reads and edits files, but a shell
     command only runs when its prefix is listed in `permissions.allow` in
     `~/.gemini/antigravity-cli/settings.json`; anything else is refused with
     no output, so do not give an agy worker a track that has to build or
     test. It does not inherit the working directory: pass `--add-dir
     <worktree>` or it runs somewhere else entirely.
   - Neither CLI is confined on this machine. Their `--sandbox` flags do not
     stop a write outside the worktree, and codex's automatic review does not
     refuse a destructive command. Give these workers a throwaway worktree,
     read the diff before integrating, and never point one at a checkout whose
     loss would cost something.

6. Define ownership precisely for every worker.
   - Give each worker:
     - the exact issue or subtask
     - the files or module boundaries it owns
     - the tests it should run
     - the instruction that it is not alone in the codebase and must not revert others' edits
   - Ask each worker to report:
     - files changed
     - tests run
     - unresolved risks or assumptions

7. Integrate deliberately.
   - While workers run, do non-overlapping work locally: shared analysis, follow-up issue reads, integration prep, or validation setup.
   - Review returned diffs before making further edits.
   - If worker outputs collide in practice, resolve conflicts in the main agent instead of bouncing the same file between workers.

8. Validate at the right level.
   - Prefer targeted tests per track first, then run broader validation after integration.
   - If one parallel track fails, do not block the others from landing unless the failure invalidates shared assumptions.

## Rules

- Parallelism is optional optimization, not a goal by itself.
- Never split work across workers when the write boundary is vague.
- Prefer issue-level parallelism over file-level micro-splitting.
- When a single issue contains multiple independent concerns, decompose into explicit subtracks before spawning workers.
- Always explain the chosen partition and model assignment briefly before spawning workers.
- Say which engine each worker runs on when any of them is not a Claude subagent.
- A codex or agy worker cannot be messaged while it runs. Give it everything it
  needs up front; a follow-up only lands after it has finished.
