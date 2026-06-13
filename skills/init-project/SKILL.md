---
name: init-project
description: >
  Extends the environment's /init workflow with project-level agent
  instructions from ~/.agents/library. Installs AGENTS.md and workflow
  documents when asked to initialize or bootstrap a project.
---

# init-project Skill

## Why

`/init` discovers or creates baseline repository guidance. This skill follows
that initialization and installs reusable governance files from the library.

Use `skill-load` separately for optional skills and agents.

## Source

- `~/.agents/library/AGENTS.md`
- `~/.agents/library/docs/`

## Destination

- `<project_root>/AGENTS.md`
- `<project_root>/.agents/docs/`

## Workflow

1. Run or follow the environment's standard `/init` workflow first.
   - Preserve useful repository-specific guidance it discovers or creates.
   - Do not replace `/init`; extend its result with library documents.
2. Determine project root:
   - Prefer `git rev-parse --show-toplevel`.
   - Otherwise use current working directory.
3. Verify source files exist and are readable.
4. Inspect destination for existing `AGENTS.md` and `.agents/docs/`.
5. If any destination file exists:
   - compare content
   - leave identical files unchanged
   - ask before replacing or merging different files
   - never silently overwrite
6. Merge library `AGENTS.md` rules with `/init` output when both exist.
   - preserve repository-specific commands and constraints
   - add missing library workflow references
   - ask before resolving conflicting instructions
7. Create destination directories.
8. Copy approved missing files.
9. Replace placeholders in `.agents/docs/project.md` only from verified project data.
   Leave unknown values as `TODO`.
10. Validate:
   - all links from `AGENTS.md` resolve
   - all expected docs exist
   - no unrelated files changed
11. Report created, unchanged, skipped, merged, and conflicting files.

## Optional Follow-up

After base initialization, offer available library skills or agents through
`skill-load`. Do not install them automatically.

## Rules

- Keep templates as source material; project copies may diverge intentionally.
- Treat `/init` output as project-specific context, not disposable boilerplate.
- Project-specific existing rules take precedence during a merge.
- Do not add framework-specific rules without evidence from repository.
- Do not initialize Git, create a branch, or make a commit unless requested.
