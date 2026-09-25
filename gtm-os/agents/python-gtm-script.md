---
id: agent-python-gtm-script
type: prompt-agent
tags: [prompt-library, engineering-ai]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Automation Build
priority: P1
confidence_score: 0.6
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /python-gtm-script -- Revenue Operations & API Automation Builder

**Type:** Engineering & AI

**Status: strong overlap** -- this vault already has substantial real content covering this; this note exists mainly to file the reusable prompt form itself.

## System Prompt
```
Write a production-grade Python script for GTM automation. Include: Robust error handling, rate limiting for external APIs (e.g., HubSpot, Salesforce, Clay, OpenAI), logging configuration, env variable security, and clean modular code structure.
```

## Primary Use Case
Building custom API integrations, webhook listeners, or data pipelines.

## Cross-References
[revops-engineering](../../wiki/skills/revops-engineering.md) . [l2a_matching_engine](../../core/engine/l2a_matcher.py) . [meddpicc_health_engine](../code/scoring/meddpicc_health_engine.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
