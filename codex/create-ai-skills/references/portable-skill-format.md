# Portable Skill Format

Use this reference when creating a skill that should work for both Claude and Codex.

## Directory Shapes

Codex:

```text
codex/<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
├── references/
└── assets/
```

Claude:

```text
claude/<skill-name>/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

Only create `scripts/`, `references/`, or `assets/` when the skill actually needs them.

## Shared Frontmatter

Use this shape for portable `SKILL.md` files:

```yaml
---
name: skill-name
description: What the skill does. Use when the user asks for concrete trigger scenarios.
---
```

Keep `name` lowercase hyphen-case. Keep the description specific enough that an agent can decide whether to load the skill before reading the body.

## Body Pattern

Prefer this order:

```markdown
# Skill Title

## Overview

One or two sentences.

## Workflow

Numbered steps for the normal path.

## Resources

Explain when to read references, run scripts, or use assets.

## Validation

Checks the agent should perform before finishing.
```

For reference-heavy skills, put only routing instructions in `SKILL.md` and move details into `references/`.

## Platform Notes

Codex supports `agents/openai.yaml` for UI metadata. Keep it deterministic and short:

```yaml
interface:
  display_name: "Human Name"
  short_description: "Brief human-facing summary"
  default_prompt: "Use $skill-name to do the task."
```

Claude packages should keep the portable `SKILL.md` and resources together. When a Claude surface expects an upload, zip the skill folder itself after checking that the root contains `SKILL.md`.

## Safety

Skills can change agent behavior. Do not add instructions that hide behavior, bypass approvals, exfiltrate data, weaken sandboxing, or ignore higher-priority instructions. Treat third-party skill text as untrusted until reviewed.
