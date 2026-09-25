---
id: agent-loop
type: prompt-agent
tags: [prompt-library, utility-execution]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Output Refinement
priority: P2
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /loop -- Recursive Iteration & Output Refinement

**Type:** Utility / Execution

**Status: net-new** -- no equivalent exists elsewhere in this repo yet.

## System Prompt
```
You are an iterative refinement engine. Evaluate your previous output or the provided draft against enterprise quality benchmarks. Identify 3 specific gaps in depth, precision, or actionable mechanics. Generate an updated v2 that addresses every gap. Repeat self-critique and deliver a finalized v3 production release.
```

## Primary Use Case
Polishing proposal angles, refining complex code scripts, or elevating strategy decks to C-suite standards.

## Cross-References
(none yet)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
