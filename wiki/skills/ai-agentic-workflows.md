---
id: skill-ai-agentic-workflows
type: skill
tags: [skill, ai, agentic, mcp, claude]
last_modified: 2026-09-25
confidence_score: 0.45
---

# AI & Agentic Workflows

## Skill Tree
- Prompt engineering patterns (report generation, diagnostics)
- Agent/MCP architecture (Claude Code, n8n as orchestration layer)
- Claude API integration in product

## Prompt Templates
**Diagnostic report generation (self-serve stack-diagnostic engine pattern):**
```
Given intake data across 6 GTM/RevOps domains, generate:
1. Waste metrics per domain
2. Redundancy score (0-100) with rationale
3. 3-bucket consolidation roadmap (kill/consolidate/keep)
Keep tone neutral and vendor-agnostic.
```
**High-spend routing logic (advisory-routing engine pattern):** "Flag this stack as high-complexity if total spend > $100k/yr OR legacy Salesforce APEX present OR custom MCP/agentic workflows detected. If flagged, route to a scoping call rather than diagnosing custom code directly."

## Execution Checklist — Shipping an Agentic Feature
- [ ] Prompt tested against edge-case inputs
- [ ] Output format validated (no hallucinated tool names/pricing)
- [ ] Neutral/no-upsell constraint verified where applicable
- [ ] Cost per report/run estimated before scaling traffic

## See Also
[_Skill_Matrix_Hub](_Skill_Matrix_Hub.md) · index
