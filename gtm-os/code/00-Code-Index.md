---
id: code-index
type: manifest
tags: [hub, code, revops-engineering]
status: active
last_modified: 2026-09-25
confidence_score: 1.0
---

# GTM OS -- Code Index

Real Python implementations backing several agents/skills' described logic. Moved here from the legacy `30_Resources/Code/` PARA location (2026-09-25 vault audit) so they live inside the same tracked architecture as the docs that reference them, instead of sitting orphaned outside it.

## Executive Architecture & Specs
- [GTM_OS_Architecture_Spec](../../wiki/concepts/GTM_OS_Architecture_Spec.md) -- high-level system topology and API data flow
- [SFDC_MEDDPICC_Validation_Spec](../../wiki/concepts/SFDC_MEDDPICC_Validation_Spec.md) -- Salesforce validation rules and deal-stage gating metrics
- [SFDC_Tech_Debt_Audit](../../wiki/concepts/SFDC_Tech_Debt_Audit.md) -- point-in-time schema tech-debt snapshot (see [revops_tech_debt_tracker](revops_tech_debt_tracker.md) for the generator)

## Core Code Base
- **PQL Ingestion Engine:** [sfdc_pql_ingestor](sfdc_pql_ingestor.md) -- `gtm-os/code/sfdc_pql_ingestor.py`
- **Lead-to-Account Matcher:** [l2a_matching_engine](../../core/engine/l2a_matcher.py) -- `gtm-os/code/orchestrators/l2a_matching_engine.py`
- **MEDDPICC Health Scorer:** [meddpicc_health_engine](scoring/meddpicc_health_engine.md) -- `gtm-os/code/scoring/meddpicc_health_engine.py`
- **Account Churn Predictor:** [churn_prediction_pipeline](scoring/churn_prediction_pipeline.md) -- `gtm-os/code/scoring/churn_prediction_pipeline.py`
- **Schema Tech Debt Tracker:** [revops_tech_debt_tracker](revops_tech_debt_tracker.md) -- `gtm-os/code/revops_tech_debt_tracker.py`
- **Automated Test Suite:** [test_revops_suite](tests/test_revops_suite.md) -- `gtm-os/code/tests/test_revops_suite.py`

**Not yet built:** an attribution SQL engine (`w_shaped_attribution.sql`) was referenced in the pre-consolidation manifest but was never actually written -- flagging here rather than re-promising it silently. Pipeline Attribution Setup is the open project tracking that work.

## Integration Quality Control
All scripts here are syntax-checked and unit-tested via GitHub Actions on every push (`.github/workflows/lint_and_test.yml`).

## See Also
index . [gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md)
