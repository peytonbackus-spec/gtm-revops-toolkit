---
id: skill-revops-engineering
type: skill
tags: [skill, revops, hubspot, salesforce, automation]
last_modified: 2026-09-25
confidence_score: 0.4
---

# RevOps Engineering

## Skill Tree
- CRM architecture: HubSpot Free (ops CRM + client proof-of-concept), Salesforce (client environments)
- Data schemas & contact/company data modeling
- Automation: n8n workflows, Clay enrichment
- Sales-engagement / customer-success integration (Outreach, Gainsight)

## Code Patterns
```python
# Rule-based contact cleaning pattern
import pandas as pd

def clean_contacts(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["email"])
    df["email"] = df["email"].str.strip().str.lower()
    df = df[df["email"].str.contains(r"^[^@]+@[^@]+\.[^@]+$", regex=True, na=False)]
    df["company_domain"] = df["email"].str.split("@").str[1]
    return df
```
```sql
SELECT stage, COUNT(*) AS deals, SUM(amount) AS pipeline_value
FROM deals
WHERE created_at >= date_trunc('quarter', current_date)
GROUP BY stage
ORDER BY pipeline_value DESC;
```

## Execution Checklist — RevOps Sprint (6-week engagement)
- [ ] Week 1: CRM/data audit
- [ ] Week 2: Enrichment + routing design (Clay + n8n)
- [ ] Week 3-4: Build & test automations in staging
- [ ] Week 5: Migrate/deploy to production CRM
- [ ] Week 6: Handoff docs + team training

## See Also
[_Skill_Matrix_Hub](_Skill_Matrix_Hub.md) · index · [gtm-stack-integration-architecture](../concepts/gtm-stack-integration-architecture.md) · [gtm-tool-data-models](../concepts/gtm-tool-data-models.md)
