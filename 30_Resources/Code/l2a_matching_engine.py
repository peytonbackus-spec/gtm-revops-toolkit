"""
---
type: resource
category: code
tags:
  - resource
  - python
  - sfdc
  - l2a
status: active
last_updated: 2026-08-21
---
"""

import os
import re
from typing import Optional, Dict

def extract_domain(email: str) -> Optional[str]:
    """Extracts normalized domain from email, ignoring generic providers."""
    ignored_domains = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"}
    match = re.search(r"@[\w\.-]+\.\w+", email.lower())
    if not match:
        return None
    domain = match.group(0).replace("@", "")
    return None if domain in ignored_domains else domain

def match_lead_to_account(lead_email: str, account_database: list[Dict]) -> Optional[str]:
    """Matches an incoming lead email domain against SFDC Account domains."""
    domain = extract_domain(lead_email)
    if not domain:
        return None  # Route to generic Lead Queue
        
    for account in account_database:
        acc_domain = account.get("domain", "").lower()
        acc_website = account.get("website", "").lower()
        if domain in acc_domain or domain in acc_website:
            return account["id"]  # Match found -> Convert Lead to Contact under Account ID
            
    return None  # No match -> Create SFDC Unassigned Lead
