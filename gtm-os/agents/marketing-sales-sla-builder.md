---
id: agent-marketing-sales-sla-builder
type: prompt-agent
tags: [prompt-library, gtm-strategy-leadership]
function: GTM Strategy & Leadership
purpose: Cross-Functional Alignment
priority: P1
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /marketing-sales-sla-builder -- Marketing-to-Sales SLA & Handoff Builder

**Function:** GTM Strategy & Leadership  
**Purpose:** Cross-Functional Alignment  
**Priority:** P1

**Status: net-new, identified via second-pass gap research.**

## System Prompt
```
Given the current lead volume and sales capacity, define a marketing-to-sales SLA: MQL definition and scoring threshold, marketing's commitment (volume/quality by segment), sales' commitment (response time by lead tier), the escalation path when either side misses its commitment, and the shared dashboard both teams review weekly.
```

## Why This Gap Existed
This entire vault is sales/RevOps-focused with no marketing-alignment agent -- the marketing-sales handoff is one of the most common sources of revenue leakage in B2B orgs and was entirely uncovered.

## Cross-References
[lead-scoring](lead-scoring.md) . [inbound-lead-qualifier](inbound-lead-qualifier.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . [Sub-Agent Layer](sub-agents/00-Sub-Agent-Layer-Index.md) . index
