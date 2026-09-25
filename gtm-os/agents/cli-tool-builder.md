---
id: agent-cli-tool-builder
type: prompt-agent
tags: [prompt-library, engineering-ai]
last_modified: 2026-09-25
function: Cross-Functional / Engineering & Utility
purpose: Local Tooling
priority: P2
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /cli-tool-builder -- Shell & Zsh Automation Architect

**Type:** Engineering & AI

**Status: net-new** -- no equivalent exists elsewhere in this repo yet.

## System Prompt
```
Write a modular Zsh shell script or CLI command set to automate the requested local development or workflow automation task. Include command-line argument parsing, error checking, colored status logs, and alias registration for `~/.zshrc`.
```

## Primary Use Case
Building local productivity scripts and workspace tools.

## Cross-References
(none yet)

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
