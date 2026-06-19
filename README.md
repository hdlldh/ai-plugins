# AI Plugins Repository

This repository contains portable AI skill packages for Claude and Codex.

## Structure

- `claude/` — Claude skill packages
- `codex/` — Codex skill packages

Each skill package is organized as a separate folder:

- `youtube-video-script-generator/` — a skill for generating YouTube long-form scripts and related short-form scripts with orchestrator, writer, and reviewer workflow.

## Installation

### Claude

1. Copy the desired skill folder from `claude/` into your Claude skills workspace.
2. Confirm the skill folder contains `SKILL.md` at its root.
3. Register or upload the folder in your Claude environment.

### Codex

1. Copy the desired skill folder from `codex/` into your Codex skills workspace.
2. Confirm the skill folder contains `SKILL.md` and `agents/openai.yaml`.
3. Register or upload the folder in your Codex environment.

## Usage

Ask the skill for YouTube script creation with requirements such as topic, audience, tone, and desired outcomes. For the `youtube-video-script-generator` skill, the workflow includes:

- Collecting user requirements via an orchestrator
- Generating a long-form video script and related short-form scripts via a writer
- Reviewing and refining outputs via a reviewer
- Stopping after a pass or after three refinement iterations

## Notes

- `README.md` files inside each skill folder provide package-specific installation instructions.
- This repository does not include additional runtime dependencies; the skills are defined by their metadata and instructions.
