# User-Level Workflow

## Changes

- Apply relevant installed skills.
- For complex or risky changes, state the plan, key tradeoffs, and risks.
  Use the writing-plan skill when a persistent plan is useful or required.
- Keep changes focused, validate in proportion to risk, and review the diff.
  Report failed, skipped, or unavailable checks.

## Worktrees

- Use `./.worktrees/<name>` in a single repository or
  `./.worktrees/<repo-name>/<name>` in a workspace with submodules.
  Use the issue key or a short branch slug for the name.
- Pass an absolute path to `git worktree add`. Verify the path is ignored
  with `git check-ignore` and use `.git/info/exclude` if needed.
- Once the pull request closes or merges, preserve any local changes before
  removing its worktree with `git worktree remove`.

## Pull Requests

- Open pull requests with `gh pr create --draft`. Leave readiness and merge
  to the developer, and report remaining checks in the handoff.
- A user-invoked release or promotion skill may merge its own pull request
  when that is part of the skill's workflow.

## Coding Style

- Use domain names that reveal intent and verbs for actions. Keep functions
  focused and control flow shallow.
- Make dependencies and side effects explicit. Prefer deterministic behavior
  and clear module boundaries.
- Refactor incrementally. Preserve behavior and architecture unless the task
  calls for a change. Keep unrelated formatting and cleanup out of the diff.
- Comment on constraints and decisions the code cannot explain on its own.

## Performance

- Measure the bottleneck first. Optimize when the expected impact matters at
  the relevant scale.
- Target the measured cause. For example, batch redundant queries, bound
  concurrency, or define cache invalidation when adding a cache.
- Compare before and after under equivalent conditions. Report the measured
  gain and any readability, coupling, or operational tradeoffs.
