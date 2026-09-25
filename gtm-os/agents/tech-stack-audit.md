---
id: agent-tech-stack-audit
type: prompt-agent
tags: [prompt-library, revenue-operations]
last_modified: 2026-09-25
function: RevOps
purpose: Tooling Audit
priority: P1
confidence_score: 0.6
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /tech-stack-audit -- SaaS Utilization & Redundancy Inspector

**Type:** Revenue Operations

**Status: strong overlap** -- this vault already has substantial real content covering this; this note exists mainly to file the reusable prompt form itself.

## System Prompt
```
Analyze the provided list of GTM software applications. Categorize by functional layer (Data Enrichment, Engagement, Intelligence, CRM). Identify functional redundancies, estimated license wastage, integration gaps, and consolidation recommendations.
```

## Primary Use Case
Conducting tool stack audits to optimize SaaS spend and eliminate workflow overlap.

## Cross-References
[gtm-leadership](../../wiki/skills/gtm-leadership.md) . [GTM Intelligence Overview](../../wiki/competitive/GTM Intelligence Overview.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
