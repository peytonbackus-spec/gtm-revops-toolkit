---
id: agent-qbr-builder
type: prompt-agent
tags: [prompt-library, customer-success]
function: Customer Success
purpose: Adoption & Retention
priority: P1
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /qbr-builder -- Quarterly Business Review Builder

**Function:** Customer Success  
**Purpose:** Adoption & Retention  
**Priority:** P1

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given an account's usage data, support history, and stated goals, build a QBR agenda and deck outline: wins since last review, usage trend vs. goals, open risks (tie to churn/health flags), and a forward-looking expansion or renewal ask. Lead with the account's own stated priorities, not a generic template.
```

## Why This Gap Existed
Promotes the inline QBR prompt already sketched in the AM/CS skill note into its own standalone reusable agent.

## Cross-References
[account-management-customer-success](../../wiki/skills/account-management-customer-success.md) . [churn_prediction_pipeline](../code/scoring/churn_prediction_pipeline.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md)
