"""
RevOps Tech Debt Tracker & Schema Auditor
Analyzes Opportunity object custom fields for low population rates and stale schema debt.
"""

import json

class RevOpsTechDebtAuditor:
    def __init__(self, metadata_sample):
        self.metadata = metadata_sample

    def run_schema_audit(self, population_threshold=5.0):
        debt_report = []
        
        for field in self.metadata:
            api_name = field.get('api_name')
            pop_rate = field.get('population_rate_pct', 0.0)
            last_modified_days = field.get('days_since_last_modified', 0)
            
            # Identify tech debt candidates (population < 5% or unupdated for 180+ days)
            if pop_rate < population_threshold or last_modified_days > 180:
                severity = 'HIGH' if pop_rate == 0.0 else 'MEDIUM'
                action = 'SAFE TO DEPRECATE' if pop_rate == 0.0 else 'REVIEW WITH SALES OPS'
                
                debt_report.append({
                    'api_name': api_name,
                    'population_rate': f'{pop_rate}%',
                    'days_inactive': last_modified_days,
                    'severity': severity,
                    'recommended_action': action
                })
                
        return debt_report

if __name__ == '__main__':
    mock_sfdc_schema = [
        {'api_name': 'Legacy_Lead_Source_Detail__c', 'population_rate_pct': 0.0, 'days_since_last_modified': 240},
        {'api_name': 'Quantified_ROI__c', 'population_rate_pct': 82.4, 'days_since_last_modified': 12},
        {'api_name': 'Temp_Competitor_Notes__c', 'population_rate_pct': 1.2, 'days_since_last_modified': 195},
        {'api_name': 'Economic_Buyer_Contacted__c', 'population_rate_pct': 74.1, 'days_since_last_modified': 3}
    ]

    auditor = RevOpsTechDebtAuditor(mock_sfdc_schema)
    audit_results = auditor.run_schema_audit()

    print('=== RevOps Tech Debt Audit Results ===')
    print(json.dumps(audit_results, indent=2))
