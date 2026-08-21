import json
import sys

def score_deal(deal_data):
    weights = {
        "metrics": 15,
        "economic_buyer": 20,
        "decision_criteria": 10,
        "decision_process": 10,
        "paper_process": 10,
        "identify_pain": 15,
        "champion": 15,
        "competitors": 5
    }
    
    total_score = 0
    missing = []
    
    for key, weight in weights.items():
        if deal_data.get(key):
            total_score += weight
        else:
            missing.append(key.replace('_', ' ').title())
            
    return total_score, missing

if __name__ == "__main__":
    sample_deal = {
        "metrics": True,
        "economic_buyer": False,
        "decision_criteria": True,
        "decision_process": True,
        "paper_process": False,
        "identify_pain": True,
        "champion": True,
        "competitors": False
    }
    
    score, missing_fields = score_deal(sample_deal)
    print(f"[✓] MEDDPICC Deal Score: {score}/100")
    print(f"[!] Gaps Identified: {', '.join(missing_fields)}")
