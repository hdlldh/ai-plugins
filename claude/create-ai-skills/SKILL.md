---
name: create-ai-skills
description: Create portable AI skills for Claude and Codex from one reusable design. Use when the user wants to create, update, package, validate, or adapt SKILL.md-based skills for Claude, Claude Code, Codex, or cross-agent skill libraries, including skills with scripts, references, assets, metadata, examples, or installation-ready folders.
---

# Create AI Skills

## Overview

Create one canonical skill design, then emit platform-specific folders for Codex and Claude. Keep the shared instructions aligned while allowing small metadata and packaging differences.

## Workflow

1. Clarify the concrete skill purpose with 2-4 realistic user prompts.
2. Choose a short hyphen-case skill name under 64 characters.
3. Decide whether the skill needs only `SKILL.md` or also `scripts/`, `references/`, or `assets/`.
4. Draft platform-neutral instructions first: core workflow, resource routing, validation expectations, and safety boundaries.
5. Add platform-specific metadata:
   - Codex: YAML frontmatter with `name` and `description`; optional `agents/openai.yaml`.
   - Claude: `SKILL.md` with clear name/description metadata and concise task instructions; package as a folder or zip depending on the Claude surface.
6. Validate by checking frontmatter, file names, stale placeholders, resource references, and a realistic invocation prompt.

## Resources

Read `references/portable-skill-format.md` before designing a new cross-platform skill or changing the generator contract.

For repeated creation, use `scripts/build_dual_skill.py` with a JSON spec:

```bash
python3 scripts/build_dual_skill.py spec.json --out ./dist
```

The generated Claude skill should keep only the resources needed for the resulting workflow.

## Validation

Confirm the folder name equals the frontmatter `name`, the description includes trigger scenarios, all referenced resources exist, and there are no TODO markers or template instructions.
