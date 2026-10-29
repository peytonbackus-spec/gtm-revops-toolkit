---
type: area
category: revops
tags:
  - area
  - proof-of-work
  - estimates
status: active
last_updated: 2026-10-29
---

# Proof of Work

Module: `docs`. What I built and ran at a B2B SaaS company and an acquired company, with sizes and results. **Every figure on this page is my own estimate ("est."), not an audited or system-reported number.** The templates in this repo are generic and run on synthetic data; they are not the code or data from those roles.

## Executive Summary

I built six AI agents for post-sale and forecasting work at a B2B SaaS company: Mutual Action Plan, BVA, QBR, Expansion (whitespace), quarterly business report and Forecasting. Used by about 21 people (est.), they cut QBR prep from 3+ hours to about 45 minutes in total (est.) and sourced about 10 expansion opportunities a quarter (est.). That figure is **pipeline, not revenue**. Reusable versions of the specs are in the [agent spec templates](specs/gtm-engineering/agent-specs/README.md).

## Agent suite (a B2B SaaS company)

### Who used it (est.)

| Group | Users (est.) |
|---|---|
| Account managers (AMs) | 8 |
| Customer success managers (CSMs) | 5 |
| Install owners | 8 |
| **Total** | **21** |

Each user worked about 10 to 15 accounts (est.).

### Coverage and runs

- The Expansion agent covered about 85% of customers (est.). The rest were under 6 months old or had renewed in the last 60 days.
- Runs (est.):

| Agent | Runs (est.) |
|---|---|
| Mutual Action Plan | about 50 |
| BVA | about 75 |
| QBR | about 20 |
| Forecasting | about 16, roughly weekly |

### Results (est.)

| Measure | Before | After | Notes |
|---|---|---|---|
| QBR prep time | 3+ hours (est.) | About 15 minutes of agent work plus human review, about 45 minutes total (est.) | Per QBR |
| QBRs prepped | n/a | About 20 per quarter (est.) | |
| Expansion opportunities sourced | n/a | About 10 per quarter (est.), $15K to $75K each, about $55K average (est.) | **Pipeline, not revenue** |
| At-risk flags | n/a | 3 to 4 per quarter (est.) | 2 of the 3 resolved accounts were saved and renewed (est.) |
| Forecast accuracy | n/a | Within +/-5% of quarter-end and year-end bookings (est.) | Weekly forecast |

### Forecasting agent

Weekly forecast across 12 models (est.): opportunity stages, verticals, revenue segments and historicals, each for new business and for all existing business, and drillable to the accounts behind it. Template: [forecasting agent](specs/gtm-engineering/agent-specs/forecasting-agent.md).

### How the agents were evaluated

- Human-written reference outputs for language and tone.
- A test set re-run after every prompt change.
- Human review before delivery.
- Errors and decisions logged.
- Reworks made from real use, such as a Slack character limit and send frequency.
- Output tailored to each rep's communication style.

Checklist version: [Agent Eval Checklist](playbooks/Agent_Eval_Checklist.md).

## Engineering

AI-assisted Python and TypeScript API code. I run it, deploy it and own it.

- A deployed FastAPI intent-signal system with real traffic.
- A Salesforce product-qualified-lead (PQL) ingestor.
- A MEDDPICC deal-health and churn pipeline.
- An enrichment waterfall rules engine.

Reference implementations in this repo, on synthetic data: [`sfdc_pql_ingestor.py`](../prototypes/sfdc_pql_ingestor.py), [`meddpicc_health_engine.py`](../prototypes/meddpicc_health_engine.py), [`churn_prediction_pipeline.py`](../prototypes/churn_prediction_pipeline.py), [`rules_engine.py`](../gtm_engineer/enrichment/rules_engine.py) with [`waterfall_rules.yaml`](../config/waterfall_rules.yaml), and the [enrichment webhook](../gtm_engineer/integrations/webhook.py).

## Outbound deliverability

SPF, DKIM and DMARC with alignment, secondary domains, inbox warmup, monitoring of bounce, spam and reply rates, and per-mailbox sending limits. Reference: the Gmail and Yahoo bulk-sender rules (authentication, one-click unsubscribe honored within 2 days, spam rate under 0.3% and ideally under 0.1%). Checklist: [Outbound Deliverability Checklist](playbooks/Outbound_Deliverability_Checklist.md).

## CRM data migration (an acquired company)

Migrated HubSpot data to Salesforce: leads, contacts, accounts and opportunities.

| Object | Volume (est.) |
|---|---|
| Accounts | About 25K to 35K |
| Contacts | About 90K |
| Opportunities | About 1,000 |

Leads stayed in HubSpot unless new events occurred. I mapped the fields and handled dedupe and cleanup, working with the director of RevOps. Checklist: [CRM Migration Checklist](playbooks/CRM_Migration_Checklist.md).

## Reading this page

- All figures are my own estimates (est.), not audited.
- Expansion figures are pipeline created. They are not bookings or revenue.
- Before-and-after comparisons are estimates, not controlled tests.
