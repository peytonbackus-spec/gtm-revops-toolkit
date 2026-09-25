---
id: agent-renewal-playbook
type: prompt-agent
tags: [prompt-library, revenue-operations]
last_modified: 2026-09-25
function: Customer Success
purpose: Renewal
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /renewal-playbook -- Proactive Renewal Motion Builder

**Type:** Revenue Operations

**Status: net-new, identified via external research** -- not among the 25 supplied; added after researching current GTM prompt-library practice.

## System Prompt
```
Given an account's usage/health data and contract timeline, build a proactive renewal playbook: T-90/T-60/T-30 day milestones, required stakeholder touchpoints, upsell/downsell decision points, and an escalation trigger if health score drops below threshold before renewal date.
```

## Primary Use Case
Distinct from reactive churn scoring (see churn_prediction_pipeline) -- this is the proactive, calendar-driven renewal motion.

## Cross-References
[account-management-customer-success](../../wiki/skills/account-management-customer-success.md) . [churn_prediction_pipeline](../code/scoring/churn_prediction_pipeline.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
