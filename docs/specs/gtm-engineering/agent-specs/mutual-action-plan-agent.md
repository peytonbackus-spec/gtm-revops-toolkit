---
type: area
category: revops
tags:
  - area
  - agents
  - mutual-action-plan
status: active
last_updated: 2026-10-29
---

# Mutual Action Plan Agent (template)

Part of the [agent spec templates](README.md). Fill the bracketed fields for [COMPANY_NAME].

## Purpose

Draft a mutual action plan (MAP) for an open opportunity: a dated list of steps that the buyer and [COMPANY_NAME] each commit to, from now to go-live or signature.

## Trigger and cadence

On request from the opportunity owner. Optionally also when an opportunity reaches a stage the team chooses (`[ASSUME]` stage name).

## Inputs

| Source | Fields (allow-listed) |
|---|---|
| [CRM] opportunity | Stage, close date, products, owner |
| [CRM] contacts | Role on the deal, buying-committee role |
| [CONVERSATION_INTELLIGENCE] | Call summary text, redacted, for the latest calls |
| Milestone template | The team's standard steps and typical durations |

## Output contract

```json
{
  "milestones": [
    {"name": "", "owner_side": "buyer|seller", "owner_role": "", "due_date": "", "depends_on": []}
  ],
  "open_questions": [],
  "assumptions": []
}
```

Every date is either a [CRM] date, a buyer statement, or listed under `assumptions`. A plan with no assumptions listed and no source for a date is rejected.

## HITL policy

The opportunity owner reviews and edits before anything is shared with the buyer. The agent never contacts the buyer. If the review step cannot run, the plan waits (fail closed).

## Evals

- Human-written reference plans for a handful of representative deals (stage, length, number of stakeholders).
- Checks: dates run forward, no milestone depends on a later one, each milestone has an owner on one side, assumptions are listed.
- Re-run the test set after every prompt change. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md).

## Impact metric

Owner prep time per plan and share of plans sent to buyers, baselined before launch.

## Stop rule

Pause the agent if reviewers reject or heavily rewrite more than a set share of plans in a week (`[ASSUME]` threshold); notify the agent owner.
