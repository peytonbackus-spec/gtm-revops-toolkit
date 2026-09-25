---
id: agent-gtm-motion-selector
type: prompt-agent
tags: [prompt-library, gtm-strategy-leadership]
function: GTM Strategy & Leadership
purpose: Strategic Planning
priority: P1
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /gtm-motion-selector -- GTM Motion Selector (PLG vs. Sales-Led vs. Hybrid)

**Function:** GTM Strategy & Leadership  
**Purpose:** Strategic Planning  
**Priority:** P1

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given [COMPANY_NAME]'s [PRIMARY_PRODUCT_SUITE] at an [ACV_RANGE] price point, a [TARGET_BUYER_PERSONA] buying committee, and a [SALES_CYCLE_LENGTH] time-to-value, recommend a primary GTM motion (product-led, sales-led, or hybrid) with the specific triggers that would justify adding the other motion later. Name the org and tooling implications of the recommendation.
```

## Variables
Uses the tag set in [VARIABLES.md](../../VARIABLES.md).

## Why This Gap Existed
A foundational strategic decision GTM leaders make before building any of the other playbooks in this repo -- was assumed implicitly (sales-led) rather than decided explicitly anywhere.

## Cross-References
[gtm-leadership](../../wiki/skills/gtm-leadership.md) . [pricing-packaging-optimizer](pricing-packaging-optimizer.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md)
