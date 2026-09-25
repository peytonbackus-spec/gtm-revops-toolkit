---
id: subagent-source-citation-verifier
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
confidence_score: 0.4
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: Source Citation Verifier

**Slug:** `source-citation-verifier`

## Task (single-purpose, reusable)
Check every factual claim in the given draft for a cited source (URL, transcript timestamp, or CRM field change record). Flag any uncited claim rather than allowing it through silently -- mirrors the evidence_standard rule already declared in pipeline-risk-contract.yaml.

## Called By (parent agents that invoke this sub-agent)
[account-research-brief](../account-research-brief.md) . [win-loss-analyzer](../win-loss-analyzer.md) . [rfp-proposal-generator](../rfp-proposal-generator.md) . [inbound-lead-qualifier](../inbound-lead-qualifier.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
4 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 4.

## See Also
[Sub-Agent Layer](00-Sub-Agent-Layer-Index.md) . [00-Prompt-Library-Index](../00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../../wiki/concepts/full-org-agent-taxonomy.md)
