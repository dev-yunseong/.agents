# User-Level Subagent Model Selection

## Model Selection

Use the weakest model that can do the work reliably. Honor the user's
model choice. Choose the stronger tier when in doubt and inherit the parent
model when the task cannot be classified. Keep blocking design and final
integration with the main agent.

| Tier | Task | Claude Code | Codex reasoning | Antigravity |
| --- | --- | --- | --- | --- |
| Small | Mechanical edits and inventory | `haiku` | `low` | `gemini-3.8-flash-low` |
| Standard | Bounded implementation, tests, or review | `sonnet` | `medium` | `gemini-3.8-flash-high` |
| Frontier | Ambiguous contracts or costly judgment | `opus` | `high` | `gemini-3.1-pro-high` |

## Command-Line Workers

Delegate when the worker's input is much larger than its expected answer.
Use `codex exec` for work needing commands and `agy -p` for suitable read-only
work. Antigravity requires commands to be in `permissions.allow`. Mention the
engine and why you chose it. State the tiers when spawning multiple workers.

- Claude Code forks inherit the parent model.
- Codex uses the configured model with `-c model_reasoning_effort="<tier>"`,
  using the reasoning value from the table. Use `codex debug models` for model
  discovery and `codex exec resume [OPTIONS] <thread_id> "<prompt>"` to continue.
- Antigravity accepts `--model` and lists options with `agy models`. Use the
  `conversation_id` from `--output-format json` with `--conversation <id>`
  to continue.
