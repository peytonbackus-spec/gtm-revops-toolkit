---
id: agent-escalation-runbook
type: prompt-agent
tags: [prompt-library, customer-success]
function: Customer Success
purpose: Risk Management
priority: P1
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /escalation-runbook -- Customer Escalation Runbook Builder

**Function:** Customer Success  
**Purpose:** Risk Management  
**Priority:** P1

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given an at-risk account signal (churn flag, executive sponsor departure, repeated escalations), build an escalation runbook: who gets notified internally and in what order, the customer-facing communication script, a save-play decision tree, and the executive-sponsor-to-executive-sponsor escalation path if needed.
```

## Why This Gap Existed
Distinct from health scoring (which detects risk) -- this is the response runbook for what happens once risk is detected.

## Cross-References
[account-management-customer-success](../../wiki/skills/account-management-customer-success.md) . [churn_prediction_pipeline](../code/scoring/churn_prediction_pipeline.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . index
