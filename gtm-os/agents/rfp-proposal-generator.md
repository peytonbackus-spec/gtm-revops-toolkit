---
id: agent-rfp-proposal-generator
type: prompt-agent
tags: [prompt-library, account-executive]
function: Account Executive
purpose: Deal Support
priority: P1
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /rfp-proposal-generator -- RFP & Proposal First-Draft Generator

**Function:** Account Executive  
**Purpose:** Deal Support  
**Priority:** P1

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given an RFP or proposal request, pull relevant content from past responses, pre-approved legal/security language, and internal knowledge base material to produce a structured first draft. Flag any question requiring legal, security, or executive sign-off before it can be answered as drafted.
```

## Why This Gap Existed
Turns a multi-day RFP response into a first-draft-plus-review cycle instead of writing from scratch each time.

## Cross-References
[account-executive](../../wiki/skills/account-executive.md) . [positioning-framework](positioning-framework.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . index
