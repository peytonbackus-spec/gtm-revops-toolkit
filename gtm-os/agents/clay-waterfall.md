---
id: agent-clay-waterfall
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: RevOps
purpose: Data Enrichment
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /clay-waterfall -- Data Enrichment & Scraping Strategy

**Type:** Sales Development

**Status: strong overlap** -- this repo already has substantial real content covering this; this note exists mainly to file the reusable prompt form itself.

## System Prompt
```
Design a Clay multi-vendor waterfall enrichment logic for target accounts and contacts. Define: Primary/Secondary enrichment providers (e.g., Apollo -> ZoomInfo -> Findymail), AI prompting logic for web scraping, and fallback conditional rules.
```

## Primary Use Case
Engineering automated outbound data enrichment pipelines inside Clay or Python.

## Cross-References
[gtm-tool-data-models](../../wiki/concepts/gtm-tool-data-models.md) . [Clay](../../wiki/competitive/tools/Clay.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
