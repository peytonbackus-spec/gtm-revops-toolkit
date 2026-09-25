---
id: agent-positioning-framework
type: prompt-agent
tags: [prompt-library, gtm-strategy-advisory]
last_modified: 2026-09-25
function: GTM Strategy & Leadership
purpose: Messaging
priority: P1
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /positioning-framework -- Messaging & Value Prop Architect

**Type:** GTM Strategy & Advisory

**Status: partial overlap** -- related material already exists elsewhere in this repo; this note captures the reusable prompt form specifically.

## System Prompt
```
Construct a B2B positioning matrix for [COMPANY_NAME]'s [PRIMARY_PRODUCT_SUITE], sold to [TARGET_BUYER_PERSONA] on a [SALES_CYCLE_LENGTH] cycle. Define: ICP (Ideal Customer Profile), Buyer Personas, Core Pain Points, Value Drivers, Differentiating Moats (including any [PRIMARY_PARTNER_ECOSYSTEM] advantage), and a 3-tier Messaging Hierarchy (Elevator Pitch, Feature-to-Value Mapping, Objection Counter-Narratives).
```

## Variables
Uses the tag set in [VARIABLES.md](../../VARIABLES.md).

## Primary Use Case
Building core messaging frameworks and value propositions for new product launches or GTM campaigns.

## Cross-References
[GTM_Proposal_Angles](../../wiki/competitive/GTM_Proposal_Angles.md) . [Proposal Diagnostic Angles](../../wiki/competitive/Proposal Diagnostic Angles.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
