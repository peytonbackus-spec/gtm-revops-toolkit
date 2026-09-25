---
type: dashboard
tags:
  - wiki/competitive
  - gtm/dashboard
id: gtm-intelligence-overview
last_modified: 2026-09-25
confidence_score: 0.5
migrated_from: obsidian-orphaned-vault
---


# 📊 GTM Tools Market Intelligence Master Index

```dataview
TABLE 
  category AS "Category",
  total_reviews_analyzed AS "Reviews Sampled"
FROM #gtm/intelligence
SORT category ASC, tool ASC
```

**Static fallback (in case Dataview is disabled or the tag query breaks silently -- this table found a real bug: the query above had its code fence backslash-escaped and was never actually rendering until the 2026-09-25 audit fixed it):**

[6sense](tools/6sense.md) . [ActiveCampaign](tools/ActiveCampaign.md) . [Aloware](tools/Aloware.md) . Apollo

[Avoma](tools/Avoma.md) . [Chili Piper](tools/Chili Piper.md) . [Clay](tools/Clay.md) . [Clearbit](tools/Clearbit.md)

[Cognism](tools/Cognism.md) . Customer . [Demandbase](tools/Demandbase.md) . [Gong](tools/Gong.md)

[HubSpot Marketing Hub](tools/HubSpot Marketing Hub.md) . [HubSpot](tools/HubSpot.md) . [Lusha](tools/Lusha.md) . [Marketo](tools/Marketo.md)

[Nooks](tools/Nooks.md) . [Orum](tools/Orum.md) . [Outreach](tools/Outreach.md) . [Pardot](tools/Pardot.md)

[PhoneBurner](tools/PhoneBurner.md) . [Pipedrive](tools/Pipedrive.md) . [RB2B](tools/RB2B.md) . [Salesforce](tools/Salesforce.md)

[Salesloft](tools/Salesloft.md) . [Zoho CRM](tools/Zoho CRM.md) . [ZoomInfo](tools/ZoomInfo.md)
