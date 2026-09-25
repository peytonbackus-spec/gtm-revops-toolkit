---
id: agent-decision
type: prompt-agent
tags: [prompt-library, utility-strategy]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Strategic Decisions
priority: P1
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /decision -- Strategic Trade-Off & Matrix Evaluator

**Type:** Utility / Strategy

**Status: partial overlap** -- related material already exists elsewhere in this repo; this note captures the reusable prompt form specifically.

## System Prompt
```
Evaluate the provided architectural, tool-stack, or go-to-market options. Construct a decision matrix covering: Implementation Effort (1-5), Scalability (1-5), Annual Cost Impact, Primary Risks, and a final Weighted Recommendation with rationale.
```

## Primary Use Case
Evaluating vendor tool choices (e.g., Clay + Apollo vs. ZoomInfo + Outreach) or build vs. buy software decisions.

## Cross-References
[gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md) . [tech-stack-audit](tech-stack-audit.md)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
