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

## Canonical Spec

When creating multiple skills, prefer a JSON spec and generate both targets with `scripts/build_dual_skill.py`.

Minimum spec:

```json
{
  "name": "write-release-notes",
  "title": "Write Release Notes",
  "description": "Draft release notes from commits, PRs, changelogs, or issue lists. Use when users ask for customer-facing, internal, or technical release notes.",
  "body": "## Workflow\n\n1. Inspect the supplied changes.\n2. Group user-visible changes by theme.\n3. Draft concise release notes.\n",
  "codex": {
    "display_name": "Write Release Notes",
    "short_description": "Draft clear release notes",
    "default_prompt": "Use $write-release-notes to turn these merged PRs into customer-facing release notes."
  }
}
```

Run:

```bash
python3 scripts/build_dual_skill.py spec.json --out ./dist
```

Read `references/portable-skill-format.md` before designing a new cross-platform skill or changing the generator contract.

## Authoring Rules

- Put trigger guidance in the description because it is what agents see before loading the full body.
- Keep `SKILL.md` concise; move long schemas, policies, examples, or API details into `references/`.
- Include scripts only for deterministic or repetitive operations, and test every added script directly.
- Keep shared instructions platform-neutral unless a platform genuinely needs different behavior.
- Do not include setup guides, changelogs, or user-facing README files inside the skill package.
- Remove placeholder text before validation.

## Validation

For each generated skill:

- Confirm the folder name equals the frontmatter `name`.
- Confirm `description` states both capability and use cases.
- Confirm every referenced resource exists.
- Confirm there are no TODO markers or template instructions.
- For Codex packages, run the Codex quick validator when available:
  `python3 /path/to/quick_validate.py path/to/skill`.
