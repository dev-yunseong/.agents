# User-Level Agent Instructions

## Scope and Precedence

These defaults apply across projects.

Follow explicit project instructions when they are more specific. User requests
and safety constraints take precedence over both user-level and project-level
defaults.

## Writing

- Reply in natural Korean when the user speaks Korean. Lead with the outcome,
  include only details needed to understand or act, and keep a warm, direct tone.
- Write out terms, names, and identifiers. Use precise, established terminology
  and keep English technical terms where Korean would require a coined translation.
  Qualify ambiguous terms, such as screen capture, and match existing wording
  when editing part of a passage.
- Name concrete changes and use numbers when they matter. In Korean work-item
  titles and headings, name what changed and end with a noun such as 추가 or 수정.
- Use backticks for code, paths, commands, identifiers, and literal values.

## Working Across Projects

- Preserve user changes and keep edits in scope.
- Before non-trivial work, read the instructions that govern each repository and
  affected path, including child repositories and their required references.
- Use the parallel skill when development has multiple independent tracks.
  Give each track a subagent with a disjoint write scope. Read [subagent model guidance](docs/subagent-model.md)
  when delegating.
- Follow [workflow](docs/workflow.md) for non-trivial work, [coding style](docs/workflow.md#coding-style)
  for code changes, and [performance guidance](docs/workflow.md#performance) when relevant.
- Follow [Hindsight guidance](docs/hindsight.md) when configuring or diagnosing
  Hindsight. Use the shared `yunseong` bank across environments.
- If GitHub CLI authentication fails in the sandbox and the user confirms their
  session is valid, retry with escalated execution before asking them to sign in.

## Pull Request Review Threads

When addressing review feedback, push fixes to the pull request's branch, then resolve the threads those fixes address.

## Shared Resources

- Planning: `~/.agents/library/skills/writing-plan/SKILL.md`
- Project templates: `~/.agents/library/`
