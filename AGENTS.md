# AGENTS.md

## Core Philosophy

Prefer:
- maintainable architecture
- explicit structure
- scalable design
- deterministic behavior
- modular systems

Avoid:
- quick hacks
- giant rewrites
- overengineering
- hidden side effects
- meaningless abstractions

---

## Workflow

Before non-trivial implementation, follow the workflow in `~/.agents/docs/workflow.md`.

Always keep changes incremental, explain architecture decisions, call out tradeoffs, and identify risk points before editing.

When GitHub CLI authentication appears invalid inside the sandbox but the user says their session auth is valid, request escalated execution and retry the `gh` command with the user's session credentials before asking them to re-authenticate.

See:
- `~/.agents/docs/workflow.md`
- `~/.agents/library/skills/writing-plan/SKILL.md`

---

## User Preferences

See:
- `~/.agents/docs/coding-style.md`
- `~/.agents/docs/performance.md`

Project-specific preference files such as backend or Unity rules may exist in the active project. Use them only when present.

---

## Code Rules

Use `~/.agents/docs/coding-style.md` as the canonical code style source.

---

## Communication Rules

Agent must use the caveman skill.

For technical responses:
- explain WHY first
- code second
- include tradeoffs
- respect existing architecture

Avoid:
- dumping large code without explanation
- unrelated refactors
- unnecessary renaming
- pattern-first design

---

## Final Principle

Optimize for:
- long-term maintainability
- developer clarity
- scalable architecture
- real-world operation

Not:
- short-term convenience
- temporary hacks
- visually impressive complexity
