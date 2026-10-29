---
type: area
category: revops
tags:
  - area
  - agents
  - bva
status: active
last_updated: 2026-10-29
---

# BVA Agent (template)

Part of the [agent spec templates](README.md). Fill the bracketed fields for [COMPANY_NAME]. BVA here means business value assessment (a written case for the value of [COMPANY_NAME] to one customer); use your organization's own term.

## Purpose

Draft a BVA for one customer or prospect: their stated goals and problems, their current baseline, and the expected benefit, with every number traced to a source.

## Trigger and cadence

On request from the account owner, before a value conversation, a renewal or an expansion discussion.

## Inputs

| Source | Fields (allow-listed) |
|---|---|
| [CRM] account and opportunity | Segment, products, contract dates, stated use case |
| [CONVERSATION_INTELLIGENCE] | Customer-stated goals and metrics from call summaries, redacted |
| Value model | The team's approved benefit formulas and their input definitions |
| Aggregated usage | Trends only, never record-level customer data |

## Output contract

```json
{
  "goals": [{"text": "", "source": "customer|crm"}],
  "baseline": [{"metric": "", "value": "", "source": "customer|crm|assumption"}],
  "benefit": [{"metric": "", "formula_id": "", "inputs": [], "result": "", "source": "assumption|computed"}],
  "caveats": []
}
```

The model fills text and picks formulas. Results are computed by code from the inputs, not generated.

## HITL policy

The account owner confirms every `assumption` with the customer or removes it before the document leaves the company. No BVA is shared without that confirmation.

## Evals

- Human-written reference BVAs for representative segments, written for language and tone as well as numbers.
- Checks: no figure without a source tag, formulas match the value model, no benefit stated for a metric with no baseline.
- Re-run the test set after every prompt or value-model change. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md).

## Impact metric

Owner time per BVA and share of BVAs used in a customer conversation, baselined before launch.

## Stop rule

Pause the agent if a reviewer finds an unsourced number in a delivered BVA; log it as an incident and notify the agent owner.
