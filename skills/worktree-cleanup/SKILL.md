---
name: worktree-cleanup
description: Clean up Git worktrees and local branches created for a finished task or PR. Use when asked to remove task checkouts, preserve their deliverables, or recover from a Windows worktree removal blocked by an open handle.
---

# Clean up a task's worktrees

1. Identify candidates from the task's recorded paths, branch names and PRs. In each owning repository (including each affected submodule), use `git worktree list --porcelain` to match the absolute path, branch or detached HEAD, and commit. Run cleanup from a surviving checkout. Leave the main checkout, other tasks, locked worktrees and ambiguous paths alone.
2. Inspect each candidate before removing anything. Use `git -C <path> status --short --untracked-files=all` for staged, modified and untracked files, and `git -C <path> clean -ndX` to preview ignored files. Inspect nested repositories separately. Preserve requested outputs outside the worktree and verify the copy before removing its source. Keep the worktree when a user's edit, ignored local configuration or unexplained file still needs a home. Disposable build outputs may go with the checkout.
3. Verify commit recovery separately from file recovery. Fetch the relevant remote ref and check that the exact worktree HEAD is reachable from it (for example, `git merge-base --is-ancestor <head> <fetched-ref>`). A closed PR, a stale tracking ref or a squash merge alone does not prove this. If the head is local-only, including a detached HEAD, keep a named local ref to it and report it. For an open PR, remove its checkout only when cleanup was requested and its current head is preserved remotely.
4. Recheck the path, HEAD and status immediately before removal. Run `git -C <owner> worktree remove <absolute-path>` for that checkout. If Git refuses, inspect the reason. Avoid force-removal, repository-wide clean/prune, and deleting remote branches. Once unregistered, delete the task's local branch with `git branch -d <branch>` only if its tip is preserved, its ref still matches the inspected SHA, and no other worktree uses it. If Git refuses, retain the branch and report why.
5. Verify both the Git registration and the directory have disappeared. Verify which local refs were removed or retained. Report preserved files at their new locations, any open PRs, and anything deliberately kept.

## Windows directory locks

Git can unregister a worktree and remove its contents yet leave an empty directory after a permission error. Recheck both states before retrying. Identify the process holding that exact path and verify its command and ownership. Close only a completed task-owned shell or helper. Leave an active user application running. From a surviving checkout, resolve the absolute target, confirm its parent is the intended worktree directory and that the target is empty, then remove the empty directory non-recursively. Keep the path if ownership or contents are uncertain.
