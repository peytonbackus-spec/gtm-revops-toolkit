---
id: code-revops-tech-debt-tracker
type: code-index
tags: [code, revops-engineering, schema-governance]
last_modified: 2026-09-25
---

# RevOps Schema Tech Debt & Metadata Governance Auditor

Companion note for `revops_tech_debt_tracker.py` -- gives the script a markdown page so other notes can link to it with a real relative link instead of a bare filename.

**Real file:** `gtm-os/code/revops_tech_debt_tracker.py`

`RevOpsTechDebtAuditor` takes Salesforce schema/field-utilization telemetry and flags fields for deprecation by fill rate and inactivity. Produces the kind of output captured as a point-in-time snapshot in [SFDC_Tech_Debt_Audit](../../wiki/concepts/SFDC_Tech_Debt_Audit.md).

## See Also
[00-Code-Index](00-Code-Index.md) . [SFDC_Tech_Debt_Audit](../../wiki/concepts/SFDC_Tech_Debt_Audit.md)
