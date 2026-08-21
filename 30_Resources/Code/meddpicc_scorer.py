import sys

def score_sfdc_opportunity(opportunity_data):
    # Mapping MEDDPICC criteria to standard SFDC Opportunity fields/custom APEX fields
    sfdc_field_map = {
        "Quantified_ROI__c": ("Metrics", 15),
        "Economic_Buyer_Contacted__c": ("Economic Buyer", 20),
        "Technical_Evaluation_Criteria__c": ("Decision Criteria", 10),
        "Decision_Proc_Documented__c": ("Decision Process", 10),
        "Paper_Process_Stage__c": ("Paper Process", 10),
        "Quantified_Pain__c": ("Identify Pain", 15),
        "Primary_Champion__c": ("Champion", 15),
        "Primary_Competitor__c": ("Competitors", 5)
    }
    
    total_score = 0
    missing = []
    
    for sfdc_field, (label, weight) in sfdc_field_map.items():
        if opportunity_data.get(sfdc_field):
            total_score += weight
        else:
            missing.append(label)
            
    return total_score, missing

if __name__ == "__main__":
    # Sample SFDC Opportunity Record
    sample_opp = {
        "Quantified_ROI__c": True,
        "Economic_Buyer_Contacted__c": False,
        "Technical_Evaluation_Criteria__c": True,
        "Decision_Proc_Documented__c": True,
        "Paper_Process_Stage__c": None,
        "Quantified_Pain__c": True,
        "Primary_Champion__c": True,
        "Primary_Competitor__c": None
    }
    
    score, missing_fields = score_sfdc_opportunity(sample_opp)
    print(f"[✓] SFDC Opportunity MEDDPICC Score: {score}/100")
    print(f"[!] SFDC Qualification Gaps: {', '.join(missing_fields)}")
