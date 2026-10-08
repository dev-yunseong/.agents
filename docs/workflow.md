# User-Level Workflow

## Purpose

Keep work incremental, reviewable, and aligned with existing architecture.

## Repository-Local Instructions

Every repository carries its own rules, and they take precedence over these
defaults.

1. Before the first edit in a repository, read its `AGENTS.md` and `CLAUDE.md`,
   then every more specific file along the paths you will change, then the
   documents those files require.
2. Read that repository's installed skills and use the ones that cover the
   task. A project skill holds the commands, scripts, and constraints that
   repository actually runs on, so skipping it means guessing at them.
3. Repeat both steps in every repository you enter. A workspace of submodules
   holds one instruction set per submodule, and the parent workspace file does
   not replace them.
4. Do not assume another agent already did this. Some agents load neither the
   repository's instructions nor its skills on their own, so check for yourself
   and name the files and skills you read.

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
