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
   - Respect an explicit user model choice first.
   - Use `gpt-5.4-mini` for deterministic, low-risk work:
     - mechanical file moves or renames with explicit mappings
     - formatting, inventory, search, and focused validation
     - small isolated edits with clear acceptance criteria
   - Use `gpt-5.4` for normal implementation:
     - bounded feature or bug work in a known architecture
     - multi-file changes with clear ownership
     - tests, migrations, and integration work requiring moderate reasoning
   - Inherit the main agent's default frontier model for high-risk or ambiguous work:
     - architecture and decomposition
     - security-sensitive changes
     - broad refactors or unclear behavioral contracts
     - conflict resolution and final integration review
   - When uncertain between tiers, choose the stronger model.
   - Do not override the model when the task is too coupled to classify confidently; inherit the parent model.
   - Model selection never relaxes ownership, validation, or review requirements.

5. Define ownership precisely for every worker.
   - Give each worker:
     - the exact issue or subtask
     - the files or module boundaries it owns
     - the tests it should run
     - the instruction that it is not alone in the codebase and must not revert others' edits
   - Ask each worker to report:
     - files changed
     - tests run
     - unresolved risks or assumptions

6. Integrate deliberately.
   - While workers run, do non-overlapping work locally: shared analysis, follow-up issue reads, integration prep, or validation setup.
   - Review returned diffs before making further edits.
   - If worker outputs collide in practice, resolve conflicts in the main agent instead of bouncing the same file between workers.

7. Validate at the right level.
   - Prefer targeted tests per track first, then run broader validation after integration.
   - If one parallel track fails, do not block the others from landing unless the failure invalidates shared assumptions.

## Rules

- Parallelism is optional optimization, not a goal by itself.
- Never split work across workers when the write boundary is vague.
- Prefer issue-level parallelism over file-level micro-splitting.
- When a single issue contains multiple independent concerns, decompose into explicit subtracks before spawning workers.
- Always explain the chosen partition and model assignment briefly before spawning workers.
