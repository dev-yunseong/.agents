# ~/.agents/docs/workflow.md

## Required Workflow

Before major implementation:
1. understand the problem
2. create a short implementation plan
3. explain architecture decisions
4. explain tradeoffs and risks
5. implement incrementally

Use:
- `writing-plan` skill when a plan file is useful
- structured reasoning
- step-by-step execution

---

## Planning Rules

Plans should include:
- goal
- affected components
- risk points
- validation strategy

Keep plans concise.

---

## Implementation Rules

Prefer:
- incremental changes
- localized refactoring
- explicit reasoning
- minimal side effects

Avoid:
- giant rewrites
- unrelated refactors
- speculative abstraction
- architecture changes without explanation

---

## Communication Rules

Always:
- explain WHY first
- explain tradeoffs
- respect existing architecture

Avoid:
- code dumping
- overengineering
- unnecessary verbosity

---

## Final Principle

Optimize for:
- maintainability
- clarity
- scalability
- reliability

Not:
- temporary hacks
- complexity for its own sake
