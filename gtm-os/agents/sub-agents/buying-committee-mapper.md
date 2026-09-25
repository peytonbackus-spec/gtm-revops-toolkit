---
id: subagent-buying-committee-mapper
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
confidence_score: 0.4
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: Buying Committee Mapper

**Slug:** `buying-committee-mapper`

## Task (single-purpose, reusable)
Given known contacts on an account, map each to a MEDDPICC role (economic buyer, champion, technical evaluator, blocker) with engagement-level evidence, and flag any critical role with no identified contact yet.

## Called By (parent agents that invoke this sub-agent)
[account-brief-generator](../account-brief-generator.md) . [mutual-close-plan-builder](../mutual-close-plan-builder.md) . [demo-narrative-architect](../demo-narrative-architect.md) . [poc-pilot-success-plan-builder](../poc-pilot-success-plan-builder.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
4 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 4.

## See Also
[Sub-Agent Layer](00-Sub-Agent-Layer-Index.md) . [00-Prompt-Library-Index](../00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../../wiki/concepts/full-org-agent-taxonomy.md)
