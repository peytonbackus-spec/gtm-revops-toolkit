---
id: raw-clay-hubspot-salesforce-mapping
type: raw-source
tags: [raw-source, clay, hubspot, salesforce, enrichment]
last_modified: 2026-09-25
source_url: https://intelligentresourcing.co/blogs/clay-hubspot-salesforce-sync-and-field-mapping-guide
accessed: 2026-09-25
---

# RAW: "Clay + HubSpot/Salesforce: Sync & Field Mapping Guide"

3 sync models: one-way (Clay -> CRM, safest when Clay owns data integrity), two-way (risky at scale), conditional (Clay writes only above a confidence threshold).

Field mapping: enrichment writes to custom fields first (match scores, enrichment status, signal source/type/confidence); core sales-owned fields (lead status, opportunity stage, lifecycle stage) protected from automated overwrite.

6-step enrichment waterfall: (1) signal ingestion (funding/hiring event), (2) conditional multi-source enrichment, (3) dedup check against CRM, (4) confidence gating (verified email + confirmed title), (5) field-level write-back with conditional logic, (6) audit logging.

Pitfalls: overwriting CRM without verification gates; syncing before dedup; no audit trail; missing field-level protection for manually-edited records.
