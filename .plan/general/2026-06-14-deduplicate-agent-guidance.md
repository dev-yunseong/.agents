# 2026-06-14 — Deduplicate user and project agent guidance

- Date: 2026-06-14
- GitHub Issue: None
- Status: Complete

## Goal

Separate user-level defaults from project-level workflow templates and remove
duplicated guidance without weakening active rules.

## Non-goals

- Change Git, testing, or review conventions.
- Modify unrelated skills or agents.
- Update existing project copies created from the library.

## Context / Constraints

- Root `AGENTS.md` is the user-level entrypoint.
- `library/AGENTS.md` is copied into repositories by `init-project`.
- Detailed rules should have one canonical owner.

## Approach (Checklist)
- [x] **Step 0: Recon** Compare entrypoints, referenced docs, and initialization behavior.
- [x] **Step 1: Implementation** Shorten entrypoints and remove cross-document duplication.
- [x] **Step 2: Tests** Verify links, stale phrases, diff scope, and Markdown structure.
- [x] **Step 3: Rollout / Rollback** Keep changes documentation-only and independently revertible.

## Validation
- **Commands to run:** `rg`, link existence checks, `git diff --check`, `git diff`
- **Expected output:** No stale references, broken links, whitespace errors, or unrelated changes.

## Risks & Rollback
- **Risks:** Removing a duplicated sentence could accidentally weaken a required rule.
- **Rollback steps:** Revert only the affected documentation files.

## Open Questions

- None.
