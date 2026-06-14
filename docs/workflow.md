# User-Level Workflow

## Purpose

Keep work incremental, reviewable, and aligned with existing architecture.

## Non-Trivial Work

Before editing:

1. Confirm goal, scope, constraints, and current behavior.
2. Inspect relevant code, tests, configuration, and recent changes.
3. State a concise implementation plan.
4. Explain architecture decisions, tradeoffs, and risk points.

Use the `writing-plan` skill when a persistent plan file is useful or required
by project instructions.

During implementation:

1. Make the smallest coherent change.
2. Preserve established patterns unless the task requires changing them.
3. Keep unrelated cleanup out of scope.
4. Validate incrementally, with depth proportional to risk and blast radius.
5. Review the complete diff before handoff.

## Decision Rules

- Add abstractions only when they remove demonstrated complexity or match an
  established pattern.
- Prefer deterministic behavior and explicit dependencies.
- Prefer reversible changes for high-risk behavior.
- Never hide failed, skipped, or unavailable validation.
- Stop before destructive or high-impact ambiguous actions that lack approval.

## Communication

- Explain why before implementation details.
- State tradeoffs, risks, validation performed, and anything not verified.
- Keep responses concise.
- Prefer file references or focused excerpts over large code dumps.

## Outcome

Optimize for maintainability, clarity, scalability, reliability, and real-world
operation. Avoid temporary hacks, speculative complexity, and large rewrites
without explicit need.
