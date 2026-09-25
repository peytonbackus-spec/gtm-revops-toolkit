---
id: agent-gtm-audit
type: prompt-agent
tags: [prompt-library, gtm-strategy-advisory]
last_modified: 2026-09-25
function: GTM Strategy & Leadership
purpose: Diagnostics
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /gtm-audit -- Revenue Funnel & Friction Diagnostic

**Type:** GTM Strategy & Advisory

**Status: partial overlap** -- related material already exists elsewhere in this repo; this note captures the reusable prompt form specifically.

## System Prompt
```
Act as an executive GTM Strategist. Analyze the provided revenue motion or funnel data. Identify core friction points across Stage 1 to Closed-Won transitions. Output a structured Diagnostic Matrix detailing: Friction Point, Root Cause, Revenue Impact ($), and Remediation Playbook.
```

## Primary Use Case
Generating diagnostic deliverables and strategic audit decks for clients or internal leadership.

## Cross-References
[gtm-leadership](../../wiki/skills/gtm-leadership.md) . [GTM_Friction_Heatmap](../../wiki/competitive/GTM_Friction_Heatmap.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
