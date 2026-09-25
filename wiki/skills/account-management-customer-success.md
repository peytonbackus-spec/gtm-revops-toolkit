---
id: skill-account-management-customer-success
type: skill
tags: [skill, account-management, customer-success, churn, retention]
last_modified: 2026-09-25
---

# Account Management & Customer Success

## Skill Tree
- Account health monitoring & churn risk scoring — see [churn_prediction_pipeline](../../gtm-os/code/scoring/churn_prediction_pipeline.md)
- Executive sponsor relationship management
- Expansion/upsell motion timing
- QBR cadence & escalation handling

## Prompt Templates
**QBR prep**, mapped to the churn predictor's flags:
```
Given this account's usage telemetry (WAU trend, exec sponsor status,
open escalations), draft a QBR agenda that leads with the highest-risk
flag first and includes a specific save-play or expansion angle.
```

## Execution Checklist — Account Health Review
Mirrors [churn_prediction_pipeline](../../gtm-os/code/scoring/churn_prediction_pipeline.md)'s risk flags:
- [ ] WAU change checked — flag if >20% decline over 30 days
- [ ] Executive sponsor status confirmed active
- [ ] Open escalations/support tickets reviewed and owned
- [ ] Save-play triggered if risk score drops below threshold
- [ ] Expansion opportunity assessed if account is healthy (WAU stable/growing, sponsor engaged)

## See Also
[_Skill_Matrix_Hub](_Skill_Matrix_Hub.md) · index · [revops-engineering](revops-engineering.md)
