---
id: agent-attribution-model
type: prompt-agent
tags: [prompt-library, revenue-operations]
last_modified: 2026-09-25
function: RevOps
purpose: Reporting
priority: P1
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /attribution-model -- Multi-Touch Revenue Attribution Architect

**Type:** Revenue Operations

**Status: confirmed gap** -- the corresponding code folder (`30_Resources/Code/attribution/`) exists but is empty. This prompt captures the spec to build against.

## System Prompt
```
Design a multi-touch revenue attribution model (First-Touch, Lead Creation, Opportunity Creation, W-Shaped) for the described marketing and sales motions. Define required UTM naming conventions, CRM field capture, and pipeline reporting rules.
```

## Primary Use Case
Measuring pipeline generation efficiency and channel ROI across complex tech stacks.

## Cross-References
[data-pipeline-analytics](../../wiki/skills/data-pipeline-analytics.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
