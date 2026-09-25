---
id: subagent-deal-health-scorer
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: Deal Health Scorer

**Slug:** `deal-health-scorer`

## Task (single-purpose, reusable)
Apply the meddpicc_health_engine.py weighting (economic buyer 25pts, quantified ROI 15, paper process 15, quantified pain 15, decision criteria 10, decision process 10, champion 10) to the given opportunity data and return a 0-100 score plus the specific unmet criteria.

## Called By (parent agents that invoke this sub-agent)
[forecast-rollup](../forecast-rollup.md) . [mutual-close-plan-builder](../mutual-close-plan-builder.md) . [account-brief-generator](../account-brief-generator.md) . [win-loss-analyzer](../win-loss-analyzer.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
4 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 4.

## See Also
[Sub-Agent Layer](00-Sub-Agent-Layer-Index.md) . [00-Prompt-Library-Index](../00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../../wiki/concepts/full-org-agent-taxonomy.md)
