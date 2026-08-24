---
type: manifest
status: active
tags: [gtm, revops, architecture, obsidian]
---
# GTM Engine & RevOps Vault Manifest

## 📌 Executive Architecture & Specs
- [[GTM_OS_Architecture_Spec]]: High-level system topology and API data flow.
- [[SFDC_MEDDPICC_Validation_Spec]]: Salesforce validation rules and deal stage gating metrics.

## ⚡ Core Code Base
- **PQL Ingestion Engine**: `30_Resources/Code/sfdc_pql_ingestor.py`
- **Lead-to-Account Matcher**: `30_Resources/Code/orchestrators/l2a_matching_engine.py`
- **MEDDPICC Health Scorer**: `30_Resources/Code/scoring/meddpicc_health_engine.py`
- **Account Churn Predictor**: `30_Resources/Code/scoring/churn_prediction_pipeline.py`
- **Schema Tech Debt Tracker**: `30_Resources/Code/revops_tech_debt_tracker.py`
- **Attribution SQL Engine**: `30_Resources/Code/attribution/w_shaped_attribution.sql`
- **Automated Test Suite**: `30_Resources/Code/tests/test_revops_suite.py`

## 🧪 Integration Quality Control
All scripts in this vault are validated via GitHub Actions CI pipeline on commit.
