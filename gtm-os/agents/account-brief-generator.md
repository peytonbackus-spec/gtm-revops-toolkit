---
id: agent-account-brief-generator
type: prompt-agent
tags: [prompt-library, account-executive]
function: Account Executive
purpose: Pre-Call Preparation
priority: P0
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /account-brief-generator -- Pre-Call Account Brief Compiler

**Function:** Account Executive  
**Purpose:** Pre-Call Preparation  
**Priority:** P0

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given an account, compile a pre-call brief combining: recent interaction history, product usage signals (if available), open support tickets, buying committee map (who's involved, role, engagement level), and relevant competitive intelligence. Output as a 1-page brief a rep can read in under 2 minutes before the call.
```

## Why This Gap Existed
The highest-frequency AE prep task -- directly grounded in real-world RevOps automation practice (account-brief generation is one of the most commonly automated AE-facing jobs).

## Cross-References
[account-executive](../../wiki/skills/account-executive.md) . [GTM Intelligence Overview](../../wiki/competitive/GTM Intelligence Overview.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . index
