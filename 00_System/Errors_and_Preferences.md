---
type: system
category: system
tags:
  - errors
  - system-rules
  - preferences
date: 2026-08-21
status: active
---

# Terminal Errors & User Preferences Log

## 1. Execution & Terminal Rules
* **NO Heredocs or Multiline Inline Scripts:** Never pass raw multiline string blocks or heredocs (<< EOF) into Zsh. Always use clean single-line python commands or write to .py files.
* **No Single-Quote Escaping Inside Double-Quotes:** Keep string formatting strictly escaped or use Python base64/pathlib to avoid shell quote drops.

## 2. Technical Preferences & Workflow Standards
* **Vault Structure:** All RevOps documentation lives under 20_Areas/RevOps/, and executable code lives under 30_Resources/Code/.
* **Auto-Syncing:** Execute /Users/peytonbackus/GTM 2nd Brain/sync_vault.sh after creating or modifying vault assets.

## 3. Decision & Preference Log
| Date | Decision / Requirement | Reason | Status |
| :--- | :--- | :--- | :--- |
| 2026-08-21 | Use direct single-line Python file writers instead of multiline terminal strings | Eliminates Zsh parse errors and heredoc hanging loops | Active |
| 2026-08-21 | Maintain 00_System/Errors_and_Preferences.md for system errors and user decisions | Prevents repeating terminal issues and logs architectural choices | Active |
| 2026-08-21 | Use cat EOF heredoc for python script creation | Bypasses Zsh history expansion, escaping issues, and non-UTF-8 encoding errors | Active |
