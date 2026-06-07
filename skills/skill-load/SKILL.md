---
name: skill-load
description: Copies skills/agents from library (~/.agents/library/) to active project.
---

# skill-load Skill

Loads global skills/agents from `~/.agents/library/` to `<project_root>/.agents/` (or `.claude/`).

## Trigger Conditions
Use when requested to "load/copy/install global skill/agent".

## Workflow

### Step 1: Setup & Paths
1. Source:
   - Skills: `~/.agents/library/skills/`
   - Agents: `~/.agents/library/agents/`
2. Destination:
   - Skills: `<project_root>/.agents/skills/`
   - Agents: `<project_root>/.agents/agents/` (or `<project_root>/.claude/agents/`)
3. If specific skill/agent not specified, list options in source directory and prompt user.

### Step 2: Copy & Collision Handling
1. Ensure destination parent directory exists.
2. Copy files:
   - Skill (directory): `cp -r ~/.agents/library/skills/<name> <project_root>/.agents/skills/`
   - Agent (file): `cp ~/.agents/library/agents/<file> <project_root>/.agents/agents/`
3. Collision: If exists, ask user confirmation before overwrite.

### Step 3: Verify
Confirm destination files exist and are readable. Report status.
