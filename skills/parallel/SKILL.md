---
name: parallel
description: >
  Parallelize development when the user requests it or when multiple work
  tracks have independent write scopes. Map ownership before delegating.
---

1. Identify the requested tracks. For a priority batch, read
   `./.agents/PRIORITY.md` and relevant handoffs if present.
2. Check dependencies and likely file, configuration, migration, and contract
   overlap. Delegate only tracks with clear write ownership. Work serially
   when fewer than two tracks can safely run independently.
3. Keep decomposition and integration with the main agent. Explain the
   partition briefly. Follow `~/.agents/docs/subagent-model.md` for model and
   tool selection and `~/.agents/docs/workflow.md` for worktree placement.
4. Give each worker an isolated worktree, its exact task and write scope,
   required checks, and the instruction to preserve other workers' changes.
   Include all context up front for workers that cannot receive live messages.
5. Review each diff and resolve integration conflicts in the main agent.
   Run focused checks per track and integration checks for shared behavior.
   Report changed files, checks, and unresolved assumptions.
