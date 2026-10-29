---
type: area
category: revops
tags:
  - area
  - agents
  - forecasting
status: active
last_updated: 2026-10-29
---

# Forecasting Agent (template)

Part of the [agent spec templates](README.md). Fill the bracketed fields for [COMPANY_NAME]. Cadence and accuracy measurement follow [`forecast-cadence.md`](../../../../gtm_strategy_ops/forecasting/forecast-cadence.md) and [`forecast_accuracy.py`](../../../../gtm_strategy_ops/forecasting/forecast_accuracy.py).

## Purpose

Produce the weekly forecast across a set of models, covering new business and all existing business, with drill-down from each model to the accounts and opportunities behind it.

## Trigger and cadence

Weekly, on a fixed day before the forecast call. Re-run on request after a material change.

## Model set

Build one model per view. Cover all four dimensions; the exact list is the team's choice.

| Dimension | What each model cuts by |
|---|---|
| Opportunity stages | Pipeline by stage, with the team's stage probabilities |
| Verticals | The same forecast by vertical |
| Revenue segments | The same forecast by revenue segment |
| Historicals | Past quarters and years, for comparison and for calibrating the current ones |

Run each model for new business and for all existing business (renewals, expansion and the rest of the installed base). Every model is drillable to the opportunity or account.

## Inputs

| Source | Fields (allow-listed) |
|---|---|
| [CRM] opportunities | Stage, amount, close date, owner, segment, vertical, history |
| [CRM] accounts | Contract and renewal dates, segment, vertical |
| Closed history | Prior quarters and years of bookings |
| [FORECAST_TOOL] | Submitted calls, if used |

## Output contract

```json
{
  "as_of": "",
  "models": [
    {"id": "", "scope": "new_business|existing_business", "cut": "", "forecast": 0, "drill": []}
  ],
  "commentary": [{"model_id": "", "text": "", "evidence": ""}]
}
```

Forecast numbers are computed by code from the inputs. The model writes commentary only (decision log #5). Commentary cites the model and the rows it relies on.

## HITL policy

A sales or finance leader reviews before the forecast is shared. No forecast category or [CRM] field is changed by the agent (decision log #6). If a query fails or a model cannot be built, the report says which model is missing; it never fills the gap.

## Evals

- Human-written reference commentary for past weeks, for language and tone.
- Checks: totals reconcile across models, drill-down rows sum to the model total, commentary numbers match the model.
- Accuracy tracked over time: forecast against quarter-end and year-end bookings.
- Re-run the test set after every prompt change. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md).

## Impact metric

Forecast accuracy against quarter-end and year-end bookings, and hours spent on forecast preparation, baselined before launch.

## Stop rule

Pause the agent if totals fail to reconcile across models; notify the agent owner before the next run.
