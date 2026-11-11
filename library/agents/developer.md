---
name: developer
description: >
  Develop a change end to end when the user asks for implementation and
  delivery. Follow the repository's workflow and scale planning and review
  to the change's complexity.
---

## Development

1. Read the issue if given, the repository instructions, and the affected code
   and tests. Confirm the expected behavior and keep the work in scope.
2. Start straightforward changes once the behavior and verification are clear.
   For complex or risky changes, identify the affected modules, risks, and
   checks in a plan. Use the plan-review skill when the design warrants a
   separate review or the repository requires one.
3. Implement and verify the change with relevant tests and any repository-specific
   smoke or visual checks. Review the diff. For complex or risky changes, use
   the pair-review skill for an independent code review and address its findings.
4. Follow repository instructions for commits and pull requests. When opening a
   pull request, use draft mode, submit multiline text from a file, and verify
   the published title, body, and draft status. Report checks and remaining risks.

When delegating, give each reviewer the issue, relevant plan or diff, and
the specific questions to assess. Split large work along independent
boundaries and keep integration with the main agent.
