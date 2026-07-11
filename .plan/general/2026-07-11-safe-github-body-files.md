# Safe GitHub Body Files

- Date: 2026-07-11
- GitHub Issue: None

## Goal

Require issue and pull request bodies to be written to Markdown files and passed through `--body-file`.

## Scope

- Update issue creation guidance.
- Update pull request creation guidance.
- Update autonomous developer commands.
- Require post-creation body verification.

## Architecture Decisions

- Use temporary Markdown files for generated GitHub bodies unless a repository requires a tracked artifact.
- Keep title arguments separate; only multiline bodies use files.
- Verify rendered remote content after creation to catch quoting, interpolation, or truncation errors.

## Risks and Tradeoffs

- Temporary files add one lifecycle step but avoid shell quoting and multiline interpolation failures.
- Verification adds one GitHub API call per created issue or pull request.

## Validation

- Review all issue and pull request creation examples for direct multiline `--body` usage.
- Run repository diff and whitespace checks.
