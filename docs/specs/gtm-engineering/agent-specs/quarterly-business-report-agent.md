---
type: area
category: revops
tags:
  - area
  - agents
  - reporting
status: active
last_updated: 2026-10-29
---

# Quarterly Business Report Agent (template)

Part of the [agent spec templates](README.md). Fill the bracketed fields for [COMPANY_NAME]. This is the written quarterly report; the per-customer meeting prep is the [QBR prep agent](qbr-agent.md).

## Purpose

Assemble the quarterly business report for a stated audience: the numbers for the quarter, what moved them, and what happens next. Set the audience and scope below before building.

## Trigger and cadence

Quarterly, after quarter close and after the data-quality checks pass. The report owner starts the run.

## Inputs

| Source | Fields (allow-listed) |
|---|---|
| Metric definitions | The approved definitions ([`metric-definitions.md`](../../../../shared_core/metrics/metric-definitions.md)) |
| Query results | The quarter's metrics from the warehouse or [CRM] reports, passed in as data |
| Prior report | Last quarter's report, for comparison and continuity |
| Audience | Who reads it, and what decision they make from it |

## Output contract

```json
{
  "audience": "",
  "headline": "",
  "metrics": [{"name": "", "value": "", "vs_prior": "", "definition_id": ""}],
  "what_moved_it": [{"text": "", "evidence": ""}],
  "risks_and_next_steps": []
}
```

Every metric value comes from a query result and carries a `definition_id`. The model writes the headline and the explanations only.

## HITL policy

The report owner reviews and signs off before distribution. Distribution is a separate, manual step. If the data-quality check fails, the run does not start.

## Evals

- Human-written reference reports for past quarters, for language and tone.
- Checks: every number matches its query result, comparisons use the same definition as last quarter, no metric appears without a definition.
- Re-run the test set after every prompt change. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md).

## Impact metric

Report owner hours per quarter, baselined before launch. Count corrections found after distribution.

## Stop rule

Pause the agent if a distributed report contained a number that did not match its source; log the incident and notify the agent owner.
