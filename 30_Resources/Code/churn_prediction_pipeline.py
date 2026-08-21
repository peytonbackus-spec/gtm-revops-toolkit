"""
---
type: resource
category: code
tags:
  - resource
  - python
  - churn
  - machine-learning
status: active
last_updated: 2026-08-21
---
"""

import os
from typing import Dict, Any

def calculate_churn_risk_score(account_telemetry: Dict[str, Any]) -> Dict[str, Any]:
    """Calculates churn risk probability based on usage drop-offs and ticket escalation signals."""
    
    score = 0
    risk_factors = []

    license_utilization = account_telemetry.get("license_utilization", 1.0)
    monthly_usage_change = account_telemetry.get("monthly_usage_change_pct", 0.0)
    p1_tickets_open = account_telemetry.get("open_p1_tickets", 0)
    days_since_last_csm_touch = account_telemetry.get("days_since_last_csm_touch", 0)

    if license_utilization < 0.50:
        score += 35
        risk_factors.append("Low license utilization (<50%)")
        
    if monthly_usage_change < -0.25:
        score += 30
        risk_factors.append("Product usage dropped >25% MoM")

    if p1_tickets_open > 0:
        score += 20
        risk_factors.append("Active unresolved P1 support ticket")

    if days_since_last_csm_touch > 60:
        score += 15
        risk_factors.append("No CSM engagement for 60+ days")

    risk_level = "Low"
    if score >= 60:
        risk_level = "High"
    elif score >= 30:
        risk_level = "Medium"

    return {
        "account_id": account_telemetry.get("account_id"),
        "churn_risk_score": score,
        "risk_level": risk_level,
        "risk_factors": risk_factors
    }
