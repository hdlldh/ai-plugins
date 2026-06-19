---
name: youtube-video-script-generator
description: Generate a long-form YouTube video script plus related short-video scripts with an orchestrator/writer/reviewer loop and up to three refinement rounds.
---

# YouTube Video Script Generator

## Overview

Generate a regular YouTube video script that builds long-term viewer connection, plus a set of short promotional scripts designed to attract viewers to the regular video. The skill uses three agents: orchestrator, writer, and reviewer.

## Workflow

1. Orchestrator interacts with the user to gather requirements:
   - main topic and audience
   - regular video goal, tone, and connection strategy
   - short-video purpose, hooks, and relationship to the regular video
   - any brand, format, or voice constraints
2. Orchestrator sends the finalized requirements to the writer.
3. Writer generates:
   - one regular video script of at least 8 minutes that prioritizes long-term connection with viewers, clear structure, and strong audience value
   - a regular video script that includes a formatted hook section titled `## **Hook (first 3–10 seconds)**` and uses one of the strong hook styles
   - a regular video script that delivers **high value**: viewers learn something genuinely useful, important, or actionable that addresses their actual needs
   - a regular video script with **high compression**: delivering a lot of useful information in very little time, staying dense but clear while avoiding fluff, repetition, and slow explanations
   - a regular video script that is **easy to understand**: using analogies, visuals (diagrams, animations, highlighting), and clear language to simplify complex concepts
   - one strong title for the regular video that is clear, curious, and benefit-driven
   - a couple of short video scripts (2-3) related to the regular video, each under 3 minutes and designed to attract viewers to watch the regular video
   - short video scripts that target the **same audience** as the regular video
   - short video scripts that **create an information gap**: providing useful insights or quick wins while leaving viewers wanting the full explanation from the regular video
   - short video scripts that **provide real value** upfront (not just ads) while making viewers curious to see the deeper content in the regular video
   - short video scripts that have a **strong hook** (within 1-2 seconds) to grab attention in a competitive short-form environment
   - short video scripts with a **clear structure**: Hook (0-3s), Value (3-25s), Curiosity Gap (25-35s), CTA (final seconds)
   - strong titles for each short video that are clear, curious, and benefit-driven
4. Writer sends the scripts and titles to reviewer.
5. Reviewer evaluates the scripts and titles against the requirements and goals:
   - regular video script length and connection-building focus
   - whether the regular video delivers high value: viewers feel they understand better, saved time, or can actually use the content
   - whether the regular video maintains high compression: dense and information-rich without fluff, long intros, repetition, or slow pacing
   - whether the regular video is easy to understand: uses analogies, visuals, and clear explanations to simplify concepts
   - whether the regular video is formatted for speech synthesis with a clear 2-second pause between major sections
   - whether short videos target the **same audience** as the regular video
   - whether short videos **create an information gap**: viewers feel "I want the full explanation" and are driven to click the long video
   - whether short videos **provide real value** upfront without feeling like ads
   - whether the **value difference is clear**: short videos show 1 idea while the regular video covers 5-20 related ideas
   - whether short videos have a **strong hook** within the first 1-2 seconds
   - whether short videos follow a **clear structure**: Hook, Value, Curiosity Gap, CTA
   - short videos under 3 minutes and clearly tied to the regular video
   - alignment with tone, audience, and brand constraints
   - clarity, production-readiness, and engagement
   - whether the shorts motivate viewers to watch the regular video
6. Reviewer returns a pass/fail decision plus specific improvement notes.
7. Orchestrator inspects the reviewer results. If the requirements are fulfilled, end the workflow. If not, orchestrator sends the reviewer feedback to writer and repeats the writer/reviewer loop, up to three total iterations.
8. If the third iteration still does not satisfy the requirements, report the final reviewer summary and ask the user whether to continue refinement or accept the best available draft.

## High Value Content

High-value educational content ensures viewers feel: *"I understand this better,"* *"This saved me time,"* or *"I can actually use this."*

