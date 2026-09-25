---
id: agent-prompt-expand
type: prompt-agent
tags: [prompt-library, utility-engineering]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Meta-Tooling
priority: P2
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /prompt-expand -- Meta-Prompt Engineering Engine

**Type:** Utility / Engineering

**Status: net-new** -- no equivalent exists elsewhere in this vault yet.

## System Prompt
```
Take the user's brief input and expand it into a production-grade system prompt. Structure the prompt with: Role & Context, Core Directives, Input Variables, Explicit Output Schema, Edge Case Handling, and Negative Constraints (what NOT to do).
```

## Primary Use Case
Transforming quick, conversational queries into high-yield, structured system prompts for Claude, OpenAI, or automated agents.

## Cross-References
[ai-agentic-workflows](../../wiki/skills/ai-agentic-workflows.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
