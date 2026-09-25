---
id: agent-crm-hygiene-auto-updater
type: prompt-agent
tags: [prompt-library, revops]
function: RevOps
purpose: Data Quality
priority: P1
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /crm-hygiene-auto-updater -- CRM Hygiene & Auto-Update Agent Spec

**Function:** RevOps  
**Purpose:** Data Quality  
**Priority:** P1

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given a call/meeting transcript or activity log, extract: a summary, next steps, any opportunity stage change implied, missing required fields to flag, and tasks to create. Specify exactly which fields this is allowed to write automatically vs. which require human confirmation (protect sales-owned fields per the enrichment write-back rules already established).
```

## Why This Gap Existed
One of the highest-frequency real RevOps automation jobs (keeping CRM records current from call activity) -- was not covered by any of the 25 originally supplied.

## Cross-References
[gtm-tool-data-models](../../wiki/concepts/gtm-tool-data-models.md) . [revops-schema](revops-schema.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . index
