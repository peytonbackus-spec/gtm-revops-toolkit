---
type: area
category: revops
tags:
  - area
  - agents
  - qbr
status: active
last_updated: 2026-10-29
---

# QBR Agent (template)

Part of the [agent spec templates](README.md). Fill the bracketed fields for [COMPANY_NAME].

## Purpose

Build the presentation for one customer quarterly business review (QBR): what changed this quarter, outcomes delivered, open issues, risks and the asks for the meeting. The agent assembles the draft deck; the account owner reviews and edits it before the meeting.

## Trigger and cadence

Scheduled ahead of each customer QBR date held in [CRM], or on request from the account owner.

## Inputs

| Source | Fields (allow-listed) |
|---|---|
| [CRM] account | Products, contract and renewal dates, health score and its drivers, owner, open opportunities |
| Support | Ticket counts and themes, aggregated |
| Usage | Aggregated trends (percent change, utilization), never record-level customer data |
| [CONVERSATION_INTELLIGENCE] | Summaries of the quarter's calls, redacted |
| Previous QBR | The last presentation and the actions agreed |
| Deck template | The team's standard QBR slide structure and branding |

## Output contract

```json
{
  "slides": [{"section": "summary|outcomes|issues|risks|last_actions|asks|expansion",
              "title": "", "bullets": [], "sources": []}],
  "speaker_notes": []
}
```

The slides follow the deck template's section order. Every outcome and risk bullet carries a source.

## HITL policy

The account owner reviews and edits the presentation before the meeting. Risks flagged as at-risk go to the named owner for a decision; the agent does not change a health score or an opportunity. If the review step cannot run, nothing is delivered.

## Evals

- Human-written reference QBR presentations for accounts across health bands (healthy, quiet, at risk).
- Checks: every outcome and risk carries a source; last quarter's open actions are all accounted for; no claim about usage without an aggregated trend behind it.
- Re-run the test set after every prompt change. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md).

## Impact metric

Prep time per QBR, as agent time plus human review time, against a baseline measured before launch. Also QBRs prepped per quarter and at-risk flags raised and resolved.

## Stop rule

Pause the agent if a delivered presentation states an unsourced outcome or risk; log it and notify the agent owner.
