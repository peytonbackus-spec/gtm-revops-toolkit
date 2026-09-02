"""
Pipeline Health & Deal-Risk Scoring Engine
Algorithmic account and deal evaluation to surface high-conversion pipeline and improve forecasting accuracy.
"""

def calculate_deal_risk_score(engagement_score: float, days_in_stage: int, multithread_count: int) -> dict:
    """
    Evaluates deal risk based on activity velocity, stakeholder depth, and historical stage duration.
    """
    risk_factors = []
    base_score = 100.0

    if days_in_stage > 30:
        base_score -= 25.0
        risk_factors.append("Stale Stage Duration (>30 Days)")

    if multithread_count < 3:
        base_score -= 20.0
        risk_factors.append("Single-Threaded Opportunity (<3 Persona Contacts)")

    if engagement_score < 0.4:
        base_score -= 30.0
        risk_factors.append("Low Account Engagement Velocity")

    risk_level = "LOW"
    if base_score < 50:
        risk_level = "HIGH"
    elif base_score < 75:
        risk_level = "MEDIUM"

    return {
        "deal_health_score": max(base_score, 0.0),
        "risk_level": risk_level,
        "risk_factors": risk_factors
    }
