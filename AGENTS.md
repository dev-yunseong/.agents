# User-Level Agent Instructions

## Scope and Precedence

These defaults apply across projects.

Follow explicit project instructions when they are more specific. User requests
and safety constraints take precedence over both user-level and project-level
defaults.

## Required Behavior

- Use the `caveman` skill for communication.
- Preserve user changes and avoid unrelated edits.
- Follow `~/.agents/docs/workflow.md` for non-trivial work.
- Follow `~/.agents/docs/coding-style.md` for code changes.
- Apply `~/.agents/docs/performance.md` only when performance is relevant.

When GitHub CLI authentication appears invalid inside a sandbox but the user
says their session is valid, request escalated execution and retry with the
user's session credentials before asking them to re-authenticate.

## Shared Resources

- Planning: `~/.agents/library/skills/writing-plan/SKILL.md`
- Project templates: `~/.agents/library/`
