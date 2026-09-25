---
id: code-meddpicc-health-engine
type: code-index
tags: [code, revops-engineering, meddpicc]
last_modified: 2026-09-25
---

# MEDDPICC Health & Risk Calculation Engine

Companion note for `meddpicc_health_engine.py` -- exists so `[meddpicc_health_engine](meddpicc_health_engine.md)` wikilinks resolve in Obsidian (bare links only match `.md` notes) and so the real implementation is one click from every agent/skill that describes its logic.

**Real file:** `gtm-os/code/scoring/meddpicc_health_engine.py`

Calculates a 0-100 deal health score from the `MEDDPICCHealthEngine.WEIGHTS` dict: `economic_buyer_engaged` 25, `metrics_verified` 15, `paper_process_stage` 15, `quantified_pain` 15, `decision_criteria_documented` 10, `decision_process_clear` 10, `champion_identified` 10. Referenced by [the Deal Health Scorer sub-agent](../../agents/sub-agents/deal-health-scorer.md), [forecast-rollup](../../agents/forecast-rollup.md), [lead-scoring](../../agents/lead-scoring.md), [account-executive](../../../wiki/skills/account-executive.md), and [sales-leadership](../../../wiki/skills/sales-leadership.md) -- if the weights in the code ever change, update this note's summary too so the docs don't drift from the real logic.

## See Also
[00-Code-Index](../00-Code-Index.md) . [SFDC_MEDDPICC_Validation_Spec](../../../wiki/concepts/SFDC_MEDDPICC_Validation_Spec.md) . [deal-health-scorer](../../agents/sub-agents/deal-health-scorer.md)
