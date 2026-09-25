---
id: raw-cleanlist-gtm-engineering
type: raw-source
tags: [raw-source, gtm-engineering]
last_modified: 2026-09-25
source_url: https://www.cleanlist.ai/blog/2026-05-22-what-is-gtm-engineering
accessed: 2026-09-25
---

# RAW: "What is GTM Engineering?" (Cleanlist, 2026-05-22)

Key extracted points (verbatim/paraphrased, immutable — do not edit, only cite from wiki/):
- 6-layer stack: CRM Core (Salesforce/HubSpot/Attio) -> Data & Identity (Cleanlist/Clay/ZoomInfo) -> Intelligence (6sense/Bombora/UserGems) -> Execution (Outreach/Salesloft/Apollo) -> Orchestration (n8n/Zapier/MCP servers) -> Analytics (Gong/Dreamdata/warehouse)
- Two workflow patterns: deterministic (scheduled REST API, repeatable) vs agentic (MCP, interactive/adaptive)
- Practical handoff: design/debug interactively via agent, then convert to scheduled API calls for production
- Core connection pattern: enrichment -> CRM -> playbooks listening for triggers -> ICP filter -> multi-provider enrichment waterfall -> scoring -> sequence queue / reverse ETL to CRM
- Required skills: SQL, one programming language (Python/TypeScript), CRM data model fluency, API/webhook literacy (OAuth, rate limits, idempotency, retries)
- Weekly rhythm: Mon list-building, Tue-Wed playbook dev, Thu SQL/dedup/scoring, Fri monitor failed syncs
