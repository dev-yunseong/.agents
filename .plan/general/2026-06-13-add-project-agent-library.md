# 2026-06-13 — Add project agent library

- Date: 2026-06-13
- GitHub Issue: None
- Status: Complete

## Goal

Create reusable project-level `AGENTS.md` and workflow documents under `library/`, plus a dedicated initialization skill that extends `/init` and installs them into a project.

## Non-goals

- Replacing the existing `skill-load` behavior.
- Defining language- or framework-specific coding rules.
- Automatically modifying existing project files without conflict checks.

## Context / Constraints

- Source templates live under `~/.agents/library/`.
- Installed project documents must use project-local references.
- Existing project files and user changes must be preserved.

## Approach (Checklist)
- [x] **Step 0: Recon** (Inspect existing code, locate files)
- [x] **Step 1: Implementation** (Add templates, skill references, and init skill)
- [x] **Step 2: Tests** (Validate links, paths, frontmatter, and shell examples)
- [x] **Step 3: Rollout / Rollback** (Document usage and keep changes independently removable)

## Validation
- **Commands to run:** `find library -maxdepth 3 -type f`, targeted `rg`, `git diff --check`
- **Expected output:** All referenced library files exist; no whitespace errors; init instructions preserve existing files.

## Risks & Rollback
- **Risks:** Rules may be too rigid for some repositories; initialization could collide with existing files.
- **Rollback steps:** Remove the added library templates and `init-project` skill.

## Open Questions

- None. Use conservative defaults with documented project overrides.
