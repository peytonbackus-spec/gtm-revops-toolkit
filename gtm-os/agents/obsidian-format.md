---
id: agent-obsidian-format
type: prompt-agent
tags: [prompt-library, utility-knowledge-management]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Knowledge Management
priority: P2
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /obsidian-format -- Note Sanitizer & Wikilink Engine

**Type:** Utility / Knowledge Management

**Status: already enforced structurally** -- this repo's CLAUDE governance file already requires this behavior of every wiki/ note; this prompt operationalizes it for ad-hoc note conversion.

## System Prompt
```
Convert the raw chat text or transcript into a clean Obsidian Markdown file. Include standardized YAML frontmatter (`created`, `type`, `tags`), clean headers (`##`), bold key terms, and relative wikilinks (`Note Name`) connecting to related GTM, RevOps, or tool concepts.
```

## Primary Use Case
Normalizing session logs for direct terminal insertion into GTM-2nd-Brain or Personal-Vault.

## Cross-References
CLAUDE

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
