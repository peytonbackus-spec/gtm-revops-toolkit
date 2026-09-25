"""
Unified RevOps Toolkit Integration Test Suite
Executes unit testing and validation across all revenue engineering modules.
"""

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scoring.meddpicc_health_engine import MEDDPICCHealthEngine
from scoring.churn_prediction_pipeline import AccountChurnPredictor
from revops_tech_debt_tracker import RevOpsTechDebtAuditor

# NOTE: lead-to-account matching is intentionally NOT tested here. This
# repo's real L2A matcher lives at core/engine/l2a_matcher.py (a more
# mature implementation than any gtm-os/code/ stand-in would be -- see
# gtm-os/code/00-Code-Index.md's redirect note) and is already covered
# by tests/test_l2a_matcher.py.

class TestRevOpsToolkit(unittest.TestCase):
    def test_meddpicc_health_engine(self):
        sample_opp = {
            'Quantified_ROI__c': True,
            'Economic_Buyer_Contacted__c': True,
            'Quantified_Pain__c': True,
            'Primary_Champion__c': '0038000000iD34AAAS',
            'Paper_Process_Stage__c': 'Procurement Approved'
        }
        res = MEDDPICCHealthEngine.calculate_deal_health(sample_opp)
        self.assertGreaterEqual(res['health_score'], 80)
        self.assertTrue(res['qualified_for_stage_4'])

    def test_churn_prediction_critical(self):
        telemetry = {
            'account_id': '001XYZ',
            'wau_change_pct': -40.0,
            'has_active_exec_sponsor': False,
            'open_escalated_tickets': 2
        }
        predictor = AccountChurnPredictor(telemetry)
        res = predictor.predict_risk()
        self.assertEqual(res['risk_level'], 'CRITICAL')

    def test_tech_debt_auditor(self):
        schema = [{'api_name': 'Unused_Field__c', 'population_rate_pct': 0.0, 'days_since_last_modified': 200}]
        auditor = RevOpsTechDebtAuditor(schema)
        res = auditor.run_schema_audit()
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['severity'], 'HIGH')

if __name__ == '__main__':
    unittest.main()
