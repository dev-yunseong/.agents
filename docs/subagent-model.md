# User-Level Subagent Model Selection

## Purpose

Match each spawned subagent to the weakest model that can still finish its
task correctly. Cheap tasks should not burn frontier capacity, and hard tasks
should never be handed to a model that cannot reason through them.

## When To Apply

Apply this whenever a subagent is spawned, not only inside the `parallel`
skill: implementation workers, delegated searches, review passes, and one-off
background tasks all pick a model the same way.

## Tiers

Classify by what the task demands, not by how many files it touches.

Small — deterministic work with an explicit specification and a cheap
correctness check:

- mechanical renames, moves, or replacements with a given mapping
- formatting, inventory, and file discovery
- reading a known location and reporting what is there
- small isolated edits with clear acceptance criteria

Standard — bounded engineering inside an architecture that is already
understood:

- feature or bug work scoped to known files
- multi-file changes with explicit ownership
- tests, migrations, and integration work needing moderate reasoning
- focused code review of a bounded diff

Frontier — work where a wrong judgment is expensive or hard to detect:

- architecture, decomposition, and interface design
- security-sensitive changes
- broad refactors and unclear behavioral contracts
- conflict resolution and final integration review
- open-ended investigation with no known answer shape

## Environment Mapping

Claude Code Agent tool: pass `model: "haiku"` for small, `model: "sonnet"` for
standard, and `model: "opus"` for frontier. Omitting `model` inherits the
parent agent's model; `subagent_type: "fork"` always inherits and ignores a
`model` override. An agent definition under `.claude/agents/*.md` can set the
same tier in its frontmatter `model:` field.

Codex-style CLIs: the small or everyday model at low reasoning effort for
small, the everyday coding model at medium reasoning for standard, and the
strongest available model at high reasoning for frontier.

Single-tier environments: keep the tier decision in the spawn message so the
intended depth is still visible, and adjust reasoning effort where the CLI
exposes it.

## Rules

- An explicit user model choice wins over every rule here.
- When a task sits between two tiers, choose the stronger one.
- When the task is too coupled or too vague to classify, inherit the parent
  model instead of guessing.
- Model selection never relaxes ownership boundaries, validation, or review
  requirements.
- Keep blocking architecture and decomposition work in the main agent rather
  than delegating it to a frontier subagent.
- State the tier assignment briefly when spawning more than one subagent.
