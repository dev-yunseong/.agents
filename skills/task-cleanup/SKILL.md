---
name: task-cleanup
description: Remove files created during the current task that no longer serve a purpose. Use when the user asks to tidy up after work, remove leftovers, or clean up the files an agent made.
---

# Clean up after a task

Start from what the agent actually did. Reconstruct the paths it created from the conversation, commands and outputs: temporary PR bodies, downloads, extracted archives, conversion intermediates, superseded drafts, test fixtures created for a one-off check, screenshots, and build or test output. Include known scratch and temporary paths outside the repository. This also works in an ordinary checkout or a non-Git folder.

For each candidate, establish who created it and whether anything still needs it. Keep the requested result, assets it references, user edits, and inputs needed by pending builds, reviews or handoffs. A screenshot delivered as the result may still be needed; a screenshot taken only to inspect a completed test can be removed. For a duplicate, verify that the retained copy is usable. File age, a temporary-looking name, or ignored/untracked status alone does not establish ownership or usefulness.

Delete the identified leftovers at their exact paths. Do not move disposable files into an archive as a substitute for deleting them. In a shared output directory, remove individual task files. Remove a whole directory only after resolving its absolute path, checking its contents (including hidden files), and confirming that it contains only disposable task output. Do not follow links into another tree. Leave ambiguous items in place and continue with the known leftovers.

If this task also created a worktree or local branch and the user wants the task cleaned up, inspect it in its owning repository. Preserve local-only commits and edits, including untracked and ignored deliverables. Verify the tip is recoverable from a current remote ref before deleting a local branch. Remove the clean task checkout with Git from another checkout, then use `git branch -d` for its local branch. On Windows a completed task-owned shell can hold an empty directory open: confirm its identity before closing it and retry removing only that empty directory.

Verify that the selected paths are gone and the retained deliverables still exist at their reported locations. Summarize what was deleted and identify anything left because its purpose was unclear.