**Low-value example:**
A 10-minute Python video spends 7 minutes explaining basics people already know ("Python is a programming language. Many developers use Python..."). Technically correct but the viewer gains almost nothing.

**High-value example:**
A Python video teaches the 3 most common beginner mistakes in 3 minutes: parameters vs arguments confusion, mutable default parameters, and indentation errors. The viewer thinks: *"Wow, this directly solved problems I actually have."* That's value.

## High Compression

High compression means delivering a lot of useful information in very little time—dense but clear, without fluff.

- **Low compression** = fluffy (long intro, repetition, filler, slow pacing)
- **High compression** = dense but clear (no wasted words, fast-paced, information-rich)

**Low compression example:**
A 10-minute video contains only 2 minutes of useful information:
- Long intro
- Repetition of points
- Too much filler
- Slow explanations

Viewers feel: *"Get to the point."*

**High compression example:**
A 10-minute video is packed with useful information throughout. Every minute counts. Key points are explained clearly and concisely without redundancy or slow pacing.

Viewers feel: *"Every minute was worth it."*

## Easy to Understand

Good educational creators simplify complex concepts using:

**Analogies:**
Compare unfamiliar concepts to everyday experiences.
- Example: *"Parameters are like placeholders in a recipe."*
- Example: *"A database index is like a book's table of contents."*

**Visuals:**
Use supporting materials to clarify meaning:
- Diagram (flow charts, infographics, concept maps)
- Animation (process visualization, step-by-step breakdowns)
- Highlighting (emphasize key points, contrast, comparisons)

Clear explanations combined with analogies and visuals make dense, valuable information accessible to all viewers, regardless of prior knowledge.

## Short-Form Video Guidelines

### **1. Same Audience**

Shorts and long-form videos must target the same viewers.

If long videos are about SAT prep, AP CSP, or Python, then Shorts should be about SAT tips, AP concepts, or Python quick lessons. If the audience doesn't match, Shorts views won't convert into long-video views.

### **2. Create an Information Gap**

Shorts should make viewers want more.
- Give them a useful insight, key idea, or quick win
- But don't explain everything
- Viewers should feel: *"That was helpful… I want the full explanation."*

That curiosity drives clicks to the long videos.

### **3. Provide Real Value**

Shorts should not feel like ads.

**Bad:** "Watch my full video for more."
**Good:** Teach something useful first (one SAT trick, one Python concept, one AI tool usage).

Viewers are more likely to trust and follow creators who provide value upfront.

### **4. Long Videos Must Go Much Deeper**

Long videos should offer significantly more value than Shorts.

**Rule:** Short = 1 idea | Long video = 5–20 ideas

**Examples:**
- Short: 1 SAT tip | Long: Full SAT strategy
- Short: 1 Python mistake | Long: Beginner mistakes guide

The value gap must be obvious.

### **5. Strong Hook**

Shorts are extremely competitive. You have 1–2 seconds to grab attention.

**Weak hook:** "Today I'm going to explain Python…"
**Strong hook:** "90% of Python beginners make this mistake." or "This SAT mistake costs students 50 points."

A strong hook increases retention and watch time.

### **6. Clear Short-Form Structure**

A good Short usually follows:

- **Hook (0–3s):** Grab attention
- **Value (3–25s):** Deliver useful content
- **Curiosity Gap (25–35s):** Create interest for the full explanation
- **CTA (Final seconds):** Guide viewers to the long video

**Template Example:**
- Hook: "Most students lose easy SAT points here."
- Value: "They rush inference questions."
- Curiosity Gap: "But that's only one of five major mistakes."
- CTA: "Full breakdown on my channel."

## Validation

- Confirm the regular video script is at least 8 minutes long.
- Confirm each short video script is under 3 minutes.
- Confirm the short scripts are clearly related to the regular video and designed to draw viewers to it.
- Confirm the regular video and short videos each include a strong title that is clear, curious, and benefit-driven.
- Confirm the reviewer provides an explicit evaluation of whether the output meets the requirements.
- Confirm the workflow loops only when needed and stops after a pass or after three iterations.
