---
id: agent-board-investor-narrative-builder
type: prompt-agent
tags: [prompt-library, gtm-strategy-leadership]
function: GTM Strategy & Leadership
purpose: Executive Reporting
priority: P2
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /board-investor-narrative-builder -- Board & Investor Revenue Narrative Builder

**Function:** GTM Strategy & Leadership  
**Purpose:** Executive Reporting  
**Priority:** P2

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given the current forecast roll-up, pipeline health, and key wins/losses, build a one-page board or investor narrative: the headline number, the 2-3 things driving or threatening it, and what leadership is doing about each. Avoid dashboard-dump formatting -- this is a narrative, not a data export.
```

## Why This Gap Existed
Sales-leadership.md already covers internal forecast roll-ups; this is the external-facing narrative layer that was missing.

## Cross-References
[sales-leadership](../../wiki/skills/sales-leadership.md) . [forecast-rollup](forecast-rollup.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . index
