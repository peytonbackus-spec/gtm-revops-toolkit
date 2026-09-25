---
id: agent-goal
type: prompt-agent
tags: [prompt-library, utility-execution]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Planning
priority: P2
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /goal -- Objective-to-Task Decomposition

**Type:** Utility / Execution

**Status: net-new** -- no equivalent exists elsewhere in this repo yet.

## System Prompt
```
Decompose the provided business, technical, or revenue objective into a strict, step-by-step terminal execution plan. Output: 1) Prerequisite dependencies, 2) Data schemas or required inputs, 3) Sequential execution steps, 4) Success validation metrics.
```

## Primary Use Case
Converting high-level strategic directives into execution roadmaps.

## Cross-References
[gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
