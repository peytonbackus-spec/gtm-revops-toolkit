---
id: gtm-tool-data-models
type: concept
tags: [concept, data-model, fields, objects]
last_modified: 2026-09-25
---

# GTM Tool Data Models — Objects, Fields & Relationships

## Salesforce Core Object Model
- **Lead** — unqualified/unmatched person, not yet linked to an Account. Converts into Contact + Account (+ optionally Opportunity).
- **Contact** — a person linked to an Account.
- **Account** — the company/organization.
- **Opportunity** — a deal in progress, linked to an Account.
- **Campaign** — a marketing initiative, can link to Leads/Contacts via Campaign Members.

### The Lead-bypass debate (this matters more than it sounds)
Many practitioners now **skip the Lead object entirely** because it fragments activity/reporting across two person-object types and doesn't reflect real B2B buying cycles (accounts re-engage, upsell, and return as customers — a closed-lost Lead loses that history). Three practical approaches:
1. Marketing automation creates Contacts directly (matched by domain before creation)
2. Salesforce Flow + Apex auto-converts Leads to existing Contact/Account on match
3. Warehouse-level matching/merge logic for full control

**Working rule:** convert Leads to Contacts whenever possible; only use Lead for personal emails with no resolvable company.

## Outreach ↔ Salesforce Object Mapping
| Salesforce | Outreach | Direction |
|---|---|---|
| Lead | Prospect | Bi-directional |
| Contact | Prospect | Bi-directional |
| Account | Account | Bi-directional |
| Opportunity | Opportunity | Bi-directional (configurable) |
| Event | Meeting | Outbound only |
| Task | Activity/Task | Outbound only |

- Inbound polling: every 10 min, up to 2,000 records/call
- Outbound push: near-instant (30-45 sec)
- **Advanced Task Mapping (ATM)** required to avoid duplicate activity records — disable standard activity sync on Lead/Contact when ATM is on

## Orum (dialer) Integration Shape
Orum syncs bi-directionally with Salesforce and surfaces prospect context from Outreach/Salesloft during live calls, plus logs outcomes to Gong. Public docs are thin on field-level detail — treat vendor integration pages as directional, not authoritative; verify actual field behavior in a sandbox before building on it.

## Clay Enrichment → CRM Write-Back Pattern
Clay supports 3 sync models:
- **One-way** (Clay → CRM only) — safest when Clay owns enrichment integrity
- **Two-way** — risky at scale (field thrashing)
- **Conditional** — writes only above a confidence threshold

**6-step waterfall:** signal ingestion → multi-source conditional enrichment → dedup check against CRM → confidence gating (verified email + confirmed title) → field-level write-back → audit log.

**Rule that prevents CRM corruption:** enrichment writes to *custom* fields first (match score, enrichment status, signal confidence); sales-owned fields (lead status, opp stage, lifecycle stage) stay protected from automated overwrite. This is the same principle already encoded in [SFDC_MEDDPICC_Validation_Spec](SFDC_MEDDPICC_Validation_Spec.md)'s custom-field approach (`Quantified_ROI__c`, `Economic_Buyer_Contacted__c`, etc. — all custom fields, not overwrites of standard ones).

## Sources
[Cleanlist: GTM Engineering](../../raw-sources/articles/gtm-integration-research/01-cleanlist-gtm-engineering.md) . [Outreach<->Salesforce Config](../../raw-sources/articles/gtm-integration-research/02-outreach-salesforce-config.md) . [Orum Integrations](../../raw-sources/articles/gtm-integration-research/03-orum-integrations.md) . [AriseGTM Blueprint](../../raw-sources/articles/gtm-integration-research/04-arisegtm-blueprint.md) . [Clay/HubSpot/Salesforce Mapping](../../raw-sources/articles/gtm-integration-research/05-clay-hubspot-salesforce-mapping.md) . [Reverse ETL vs. iPaaS](../../raw-sources/articles/gtm-integration-research/06-reverse-etl-vs-ipaas.md) . [Lead-Bypass Debate](../../raw-sources/articles/gtm-integration-research/07-lead-bypass-debate.md)

## See Also
[gtm-stack-integration-architecture](gtm-stack-integration-architecture.md) · [account-executive](../skills/account-executive.md) · [revops-engineering](../skills/revops-engineering.md) · [_Skill_Matrix_Hub](../skills/_Skill_Matrix_Hub.md) · [README](../../README.md)

## Sources
- [Salesforce Configuration for Outreach](https://support.outreach.io/hc/en-us/articles/13056326486427-Salesforce-Configuration-for-Outreach-End-to-End-Guide-Best-Practice)
- [Orum Platform Integrations](https://www.orum.com/platform/integrations)
- [Clay + HubSpot/Salesforce Sync & Field Mapping Guide](https://intelligentresourcing.co/blogs/clay-hubspot-salesforce-sync-and-field-mapping-guide)
- [Leads & Contacts: Bypass the Lead or Keep It? (RevOps Co-op)](https://www.revopscoop.com/post/bypassing-the-lead-object)
- Raw capture: [02-outreach-salesforce-config](../../raw-sources/articles/gtm-integration-research/02-outreach-salesforce-config.md) · [03-orum-integrations](../../raw-sources/articles/gtm-integration-research/03-orum-integrations.md) · [05-clay-hubspot-salesforce-mapping](../../raw-sources/articles/gtm-integration-research/05-clay-hubspot-salesforce-mapping.md) · [07-lead-bypass-debate](../../raw-sources/articles/gtm-integration-research/07-lead-bypass-debate.md)
