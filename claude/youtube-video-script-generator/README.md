# YouTube Video Script Generator Skill

This skill generates a YouTube long-form video script plus related short-form video scripts, with built-in orchestrator, writer, and reviewer workflow.

## Installation

1. Copy the `youtube-video-script-generator` folder into your Claude skills workspace.
2. Confirm that `SKILL.md` is present at the root of the imported folder.
3. Upload or register the folder in your Claude skill manager according to your Claude environment.

## Usage

- The skill is triggered by asking for YouTube video scripts that include a long-form script, shorts, titles, and review/refinement logic.
- The skill is designed to generate:
  - one 8+ minute regular video script
  - multiple related short scripts under 3 minutes
  - strong titles for both long and short videos
  - structured evaluation and up to three refinement iterations

## Notes

- No additional scripts or dependencies are required for basic use.
- Use the existing `SKILL.md` instructions to guide the workflow and validation.
