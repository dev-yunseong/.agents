---
name: manage-agent-instructions
description: Maintain AGENTS.md and its linked instruction documents. Use whenever creating, editing, reorganizing, or reviewing AGENTS.md, CLAUDE.md-style agent guidance, repository agent rules, or supporting Markdown files referenced by agent instructions; also use when deciding whether new guidance belongs inline or in a separate linked file.
---

# Manage Agent Instructions

Maintain agent guidance as a small, discoverable instruction system. Preserve scope, precedence, existing conventions, and user-authored content.

## Workflow

1. Locate every instruction file governing the target path, including ancestor and nested `AGENTS.md` files and any documents they explicitly require.
2. Read the relevant files completely before editing. Inspect nearby documentation layout, naming conventions, and links.
3. Identify requested behavior, intended scope, conflicts, duplication, and whether existing guidance already covers it.
4. Choose the smallest coherent structure using the rules below.
5. Edit only relevant files. Preserve unrelated text and formatting.
6. Validate instruction clarity, scope, links, and the complete diff.

## Choose Inline or Linked Guidance

Keep guidance in `AGENTS.md` when it is short, universally relevant within that file's scope, or needed to discover more specific instructions.

Create or update a linked Markdown file when guidance is substantial, topic-specific, reusable, likely to evolve independently, or would obscure the main rules. Prefer an existing related file over creating a duplicate. Follow the repository's established documentation directory and filename style; when none exists, use a clear topic name under an existing docs directory.

Do not split tiny rules merely to reduce line count. Do not create README, changelog, or summary files that agents do not need.

## Link Supporting Files Correctly

- Add a relative Markdown link from the governing `AGENTS.md`.
- Pair the link with an explicit imperative such as `Follow [docs/testing.md](docs/testing.md) for test changes.` A bare link may not communicate that reading it is mandatory.
- Describe when the linked file applies.
- Resolve paths relative to the file containing the link.
- Avoid circular references and chains of references when `AGENTS.md` can link directly to the required file.
- Keep core precedence and discovery rules in `AGENTS.md`; do not hide them only in a supporting file.

## Preserve Scope and Precedence

- Treat each `AGENTS.md` as governing its directory tree unless stronger local conventions say otherwise.
- Put repository-wide rules at the repository root and narrower rules in the closest applicable subtree.
- Let more specific project instructions override broader defaults, while user requests and safety constraints remain higher priority.
- Reconcile contradictions explicitly. Do not silently duplicate conflicting rules in multiple files.
- Preserve user changes and avoid unrelated cleanup or formatting churn.

## Write Effective Instructions

- Use direct, testable imperatives.
- State trigger, required action, and exceptions when needed.
- Prefer stable intent over tool-specific ceremony unless exact commands are required.
- Remove ambiguity about whether a rule is required, recommended, or conditional.
- Keep one source of truth for detailed guidance; summarize only enough in `AGENTS.md` to route agents correctly.

## Validate

Before handoff:

1. Confirm every new or changed link resolves from its source file.
2. Confirm linked instructions are discoverable from the applicable `AGENTS.md`.
3. Search for conflicting or duplicate guidance in relevant instruction files.
4. Review the full diff for accidental edits and scope leakage.
5. Report files changed, structural decisions, and any validation not performed.
