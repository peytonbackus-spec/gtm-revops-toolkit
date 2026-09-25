---
id: vault-audit-2026-09-25
type: audit
tags: [hub, meta, audit, vault-health]
last_modified: 2026-09-25
---

> **Context:** this audit was run against the Obsidian "GTM 2nd Brain" vault specifically (a separate, private knowledge base) -- filed here as a dated record of the audit methodology and findings, several of which (the automation-layer gap, the agent library structure) are directly relevant to this repo too.

# Vault Health Audit -- 2026-09-25

Structural audit of the GTM 2nd Brain: link-graph scan (broken links, orphaned files, duplicate basenames), frontmatter compliance vs. CLAUDE.md Section 3, and a read-through of the legacy PARA folders against the 4-layer architecture. 141 notes scanned. Findings ordered by impact; each has evidence and a recommended fix. Suggest tackling in the order listed -- later fixes (the automation gap) are much bigger lifts than the earlier ones (linking, dedup).

## Critical

### 1. Two competing "front doors" -- README.md is stale and describes a structure that no longer exists
`README.md` (vault root) still documents the old PARA layout (`20_Areas/RevOpp/Specs/`, `30_Resources/Code/scoring/`, etc.) as the vault's primary structure, with no mention of `index.md`, the 4-layer architecture, `gtm-os/`, or the Agent Router. 113 of the vault's 141 files were created *after* README.md was last touched. Anyone (including a fresh Claude session without this conversation's context) opening README.md first gets a picture of the vault that's actively wrong.
- **Fix:** Rewrite README.md as a short pointer ("start at index and CLAUDE") rather than a structural description, or fold its still-useful operational notes (e.g. `python3 30_Resources/Code/sfdc_pql_ingestor.py` usage) into the relevant `gtm-os/` docs and retire it.

### 2. The legacy PARA folders were merged into the git repo but never actually connected to the new architecture
`00_Meta/`, `10_Projects/`, `20_Areas/`, `30_Resources/`, `40_Archives/` (16 files total) sit at the vault root, fully orphaned -- zero incoming wikilinks from `index.md`, `wiki/`, or `gtm-os/`. This includes real, load-bearing content:
- `30_Resources/Code/` -- the **actual Python implementations** several agents describe conceptually: `meddpicc_health_engine.py`, `churn_prediction_pipeline.py`, `l2a_matching_engine.py`, `sfdc_pql_ingestor.py`, `revops_tech_debt_tracker.py`, plus a test suite.
- `20_Areas/RevOpp/Specs/` -- `SFDC_MEDDPICC_Validation_Spec.md`, `SFDC_Tech_Debt_Audit.md`, and `GTM_OS_Architecture_Spec.md` (a spec for the very architecture `gtm-os/` implements).
- `00_GTM_Dashboard.md` at vault root -- a second, orphaned "home page" competing with `index.md`, linking to two more dead targets (Canvas files that were never created).

**RESOLVED (same session):** moved to `gtm-os/dashboard.md`, dead Canvas links removed, linked from `index.md`.

**Why this matters more than it looks:** agents like `deal-health-scorer.md`, `lead-scoring.md`, `qbr-builder.md`, `escalation-runbook.md`, and `python-gtm-script.md` reference `meddpicc_health_engine.py`'s exact point weights *by memory/description*, not by link, so if that file is ever edited the docs will silently drift from the real logic with nothing to catch it.
- **Fix:** Move `30_Resources/Code/` under a proper `gtm-os/code/` location, add a companion `.md` note per script so wikilinks resolve, fold the two real specs into `wiki/concepts/`, retire the old dashboard location, and delete the empty nested `.git` repo.

**RESOLVED (same session):** all of the above done -- code moved with 6 companion notes, specs moved with frontmatter, dashboard relocated, nested `.git` deleted, CI paths fixed.

### 3. Zero real automation layer -- everything is a prompt template, nothing executes on its own
`gtm-os/mcp/` and `gtm-os/schemas/` are both empty directories. All 4 Workflow Contracts (`pipeline-risk`, `inbound-lead-qualifier`, `speed-to-lead-sla`, `casl-compliance-gate`) declare `allowed_mcp_tools` and `boundaries`, but there is no MCP server implementation anywhere in the vault that would let a contract actually run against Salesforce/Outreach/Clay data without a human pasting it into a chat first. The vault is comprehensive as a **prompt and governance library** but has built zero of the "L2 Automation" layer CLAUDE.md's own architecture promises.
- **Fix:** Treat as its own project: pick the highest-value contract and build one real MCP tool end-to-end as a proof of concept before trying to wire all four.

**PARTIALLY RESOLVED (same session):** built a proof-of-concept MCP server for `speed-to-lead-sla-contract` -- 1 of 5 tools is real logic, 4 are mocked pending real credentials (see that README for the wiring plan). `pipeline-risk`, `inbound-lead-qualifier`, and `casl-compliance-gate` are still unbuilt -- see 00-Automation-Layer-Index for recommended order.

## High

### 4. Contracts have no companion notes -- they're invisible to Obsidian's graph and search
All 4 `.yaml` contracts in `gtm-os/contracts/` are pure YAML with no `.md` counterpart. Every `pipeline-risk-contract`-style wikilink pointing at them (there are 6+ across the vault) resolves to nothing in Obsidian, because bare `...` links only match markdown notes by default -- these show as broken/red links in the actual app even though the YAML file exists on disk.
- **Fix:** Add a thin `.md` note per contract (same basename) with frontmatter + a short human summary.

**RESOLVED (same session):** all 4 contracts now have companion notes.

### 5. Strict Citation Standard (CLAUDE.md Section 3) isn't actually being followed
Zero synthesized notes in `wiki/concepts/` link back to their `raw-sources/articles/` research with wikilinks -- confirmed on `gtm-stack-integration-architecture.md` and the CASL compliance checker, both of which were explicitly built from dated research drops in `raw-sources/articles/`. The 13 raw-source research files are all orphaned (no inbound links at all), so the citation trail this vault's own governance rule requires doesn't exist in practice.
- **Fix:** Add a `## Sources` section to each `wiki/concepts/*.md` and research-derived agent, linking back to its `raw-sources/articles/.../NN-topic.md` file(s).

### 6. Duplicate/conflicting HubSpot notes
`wiki/competitive/tools/HubSpot.md` (269 lines, full profile) and `30_Resources/Tech_Stack/HubSpot.md` (10-line stub) share a basename -- any `HubSpot` link is ambiguous, and Obsidian will pick one arbitrarily.
- **Fix:** These turned out to be two different things wearing the same filename (internal cost-tracking vs. market-research profile), not true duplicates.

**RESOLVED (same session):** renamed the internal one to `gtm-os/stack/internal-hubspot.md` with a disambiguating note; no content was lost.

## Medium

### 7. Tool intelligence notes rely entirely on Dataview for discovery, with no static fallback
All 27 files in `wiki/competitive/tools/` are orphaned by plain wikilink -- they're surfaced only through `FROM #gtm/intelligence` Dataview queries in `GTM Intelligence Overview.md`. That's a reasonable pattern, but it means if Dataview is ever disabled, uninstalled, or a tag typo breaks the query, all 27 profiles become unreachable from vault navigation with no warning.
- **Fix:** Add a plain wikilink table of contents to `GTM Intelligence Overview.md` alongside the Dataview table, or at minimum link the 3-5 most-used tool profiles (Salesforce, Outreach, Clay-adjacent tools) directly from `index.md`.

### 8. Empty `intelligence/daily/` and `intelligence/weekly/` folders
The L4 Intelligence layer's only real content is two log files (`decision-log.md`, `action-tracker.md`) under `intelligence/logs/`; the `daily/` and `weekly/` subfolders that the architecture implies exist are empty. Either the cadence they were meant for isn't happening yet, or they're dead scaffolding.
- **Fix:** Either start populating them (this audit itself is a natural first `intelligence/weekly/` entry) or remove them until there's a real weekly/daily synthesis habit, so empty folders don't imply false completeness.

## Suggested new agent
This exact audit is a repeatable job -- recommend codifying it as a new P1 Cross-Functional agent, `/vault-health-audit`, that runs this link-graph + frontmatter + staleness scan on demand (or could later be scheduled). Would prevent this kind of drift from re-accumulating silently.

## See Also
index . CLAUDE . Router Corrections Log . full-org-agent-taxonomy
