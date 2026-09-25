---
id: raw-outreach-salesforce-config
type: raw-source
tags: [raw-source, outreach, salesforce, integration]
last_modified: 2026-09-25
source_url: https://support.outreach.io/hc/en-us/articles/13056326486427-Salesforce-Configuration-for-Outreach-End-to-End-Guide-Best-Practice
accessed: 2026-09-25
---

# RAW: Outreach "Salesforce Configuration for Outreach: End to End Guide"

Object mapping table (bi-directional unless noted):
- Lead -> Prospect (bi-directional)
- Contact -> Prospect (bi-directional)
- Account -> Account (bi-directional)
- Opportunity -> Opportunity (bi-directional, configurable)
- User -> User (inbound only, typically)
- Event -> Meeting (outbound only)
- Task -> Activity/Task (outbound only)

Sync mechanics:
- Inbound polling every 10 min default; up to 2,000 new/updated SFDC records per API call, 200 records/import call after
- Outbound pushes near-instant (30-45 sec)
- "Updates In" vs "Updates Out" field mapping checkboxes; net-new records always get all mapped fields regardless of checkbox state

Pitfalls:
- Duplicate activities if Advanced Task Mapping (ATM) not configured correctly - disable standard activity sync options on Lead/Contact when using ATM
- Incomplete one-to-one field mappings break sync
- Integration user needs API + field-level security on all mapped fields

Best practices: keep API usage under 70-80% of daily limit; enable sync merge/delete cleanup; prefer Advanced Task Mapping over Standard for granular reporting
