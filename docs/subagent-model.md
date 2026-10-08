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

## Engine Routing

Claude Code, `codex exec` and `agy -p` draw on separate accounts. Work sent to
a CLI does not spend the Claude budget, so route by cost first and reach for a
Claude subagent when the task needs what only it has.

Delegation is not free: the prompt and the returned answer still land in the
parent's context. The saving is that the worker's own reading and editing
happens in a context that is thrown away. So delegate work whose input is much
larger than its answer, and never delegate something smaller than the briefing
it would take to describe.

Send to a CLI by default:

- reading a large file, log or diff and reporting what is in it
- inventory and discovery across many files or repositories
- summarising, extracting and mechanical rewriting
- a bounded edit whose acceptance criteria are already written down
- a second opinion from a model Claude Code cannot run

Keep in Claude:

- architecture, decomposition, and interface design
- deciding what to do when the answer shape is unknown
- integrating several workers' output and resolving their conflicts
- anything where a wrong judgment is expensive and hard to notice

Between the two CLIs: `codex exec` when the task needs to run a command, and
`agy -p` otherwise. An agy worker cannot run a command that is not already
listed in `permissions.allow` in `~/.gemini/antigravity-cli/settings.json`, and
it fails with no output rather than an error, so never give it a build or a
test run.

Report the engine and the reason in one clause when it is not a Claude
subagent, so a wrong route is visible rather than silent.

## Environment Mapping

Claude Code Agent tool: pass `model: "haiku"` for small, `model: "sonnet"` for
standard, and `model: "opus"` for frontier. Omitting `model` inherits the
parent agent's model; `subagent_type: "fork"` always inherits and ignores a
`model` override. An agent definition under `.claude/agents/*.md` can set the
same tier in its frontmatter `model:` field.

`codex exec`: keep the configured default model and set the depth with
`-c model_reasoning_effort="low"` for small, `"medium"` for standard and
`"high"` for frontier. Run `codex debug models` when a task wants a different
model; the catalog is per machine, so do not assume an ordering between the
names it prints.

`agy -p`: pass `--model gemini-3.8-flash-low` for small,
`gemini-3.8-flash-high` for standard and `gemini-3.1-pro-high` for frontier.
`agy models` lists what the account can reach, including Claude and GPT-OSS
models, and the Flash names already carry their depth as a suffix.

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
- Both CLIs keep their conversation, so a worker that needs one more pass is
  resumed rather than started again. `codex exec --json` prints a `thread_id`
  on its first line and `codex exec resume [OPTIONS] <id> "<prompt>"` continues
  it, with every option before the id. `agy --output-format json` returns a
  `conversation_id` and `agy -p "<prompt>" --conversation <id>` continues that
  one.
- State the tier assignment briefly when spawning more than one subagent.
