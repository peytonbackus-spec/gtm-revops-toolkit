---
id: raw-lead-bypass-debate
type: raw-source
tags: [raw-source, salesforce, lead-object, data-model]
last_modified: 2026-09-25
source_url: https://www.revopscoop.com/post/bypassing-the-lead-object
accessed: 2026-09-25
---

# RAW: "Leads & Contacts: Bypass the Lead or Keep It?" (RevOps Co-op)

Against Lead object: fragments activity/reporting across two person-object types; doesn't reflect non-linear B2B buying cycles (prospects re-engage, upsell, return as customers); obscures full account history.

For Lead object (weak case per author): historically useful for minimal-info capture before company match; author calls this "nonsense for every sales motion outside of PLG and direct-to-consumer."

Practitioner approaches: (1) marketing automation creates Contacts directly, matched by domain, skipping Lead; (2) Salesforce Flow + Apex auto-converts Leads to existing Contact/Account on match; (3) warehouse-level matching/merge logic for granular control.

Philosophy: convert Leads to Contacts whenever possible; reserve Lead object only for personal emails with no company association.
