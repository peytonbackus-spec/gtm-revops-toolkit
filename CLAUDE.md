# SYSTEM GOVERNANCE & BEHAVIORAL MANUAL

## 1. Operating Rules & Boundaries
- **Immutable Raw Data:** Never modify files inside `raw-sources/`. Treat them as immutable ground truth.
- **Bounded Autonomy:** All automations in `gtm-os/` must declare a valid Workflow Contract in `gtm-os/contracts/`.
- **HITL Verification:** Any write operation affecting CRM metadata or external channels (Slack, Email) requires human authorization (Accept/Modify/Ignore).
- **Strict Citation Standard:** Synthesized notes in `wiki/` must link back to source notes in `raw-sources/`.

## 2. Router Protocol (No Slash Commands Required)
When asked to do something this repo's prompt library covers, invoke it in plain language rather than requiring the exact slash command:

1. **Match silently.** Consult `gtm-os/agents/00-Agent-Router.md` (or `wiki/concepts/full-org-agent-taxonomy.md` for the broader Function -> Purpose -> Priority view) and identify the best-matching top-level agent or sub-agent. Don't announce which one was selected -- go straight to the expanded work.
2. **Expand the casual prompt into that agent's System Prompt structure**, filling in the person's specifics.
3. **Execute immediately.**
4. **If genuinely ambiguous** between two agents, ask one clarifying question rather than guessing.
5. **New requests that fit no existing agent** are a real gap -- say so, and either build the missing agent (per the taxonomy's Function/Purpose/Priority conventions) or note it for later.

### 2a. Correction Feedback Loop
When an output is wrong, fix the underlying cause, not just the one answer: sharpen the Agent Router's description if the wrong agent was matched, revise the agent's System Prompt if the match was right but the output was flawed, or build a new agent/sub-agent if nothing covers the need. Log corrections in `gtm-os/router-corrections-log.md`.

## 3. Note Schema Requirements
- All files in `wiki/` must contain valid frontmatter: `id`, `type`, `tags`, `last_modified`, `confidence_score`.
- New concepts must be linked back to `README.md` or a primary hub file.

## 4. Existing Codebase Precedence
This repo already has real, working implementations of several concepts the prompt library describes conceptually (`core/engine/`, `modules/gtm_engineering/`). Where a real implementation exists, the prompt library's docs link to it directly rather than duplicating a weaker stand-in -- see `gtm-os/code/00-Code-Index.md`. Only add a new code stand-in under `gtm-os/code/` when no better real implementation exists yet.

## 5. Execution Environment
- Primary OS: macOS (Zsh)
- Primary Stack: Claude Code + Model Context Protocol (MCP)
