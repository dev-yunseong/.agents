# User-Level Agent Instructions

## Scope and Precedence

These defaults apply across projects.

Follow explicit project instructions when they are more specific. User requests
and safety constraints take precedence over both user-level and project-level
defaults.

## Required Behavior

- Use the `caveman` skill for communication.
- Preserve user changes and avoid unrelated edits.
- Before non-trivial work in a workspace that contains child repositories,
  discover every `AGENTS.md` that applies to each repository in scope. Read the
  repository-level file and every more-specific file along the paths that may
  be changed, then read all instruction documents those files require. Repeat
  this check separately for every child repository; do not assume the parent
  workspace instructions replace repository-local instructions.
- Use the `parallel` skill for development work and run it wide: split the work
  into as many tracks with disjoint write scopes as it holds, and spawn a
  subagent for each. Serial is the exception, not the default. Take it only when
  fewer than two safe tracks exist, and say which it was and why.
- Follow `~/.agents/docs/workflow.md` for non-trivial work.
- Follow `~/.agents/docs/coding-style.md` for code changes.
- Apply `~/.agents/docs/performance.md` only when performance is relevant.

When GitHub CLI authentication appears invalid inside a sandbox but the user
says their session is valid, request escalated execution and retry with the
user's session credentials before asking them to re-authenticate.

## Shared Resources

- Planning: `~/.agents/library/skills/writing-plan/SKILL.md`
- Project templates: `~/.agents/library/`
