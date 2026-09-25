---
id: skill-data-pipeline-analytics
type: skill
tags: [skill, data, sql, python, analytics]
last_modified: 2026-09-25
---

# Data & Pipeline Analytics

## Skill Tree
- SQL for pipeline/funnel reporting
- Python for data cleaning & schema work
- Dashboarding

## Code Patterns
```python
def usable(df):      # dedupe, normalize, validate formats
    ...
def valuable(df):    # enrich, flag missing critical fields
    ...
def scalable(df):    # parameterize rules, log rejects for review
    ...
```

## Execution Checklist — Data/Contact Audit
- [ ] Dedupe pass (email/domain normalization)
- [ ] Missing/invalid field rate reported
- [ ] "What's missing" section written
- [ ] Scalability notes: what breaks at 10x the row count

## See Also
[_Skill_Matrix_Hub](_Skill_Matrix_Hub.md) · [README](../../README.md)
