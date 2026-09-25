---
id: agent-customer-onboarding-playbook-builder
type: prompt-agent
tags: [prompt-library, customer-success]
function: Customer Success
purpose: Onboarding
priority: P0
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /customer-onboarding-playbook-builder -- Customer Onboarding Playbook Builder

**Function:** Customer Success  
**Purpose:** Onboarding  
**Priority:** P0

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Design a customer onboarding playbook from contract signature to first value. Break into task modules with clear objectives per phase, assign ownership (CS/Implementation/Customer), define milestone tracking checkpoints, and branch the plan by segment (high-touch enterprise vs. low-touch/self-serve).
```

## Why This Gap Existed
The single biggest gap found: no onboarding agent existed anywhere in this repo despite it being the foundational CS motion (contract-to-first-value directly drives retention).

## Cross-References
[account-management-customer-success](../../wiki/skills/account-management-customer-success.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md)
