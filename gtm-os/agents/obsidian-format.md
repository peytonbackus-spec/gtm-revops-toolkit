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

# /obsidian-format -- Note Sanitizer & Repo-Link Converter

**Type:** Utility / Knowledge Management

**Status: already enforced structurally** -- this repo's CLAUDE governance file already requires this behavior of every wiki/ note; this prompt operationalizes it for ad-hoc note conversion, including converting notes authored in Obsidian (which uses `[[wikilinks]]`) into this repo's own convention.

## System Prompt
```
Convert the raw chat text, transcript, or Obsidian-authored note into a clean Markdown file matching this repo's conventions. Include standardized YAML frontmatter (`id`, `type`, `tags`, `last_modified`), clean headers (`##`), bold key terms, and real relative markdown links (`[Note Name](path/to/Note-Name.md)`) connecting to related GTM, RevOps, or tool concepts -- never Obsidian-style `[[wikilinks]]`, which GitHub does not render.
```

## Primary Use Case
Normalizing session logs or Obsidian export notes for direct insertion into this repo's wiki/ or gtm-os/ structure.

## Cross-References
CLAUDE

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
