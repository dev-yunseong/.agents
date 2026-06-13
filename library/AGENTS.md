# AGENTS.md

## Purpose

This file defines repository-wide instructions for coding agents.

Optimize for:
- maintainability
- explicit structure
- deterministic behavior
- small, reviewable changes
- real-world operation

Avoid:
- quick hacks
- unrelated refactors
- hidden side effects
- speculative abstractions
- large rewrites without explicit approval

## Project Context

Read [`.agents/docs/project.md`](.agents/docs/project.md) before making non-trivial changes.

Project-specific instructions override general workflow defaults when they are explicit and more restrictive.

## Required Workflow

For non-trivial work:
1. understand current behavior and constraints
2. inspect relevant code and tests
3. use the `writing-plan` skill to write or update a plan
4. identify architecture decisions, tradeoffs, and risks
5. implement incrementally
6. follow `.agents/docs/testing.md`; use an installed testing skill when available
7. review the diff before handoff

See:
- [`.agents/docs/workflow.md`](.agents/docs/workflow.md)
- [`.agents/docs/testing.md`](.agents/docs/testing.md)

## Git Workflow

Follow:
- [`.agents/docs/issue.md`](.agents/docs/issue.md)
- [`.agents/docs/branch.md`](.agents/docs/branch.md)
- [`.agents/docs/commit.md`](.agents/docs/commit.md)
- [`.agents/docs/pull-request.md`](.agents/docs/pull-request.md)

Use `writing-plan` for plan creation and `plan-review` when plan review is
needed. Skill instructions define plan format and paths.

Never discard user changes or rewrite shared history without explicit approval.

## Code Rules

Prefer:
- intent-revealing names
- small functions with one responsibility
- explicit dependencies
- shallow control flow
- domain-specific modules
- tests at the behavior boundary

Avoid:
- generic `Manager`, `Helper`, `Utils`, or `Misc` containers
- premature optimization
- broad formatting churn
- comments that repeat code

Respect established repository patterns unless changing them is part of the task.

## Communication

Explain why before implementation details. State tradeoffs, risks, validation performed, and anything not verified.

Keep responses concise. Do not dump large code blocks when a file reference or focused excerpt is enough.
