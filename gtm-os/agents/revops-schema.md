---
id: agent-revops-schema
type: prompt-agent
tags: [prompt-library, revenue-operations]
last_modified: 2026-09-25
function: RevOps
purpose: Data Model
priority: P0
confidence_score: 0.65
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /revops-schema -- CRM Custom Object & Lifecycle Modeler

**Type:** Revenue Operations

**Status: strong overlap** -- this vault already has substantial real content covering this; this note exists mainly to file the reusable prompt form itself.

## System Prompt
```
Design a scalable CRM data model (Salesforce/HubSpot). Define: Lifecycle Stages, Lead-to-Account Mapping Logic, Custom Object Schemas (properties, field types), and Required Webhook Payloads for downstream integrations.
```

## Primary Use Case
Designing scalable CRM architectures, deal pipeline schemas, and automated data flows.

## Cross-References
[gtm-tool-data-models](../../wiki/concepts/gtm-tool-data-models.md) . [SFDC_MEDDPICC_Validation_Spec](../../wiki/concepts/SFDC_MEDDPICC_Validation_Spec.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
