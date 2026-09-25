---
id: agent-inbound-playbook
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: Inbound SDR
purpose: Response SLA
priority: P0
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /inbound-playbook -- Speed-to-Lead Triage & SLA Structurer

**Type:** Sales Development

**Status: partial overlap** -- related material already exists elsewhere in this vault; this note captures the reusable prompt form specifically.

## System Prompt
```
Create an Inbound Lead Triage Playbook. Define SLA response times by lead score, automated routing rules, instant booking workflows (Chili Piper/HubSpot), and multi-touch follow-up cadence for missed inbound demos.
```

## Primary Use Case
Optimizing conversion rates on inbound demo requests and contact forms.

## Cross-References
[lead-scoring](lead-scoring.md) . [Chili Piper](../../wiki/competitive/tools/Chili Piper.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
