---
id: agent-mutual-close-plan-builder
type: prompt-agent
tags: [prompt-library, account-executive]
function: Account Executive
purpose: Negotiation & Closing
priority: P0
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /mutual-close-plan-builder -- Mutual Close Plan Architect

**Function:** Account Executive  
**Purpose:** Negotiation & Closing  
**Priority:** P0

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given the current deal stage and known stakeholders, build a mutual close plan: defined milestones with named owners and deadlines on both buyer and seller sides, a mapping of the buyer's internal decision/approval process (procurement, legal, security), identified risks with mitigation for each, and a documented buy-in step confirming both sides agree to the timeline.
```

## Why This Gap Existed
Closes the biggest gap in the original 25: negotiation/closing had no dedicated agent. Grounded in the co-created 'shared timeline' model that replaces guessed close dates with owned ones.

## Cross-References
[account-executive](../../wiki/skills/account-executive.md) . [SFDC_MEDDPICC_Validation_Spec](../../wiki/concepts/SFDC_MEDDPICC_Validation_Spec.md)

## Sources
[Mutual Close Plan Research](../../raw-sources/articles/full-org-agent-research/02-mutual-close-plan.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md)
