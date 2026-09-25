---
id: agent-mcp-server-spec
type: prompt-agent
tags: [prompt-library, engineering-ai]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Agent Tooling
priority: P1
confidence_score: 0.4
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /mcp-server-spec -- MCP Tool/Server Definition Writer

**Type:** Engineering & AI

**Status: net-new, identified via external research** -- not among the 25 supplied; added after researching current GTM prompt-library practice.

## System Prompt
```
Given a desired capability (e.g., 'query Salesforce opportunities', 'trigger an Orum dial session'), write a complete MCP server tool definition: tool name, input schema (JSON Schema), description written for an LLM caller, expected output shape, and error-handling behavior for auth failures and rate limits.
```

## Primary Use Case
Specifying new MCP tools for agentic GTM workflows -- directly relevant to Peyton's own Claude/MCP-based tooling work.

## Cross-References
[ai-agentic-workflows](../../wiki/skills/ai-agentic-workflows.md) . [agentic-workflow](agentic-workflow.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . index
