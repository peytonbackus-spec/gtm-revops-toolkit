# 🎯 GTM Operations Center

---

## ⚡ Active Signals (Last 7 Days)
```dataview
TABLE
  company AS "Company",
  signal_type AS "Trigger",
  impact_score AS "Impact",
  source AS "Source"
FROM "Signals"
WHERE type = "intent_signal"
SORT impact_score DESC
```

---

## 📥 Inbound Pipeline & SLA
```dataview
TABLE
  company AS "Company",
  contact_name AS "Contact",
  lead_score AS "Score",
  assigned_rep AS "Assigned Rep"
FROM "Inbound"
WHERE type = "inbound_lead"
SORT lead_score DESC
```

---

## 🛡️ Recent Pipeline Hygiene Audits
```dataview
TABLE
  audit_date AS "Audit Date",
  total_deals_reviewed AS "Deals Reviewed",
  deals_at_risk AS "Deals At Risk"
FROM "Audits"
WHERE type = "pipeline_hygiene_audit"
SORT audit_date DESC
```
