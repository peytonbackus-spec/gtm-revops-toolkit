---
id: agent-agentic-workflow
type: prompt-agent
tags: [prompt-library, engineering-ai]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Agent Design
priority: P1
confidence_score: 0.6
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /agentic-workflow -- Multi-Step Autonomous Agent Specifier

**Type:** Engineering & AI

**Status: strong overlap** -- this vault already has substantial real content covering this; this note exists mainly to file the reusable prompt form itself.

## System Prompt
```
Architect an autonomous AI Agent workflow for the requested task. Define: 1) Core Agent Role, 2) Available Tool Definitions (APIs, Web Browsing, Code Interpreter), 3) System Instructions & Guardrails, and 4) Human-in-the-Loop approval checkpoints.
```

## Primary Use Case
Designing autonomous AI workflows for lead research, company diagnostics, or code generation.

## Cross-References
[ai-agentic-workflows](../../wiki/skills/ai-agentic-workflows.md) . [gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md) . [pipeline-risk-contract](../contracts/pipeline-risk-contract.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
