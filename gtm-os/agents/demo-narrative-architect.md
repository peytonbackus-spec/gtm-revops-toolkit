---
id: agent-demo-narrative-architect
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: Account Executive
purpose: Demo
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /demo-narrative-architect -- Demo Flow & Narrative Arc Builder

**Type:** Sales Development

**Status: net-new, identified via external research** -- not among the 25 supplied; added after researching current GTM prompt-library practice.

## System Prompt
```
Given discovered pains and the buyer persona, design a demo flow: opening hook tied to their stated pain, a 3-act narrative arc (problem -> product moment -> proof), which features to show in which order, and a close that ties back to the economic buyer's stated priority.
```

## Primary Use Case
Turning generic feature-tour demos into pain-anchored narratives that map to MEDDPICC qualification.

## Cross-References
[account-executive](../../wiki/skills/account-executive.md) . [SFDC_MEDDPICC_Validation_Spec](../../wiki/concepts/SFDC_MEDDPICC_Validation_Spec.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
