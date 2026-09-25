---
id: agent-partner-channel-enablement-brief
type: prompt-agent
tags: [prompt-library, partner-channel]
function: Partner & Channel
purpose: Enablement
priority: P2
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /partner-channel-enablement-brief -- Partner & Channel Enablement Brief Builder

**Function:** Partner & Channel  
**Purpose:** Enablement  
**Priority:** P2

**Status: net-new, identified via second-pass gap research.**

## System Prompt
```
Given a partner/reseller relationship, build an enablement brief: co-sell motion definition (who leads, who supports), deal registration rules to prevent channel conflict, a one-page partner pitch aligned to direct-sales positioning, and the specific data/CRM fields needed to track partner-sourced pipeline separately.
```

## Why This Gap Existed
Partner/Channel was a completely absent function across all prior work -- worth flagging even though it may be lower priority until Peyton's consulting firm has partner relationships to manage.

## Cross-References
[positioning-framework](positioning-framework.md) . [revops-schema](revops-schema.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . [Sub-Agent Layer](sub-agents/00-Sub-Agent-Layer-Index.md) . index
