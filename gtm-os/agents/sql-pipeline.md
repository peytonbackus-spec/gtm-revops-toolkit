---
id: agent-sql-pipeline
type: prompt-agent
tags: [prompt-library, engineering-ai]
last_modified: 2026-09-25
function: RevOps
purpose: Reporting
priority: P1
confidence_score: 0.5
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /sql-pipeline -- Revenue Data Warehousing & SQL Query Engine

**Type:** Engineering & AI

**Status: partial overlap** -- related material already exists elsewhere in this vault; this note captures the reusable prompt form specifically.

## System Prompt
```
Write optimized SQL queries (Snowflake/BigQuery/PostgreSQL) to calculate GTM pipeline analytics. Include metrics: Customer Acquisition Cost (CAC), Lifetime Value (LTV), Pipeline Velocity, Net Retention Rate (NRR), and Cohort Churn.
```

## Primary Use Case
Extracting revenue performance metrics from analytical databases or BI platforms.

## Cross-References
[data-pipeline-analytics](../../wiki/skills/data-pipeline-analytics.md) . [revops-engineering](../../wiki/skills/revops-engineering.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
