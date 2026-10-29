---
type: area
category: revops
tags:
  - area
  - agents
  - spec-template
status: active
last_updated: 2026-10-29
---

# Agent Spec Templates

Module: `docs/specs/gtm-engineering`. Six reusable spec templates for post-sale and forecasting agents at [COMPANY_NAME]. Each follows the six parts of the [AI Workflow Standard](../../../../shared_core/ai_governance/README.md): prompt spec, output contract, data boundary, eval set, HITL policy, impact metric. Fill in the bracketed fields; every value marked `[ASSUME]` is a starting point to replace with a sourced fact.

## Executive Summary

One spec per agent, one shared shape. An agent drafts; a named person reviews before anything reaches a customer, a record or a channel. Numbers come from queries, never from the model. Each agent is judged against a baseline captured before launch and against human-written reference outputs.

## The agents

| Agent | Spec | Primary user | Cadence |
|---|---|---|---|
| Mutual Action Plan | [mutual-action-plan-agent.md](mutual-action-plan-agent.md) | Account manager (AM) | On request |
| BVA | [bva-agent.md](bva-agent.md) | AM | On request |
| QBR (builds the QBR presentation) | [qbr-agent.md](qbr-agent.md) | AM, customer success manager (CSM) | Before each customer QBR |
| Expansion (whitespace) | [expansion-whitespace-agent.md](expansion-whitespace-agent.md) | AM, CSM | Scheduled, per eligible customer |
| Quarterly business report (trigger finder) | [quarterly-business-report-agent.md](quarterly-business-report-agent.md) | Account owners | Set per org |
| Forecasting | [forecasting-agent.md](forecasting-agent.md) | Sales and finance leaders | Weekly |

## Shared template

Copy this skeleton for a new agent.

| Part | Fill in |
|---|---|
| **Purpose** | One sentence: the artifact produced and who uses it |
| **Trigger and cadence** | On request, scheduled, or event-driven; the owner of the schedule |
| **Inputs** | Source system and fields, listed by name. Only allow-listed fields reach the prompt ([`pii_guard.py`](../../../../shared_core/ai_governance/pii_guard.py)) |
| **Output contract** | Declared keys; anything else is rejected, not patched ([`llm_client.py`](../../../../shared_core/ai_governance/llm_client.py)) |
| **Eligibility rules** | Which accounts or deals are in scope, and why the rest are excluded |
| **HITL policy** | Who reviews, what they can change, what happens if the check fails (fail closed) |
| **Evals** | Reference outputs, test set, re-run rule. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md) |
| **Logging** | Errors and decisions logged where the team will find them |
| **Impact metric** | Before and after, with the baseline captured before launch |
| **Stop rule** | What pauses the agent, and who is told |

## Rules that apply to every agent

- **Draft, then review.** Nothing is sent to a customer, written to [CRM] or posted to a channel until its named reviewer accepts it.
- **Numbers from queries.** The model writes the narrative; counts, dollar amounts and dates come from a query or a [CRM] field and are passed in. Same principle as decision log #5.
- **Say where a number came from.** Every figure in an output is tagged as a [CRM] field, a customer statement or an assumption. Untagged figures are rejected.
- **Tailor to the reader.** Outputs delivered to a rep carry that rep's tone and length preferences, and channel limits (for example a message character limit) are part of the output contract.
- **Pipeline is not revenue.** Any agent that sources opportunities reports pipeline created, kept separate from bookings.
- **Earn autonomy.** Start at L0 (every item reviewed) and move up only from a logged record ([earned autonomy](../../../../shared_core/ai_governance/earned-autonomy.md)).
