"""
Lead-to-Account (L2A) Matching Engine
Matches incoming lead webhooks against existing Salesforce Accounts using
exact domain matching and normalized fuzzy company name scoring.
"""

import re
from difflib import SequenceMatcher

class LeadToAccountMatcher:
    def __init__(self, existing_accounts):
        self.accounts = existing_accounts

    @staticmethod
    def normalize_company_name(name):
        if not name:
            return ""
        name = name.lower()
        # Remove common corporate suffixes
        suffixes = [r'\binc\b', r'\bcorp\b', r'\bcorporation\b', r'\bllc\b', r'\bltd\b', r'\bco\b']
        for suffix in suffixes:
            name = re.sub(suffix, '', name)
        return re.sub(r'[^a-z0-9]', '', name).strip()

    def match_lead(self, lead_payload):
        lead_domain = lead_payload.get('email', '').split('@')[-1].lower()
        lead_company = lead_payload.get('company', '')
        normalized_lead_company = self.normalize_company_name(lead_company)

        # Step 1: Exact Domain Matching
        for acc in self.accounts:
            if acc.get('domain') and acc['domain'].lower() == lead_domain:
                return {'matched': True, 'match_type': 'EXACT_DOMAIN', 'account_id': acc['id'], 'confidence': 1.0}

        # Step 2: Fuzzy Company Name Matching
        best_match = None
        highest_score = 0.0

        for acc in self.accounts:
            norm_acc_name = self.normalize_company_name(acc.get('name', ''))
            score = SequenceMatcher(None, normalized_lead_company, norm_acc_name).ratio()

            if score > highest_score:
                highest_score = score
                best_match = acc['id']

        if highest_score >= 0.85:
            return {'matched': True, 'match_type': 'FUZZY_NAME', 'account_id': best_match, 'confidence': round(highest_score, 2)}

        return {'matched': False, 'match_type': 'NONE', 'account_id': None, 'confidence': 0.0}

if __name__ == '__main__':
    mock_sfdc_accounts = [
        {'id': '0018000000ABC11', 'name': 'Acme Corporation, Inc.', 'domain': 'acme.com'},
        {'id': '0018000000XYZ22', 'name': 'Stark Industries LLC', 'domain': 'stark.io'}
    ]

    matcher = LeadToAccountMatcher(mock_sfdc_accounts)

    test_lead = {'email': 'jane.doe@acmecorp.com', 'company': 'Acme Corp'}
    result = matcher.match_lead(test_lead)

    print(f"[*] Lead Match Result: {result}")
