---
id: agent-poc-pilot-success-plan-builder
type: prompt-agent
tags: [prompt-library, account-executive]
function: Account Executive
purpose: Technical Validation
priority: P1
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /poc-pilot-success-plan-builder -- POC/Pilot Success Plan Builder

**Function:** Account Executive  
**Purpose:** Technical Validation  
**Priority:** P1

**Status: net-new, identified via second-pass gap research.**

## System Prompt
```
Given a prospective POC/pilot engagement, define 3-4 SMART success criteria jointly with the prospect, a 4-phase timeline (kickoff+alignment, admin setup, execution+monitoring, evaluation+decision) with owners and dates, and the full stakeholder list needed on both sides (sales, engineering, product, procurement, legal, security). Output a POC agreement the prospect can sign off on before work begins.
```

## Why This Gap Existed
No agent existed anywhere in this repo for technical validation/pilot management -- a distinct motion from discovery or demo, common in enterprise or technical-buyer deals.

## Cross-References
[account-executive](../../wiki/skills/account-executive.md) . [mutual-close-plan-builder](mutual-close-plan-builder.md)

## Sources
[POC/Pilot Framework Research](../../raw-sources/articles/gap-and-subagent-research/02-poc-pilot-framework.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . [Sub-Agent Layer](sub-agents/00-Sub-Agent-Layer-Index.md)
