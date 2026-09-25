---
id: agent-expansion-upsell-play-builder
type: prompt-agent
tags: [prompt-library, customer-success]
function: Customer Success
purpose: Expansion
priority: P1
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /expansion-upsell-play-builder -- Expansion & Upsell Play Builder

**Function:** Customer Success  
**Purpose:** Expansion  
**Priority:** P1

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given a healthy account's usage patterns and org structure, identify the most likely expansion vector (seat growth, tier upgrade, adjacent product) and build a specific upsell play: the trigger evidence, who to approach, the value narrative, and the ask.
```

## Why This Gap Existed
CS playbook frameworks explicitly separate Adoption/Renewal from Expansion as its own lifecycle stage -- this fills that gap.

## Cross-References
[account-management-customer-success](../../wiki/skills/account-management-customer-success.md) . [qbr-builder](qbr-builder.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md)
