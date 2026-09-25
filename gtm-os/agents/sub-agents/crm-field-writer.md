---
id: subagent-crm-field-writer
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
confidence_score: 0.4
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: CRM Field Writer (Protected-Field Aware)

**Slug:** `crm-field-writer`

## Task (single-purpose, reusable)
Given a proposed CRM field write, check it against the protected-field list (lead status, opportunity stage, lifecycle stage, and any manually-edited-flagged field) before allowing the write. Route protected-field changes to human confirmation instead of auto-applying.

## Called By (parent agents that invoke this sub-agent)
[crm-hygiene-auto-updater](../crm-hygiene-auto-updater.md) . [inbound-lead-qualifier](../inbound-lead-qualifier.md) . [clay-waterfall](../clay-waterfall.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
3 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 3.

## See Also
[Sub-Agent Layer](00-Sub-Agent-Layer-Index.md) . [00-Prompt-Library-Index](../00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../../wiki/concepts/full-org-agent-taxonomy.md)
