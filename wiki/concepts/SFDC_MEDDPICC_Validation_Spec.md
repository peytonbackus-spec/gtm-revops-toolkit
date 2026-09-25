---
id: sfdc-meddpicc-validation-spec
type: spec
tags: [wiki/concepts, revops-engineering, meddpicc, salesforce]
last_modified: 2026-09-25
confidence_score: 0.6
---

# Salesforce MEDDPICC Custom Fields & Validation Rules Spec

## Custom Fields (Opportunity Object)
| Field Label | API Name | Data Type | Description |
| :--- | :--- | :--- | :--- |
| Quantified ROI | `Quantified_ROI__c` | Checkbox | Verified financial ROI business case |
| Economic Buyer Contacted | `Economic_Buyer_Contacted__c` | Checkbox | Direct contact established with budget holder |
| Technical Decision Criteria | `Technical_Evaluation_Criteria__c` | Checkbox | Technical evaluation criteria documented |
| Decision Process Documented | `Decision_Proc_Documented__c` | Checkbox | Procurement and security steps clear |
| Paper Process Stage | `Paper_Process_Stage__c` | Picklist | Values: `Not Started`, `In Legal Review`, `Procurement Approved` |
| Quantified Pain | `Quantified_Pain__c` | Checkbox | Explicit cost of doing nothing identified |
| Primary Champion | `Primary_Champion__c` | Lookup (`Contact`) | Designated champion with influence |
| Primary Competitor | `Primary_Competitor__c` | Picklist | Direct competitor or `Internal Build` |

---

## Validation Rule: Enforce MEDDPICC Before Stage 4 (Proposal/Quote)

**Rule Name:** `Enforce_MEDDPICC_At_Stage_4`
**Error Message:** "Opportunities cannot advance to Stage 4 without a verified Economic Buyer, Quantified Pain, and Primary Champion."

```apex
AND(
  IsClosed = FALSE,
  StageName >= "04 - Proposal/Quote",
  OR(
    Economic_Buyer_Contacted__c = FALSE,
    Quantified_Pain__c = FALSE,
    ISBLANK(Primary_Champion__c)
  )
)
```

## See Also
[00-Code-Index](../../gtm-os/code/00-Code-Index.md) . [meddpicc_health_engine](../../gtm-os/code/scoring/meddpicc_health_engine.md) . [account-executive](../skills/account-executive.md)
