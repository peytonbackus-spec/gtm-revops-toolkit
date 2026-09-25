---
id: agent-webhook-transformer
type: prompt-agent
tags: [prompt-library, engineering-ai]
last_modified: 2026-09-25
function: RevOps
purpose: Integration
priority: P1
confidence_score: 0.5
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /webhook-transformer -- JSON Payload Parser & Data Mapper

**Type:** Engineering & AI

**Status: partial overlap** -- related material already exists elsewhere in this vault; this note captures the reusable prompt form specifically.

## System Prompt
```
Analyze the source JSON payload and target API schema. Write a transformation mapping script (Python/JavaScript) that safely extracts, cleans, formats, and maps nested keys from the source to the destination API endpoint.
```

## Primary Use Case
Connecting disparate RevOps tools (e.g., Typeform -> Webhook -> Python -> CRM).

## Cross-References
[l2a_matching_engine](../../core/engine/l2a_matcher.py) . [gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
