---
id: agent-forecast-rollup
type: prompt-agent
tags: [prompt-library, revenue-operations]
last_modified: 2026-09-25
function: RevOps
purpose: Forecasting
priority: P0
confidence_score: 0.4
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /forecast-rollup -- Multi-Rep Forecast Roll-Up Builder

**Type:** Revenue Operations

**Status: net-new, identified via external research** -- not among the 25 supplied; added after researching current GTM prompt-library practice.

## System Prompt
```
Given per-rep deal-health scores and stage-weighted pipeline across a team, build a forecast roll-up: commit/best-case/pipeline breakdown by rep and in aggregate, the top 3 risk factors named by deal, and a variance callout vs. last period's forecast.
```

## Primary Use Case
Turning individual deal health scores (see meddpicc_health_engine) into a team/org-level forecast view for sales leadership.

## Cross-References
[sales-leadership](../../wiki/skills/sales-leadership.md) . [meddpicc_health_engine](../code/scoring/meddpicc_health_engine.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
