---
id: skill-account-executive
type: skill
tags: [skill, account-executive, meddpicc, closing]
last_modified: 2026-09-25
---

# Account Executive

## Skill Tree
- MEDDPICC deal qualification & progression gating — see [SFDC_MEDDPICC_Validation_Spec](../concepts/SFDC_MEDDPICC_Validation_Spec.md) and [GTM_OS_Architecture_Spec](../concepts/GTM_OS_Architecture_Spec.md)
- Multi-threading / economic buyer engagement
- Discovery, quantifying pain, and ROI business-case building
- Forecast accuracy & commit discipline

## Prompt Templates
**Discovery call prep**, mapped to the [meddpicc_health_engine](../../gtm-os/code/scoring/meddpicc_health_engine.md) weighting:
```
Given this account/opportunity context, draft discovery questions to
surface: (1) quantified pain, (2) economic buyer identity + access plan,
(3) technical decision criteria, (4) decision process/paper process
stage, (5) champion status. Weight questions toward whichever field is
currently unverified.
```

## Execution Checklist — Deal Health Review
Mirrors [meddpicc_health_engine](../../gtm-os/code/scoring/meddpicc_health_engine.md)'s scoring weights:
- [ ] Quantified ROI business case documented (15 pts)
- [ ] Economic buyer directly contacted (25 pts — highest weight, prioritize first)
- [ ] Technical decision criteria documented (10 pts)
- [ ] Decision process / procurement steps clear (10 pts)
- [ ] Paper process stage current (Not Started / In Legal Review / Procurement Approved) (15 pts)
- [ ] Quantified pain confirmed (15 pts)
- [ ] Champion identified (10 pts)
- [ ] Deal health score recalculated after each material stage change

## See Also
[_Skill_Matrix_Hub](_Skill_Matrix_Hub.md) · index · [sales-leadership](sales-leadership.md)
