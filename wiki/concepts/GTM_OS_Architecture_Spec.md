---
id: gtm-os-architecture-spec
type: spec
tags: [wiki/concepts, revops-engineering, architecture]
last_modified: 2026-09-25
---

# Enterprise GTM Operating System Architecture Spec

## 1. System Topology & Data Flow
The GTM Operating System acts as a unified revenue orchestration framework linking Product-Qualified Leads (PQLs), CRM record enrichment, MEDDPICC deal qualification, and churn risk intelligence.

```
  [ Product Telemetry / PQL ]
              │
              ▼
    ┌──────────────────┐
    │ L2A Match Engine │ ── (Domain & Fuzzy Matching)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ MEDDPICC Health  │ ── (Deal Progression Gatekeeping)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ Churn & Renewal  │ ── (Retention Health & Risk Scoring)
    └──────────────────┘
```

## 2. Core Field Mapping Schema

| Object | Field Name | API Name | Data Type | Usage |
| :--- | :--- | :--- | :--- | :--- |
| Opportunity | Quantified ROI | `Quantified_ROI__c` | Checkbox | MEDDPICC Metrics verification |
| Opportunity | Economic Buyer Contacted | `Economic_Buyer_Contacted__c` | Checkbox | MEDDPICC Economic Buyer verification |
| Opportunity | Health Score | `MEDDPICC_Health_Score__c` | Number (0-100) | Calculated deal health score |
| Account | WAU Change | `WAU_Change_30D__c` | Percent | Churn risk evaluation input |
| Account | Risk Level | `Churn_Risk_Level__c` | Picklist | Values: LOW, ELEVATED, CRITICAL |

## 3. Automation Modules

Moved from the legacy `30_Resources/Code/` PARA location into the tracked `gtm-os/code/` architecture during the 2026-09-25 audit -- see [00-Code-Index](../../gtm-os/code/00-Code-Index.md) for the authoritative, kept-current list. Current locations:

- **PQL Ingestion**: [`gtm-os/code/sfdc_pql_ingestor.py`](../../gtm-os/code/sfdc_pql_ingestor.py)
- **Lead-to-Account Matching**: [`core/engine/l2a_matcher.py`](../../core/engine/l2a_matcher.py)
- **MEDDPICC Risk Scoring**: [`gtm-os/code/scoring/meddpicc_health_engine.py`](../../gtm-os/code/scoring/meddpicc_health_engine.py)
- **Churn Prediction**: [`gtm-os/code/scoring/churn_prediction_pipeline.py`](../../gtm-os/code/scoring/churn_prediction_pipeline.py)
- **Tech Debt Audit**: [`gtm-os/code/revops_tech_debt_tracker.py`](../../gtm-os/code/revops_tech_debt_tracker.py)
- **Attribution Engine**: not yet built (`w_shaped_attribution.sql` was referenced in the pre-consolidation manifest but never actually written -- see [00-Code-Index](../../gtm-os/code/00-Code-Index.md)'s note on this)

## See Also
[00-Code-Index](../../gtm-os/code/00-Code-Index.md) . [full-org-agent-taxonomy](full-org-agent-taxonomy.md) . [gtm-stack-integration-architecture](gtm-stack-integration-architecture.md)
