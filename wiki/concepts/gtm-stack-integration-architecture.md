---
id: gtm-stack-integration-architecture
type: concept
tags: [concept, architecture, integration, orchestration]
last_modified: 2026-09-25
---

# GTM Stack Integration & Orchestration Architecture

## The 6-Layer GTM Stack (how GTM engineers actually organize it today)
| Layer | Function | Example Tools |
|---|---|---|
| CRM Core | System of record | Salesforce, HubSpot, Attio |
| Data & Identity | Search, enrichment, verification | Clay, ZoomInfo, Cleanlist |
| Intelligence | Signal-based triggers | 6sense, Bombora, UserGems |
| Execution | Sequencing/outreach | Outreach, Salesloft, Apollo |
| Orchestration | Scheduling & agents | n8n, Zapier, MCP servers |
| Analytics | Attribution/reporting | Gong, Dreamdata, warehouse |

Larger orgs add a **warehouse layer** (Snowflake/BigQuery) + dbt + reverse ETL (Hightouch/Census) underneath all of this — see [Warehouse-Centric Architecture](../../raw-sources/articles/gtm-integration-research/07-lead-bypass-debate.md) below.

## Two Workflow Patterns
1. **Deterministic (REST API)** — scheduled, repeatable: fixed filters, enrichment steps, syncs. Example: Monday 6am outbound list build with verified-contact routing to sequencer.
2. **Agentic (MCP)** — interactive/adaptive: a model reviews returned data and adjusts filters or enrichment scope mid-run.

**The practical handoff GTM engineers use:** design and debug interactively via an agent/copilot first, then convert the settled workflow into a scheduled deterministic API job for production. This mirrors this repo's own `gtm-os/` layer intent — [GTM_OS_Architecture_Spec](GTM_OS_Architecture_Spec.md) describes exactly this kind of orchestration but only [pipeline-risk-contract](../../gtm-os/contracts/pipeline-risk-contract.md) exists as an actual declared contract so far.

## The Core Connection Pattern (signal → CRM)
Enrichment wired into CRM → playbook listens for a trigger (funding announcement, form submission, engagement signal) → filter against ICP → multi-provider enrichment **waterfall** (not single-source) → score the account → queue into sequencer or reverse-ETL back to CRM.

This is the same shape as [l2a_matching_engine](../../core/engine/l2a_matcher.py) (domain + fuzzy company matching) feeding into [meddpicc_health_engine](../../gtm-os/code/scoring/meddpicc_health_engine.md) scoring already built in this repo.

## Reverse ETL vs. iPaaS — the decision that actually matters
| | iPaaS (n8n, Zapier, Workato, Tray) | Reverse ETL (Hightouch, Census) |
|---|---|---|
| Source of truth | Lives in the SaaS apps | Lives in the warehouse |
| Model | App-to-app, point-to-point | Warehouse → many destinations at once |
| Best for | Simple workflows, no heavy transform | Non-trivial transform, self-service audience building, multiple simultaneous destinations |
| Risk if misused | N/A | Using it as your *primary ingestion pipeline* — it's built for activation, not ingestion |

**Rule of thumb:** if your source of truth is scattered across SaaS tools, use iPaaS. If you've already centralized in a warehouse, use reverse ETL to fan data back out.

## System-of-Record Rules That Actually Prevent Chaos
- Pick **one authoritative source per domain** and enforce a one-way sync out of it:
  - Subscription truth: billing tool → warehouse → CRM (consumer only)
  - Opportunity truth: CRM → warehouse → BI tools (consumer only)
  - Product events: event collector → warehouse (master) → CRM/lifecycle tools (consumers)
- **Never build two-way CRM↔CRM syncs** — guaranteed field thrashing and duplicate proliferation (this is the same lesson as the tool-integration warning in [account-executive](../skills/account-executive.md)'s underlying spec work).
- Treat schemas like APIs: versioned, tested, documented, with stakeholders notified on change ("data contracts").

## Rollout Sequence (for building this from scratch)
1. **Weeks 1-4:** canonical data model, identity graph, declare systems-of-record
2. **Weeks 5-8:** source ingestion, dbt models, first reverse-ETL activation
3. **Weeks 9-12:** scoring/health models go live (PQL, churn — this repo already has [churn_prediction_pipeline](../../gtm-os/code/scoring/churn_prediction_pipeline.md) and [meddpicc_health_engine](../../gtm-os/code/scoring/meddpicc_health_engine.md) built for this stage)
4. **Weeks 13-16:** enablement, operating rituals (weekly pipeline review, monthly QBR on shared metrics)

## Sources
[Cleanlist: GTM Engineering](../../raw-sources/articles/gtm-integration-research/01-cleanlist-gtm-engineering.md) . [Outreach<->Salesforce Config](../../raw-sources/articles/gtm-integration-research/02-outreach-salesforce-config.md) . [Orum Integrations](../../raw-sources/articles/gtm-integration-research/03-orum-integrations.md) . [AriseGTM Blueprint](../../raw-sources/articles/gtm-integration-research/04-arisegtm-blueprint.md) . [Clay/HubSpot/Salesforce Mapping](../../raw-sources/articles/gtm-integration-research/05-clay-hubspot-salesforce-mapping.md) . [Reverse ETL vs. iPaaS](../../raw-sources/articles/gtm-integration-research/06-reverse-etl-vs-ipaas.md) . [Lead-Bypass Debate](../../raw-sources/articles/gtm-integration-research/07-lead-bypass-debate.md)

## See Also
[gtm-tool-data-models](gtm-tool-data-models.md) · [revops-engineering](../skills/revops-engineering.md) · [GTM_OS_Architecture_Spec](GTM_OS_Architecture_Spec.md) · [_Skill_Matrix_Hub](../skills/_Skill_Matrix_Hub.md) · index

## Sources
- [What is GTM Engineering? (Cleanlist)](https://www.cleanlist.ai/blog/2026-05-22-what-is-gtm-engineering)
- [Salesforce Configuration for Outreach (Outreach support docs)](https://support.outreach.io/hc/en-us/articles/13056326486427-Salesforce-Configuration-for-Outreach-End-to-End-Guide-Best-Practice)
- [Orum Platform Integrations](https://www.orum.com/platform/integrations)
- [Blueprint for a Unified GTM Tech Stack (Arise GTM)](https://arisegtm.com/blog/gtm-tech-stack-blueprint)
- [Clay + HubSpot/Salesforce Sync & Field Mapping Guide](https://intelligentresourcing.co/blogs/clay-hubspot-salesforce-sync-and-field-mapping-guide)
- [Hightouch vs Census (DataToolIndex)](https://datatoolindex.com/compare/hightouch-vs-census/)
- Raw capture: [01-cleanlist-gtm-engineering](../../raw-sources/articles/gtm-integration-research/01-cleanlist-gtm-engineering.md) · [02-outreach-salesforce-config](../../raw-sources/articles/gtm-integration-research/02-outreach-salesforce-config.md) · [03-orum-integrations](../../raw-sources/articles/gtm-integration-research/03-orum-integrations.md) · [04-arisegtm-blueprint](../../raw-sources/articles/gtm-integration-research/04-arisegtm-blueprint.md) · [05-clay-hubspot-salesforce-mapping](../../raw-sources/articles/gtm-integration-research/05-clay-hubspot-salesforce-mapping.md) · [06-reverse-etl-vs-ipaas](../../raw-sources/articles/gtm-integration-research/06-reverse-etl-vs-ipaas.md)
