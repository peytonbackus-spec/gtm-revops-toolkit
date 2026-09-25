---
id: full-org-agent-taxonomy
type: concept
tags: [concept, taxonomy, agents, skills]
last_modified: 2026-09-25
---

# Full-Org Skill / Agent / Workflow Taxonomy

> Organized Function -> Purpose -> Priority. Covers all 4 layers this repo now has: **Skills** (`wiki/skills/`), **Agents** (`gtm-os/agents/` -- human-invoked top-level prompts), **Sub-Agents** (`gtm-os/agents/sub-agents/` -- shared single-purpose primitives multiple agents call), and **Workflows/Orchestrations** (`gtm-os/contracts/` -- declared bounded-autonomy automations).

## Workflow/Orchestration Layer
**4 autonomous Workflow Contracts now exist** in `gtm-os/contracts/`: [pipeline-risk-contract](../../gtm-os/contracts/pipeline-risk-contract.md) (original), plus [inbound-lead-qualifier-contract](../../gtm-os/contracts/inbound-lead-qualifier-contract.md), [speed-to-lead-sla-contract](../../gtm-os/contracts/speed-to-lead-sla-contract.md), and [casl-compliance-gate-contract](../../gtm-os/contracts/casl-compliance-gate-contract.md) (promoted this round). Each declares boundaries, a role_map built from the [shared sub-agents](../../gtm-os/agents/sub-agents/00-Sub-Agent-Layer-Index.md), an evidence standard, and stop_rules. The remaining 49 top-level agents are still human-invoked; next promotion candidate: `/crm-hygiene-auto-updater` (same rules-based, low-ambiguity profile as the 3 already promoted).

## Sub-Agent Layer
11 shared primitives now exist so top-level agents stop re-deriving the same logic -- see [Sub-Agent Layer index](../../gtm-os/agents/sub-agents/00-Sub-Agent-Layer-Index.md) for the full reuse map. Highest-reuse: [account-brief-generator](../../gtm-os/agents/account-brief-generator.md)-style agents lean on `usage-data-summarizer`, `competitive-intel-lookup`, and `buying-committee-mapper` most heavily.

## Inbound SDR

**Purpose: Response SLA**
- P0 — /speed-to-lead-sla-enforcer — [Speed-to-Lead SLA & No-Show Recovery Agent](../../gtm-os/agents/speed-to-lead-sla-enforcer.md)
- P0 — /inbound-playbook — [Speed-to-Lead Triage & SLA Structurer](../../gtm-os/agents/inbound-playbook.md)

**Purpose: Intake & Qualification**
- P0 — /inbound-lead-qualifier — [Inbound Lead Intake & Qualification Orchestrator](../../gtm-os/agents/inbound-lead-qualifier.md)

**Purpose: Qualification**
- P0 — /lead-scoring — [Behavioral & Demographic Scoring Engine](../../gtm-os/agents/lead-scoring.md)

## Outbound SDR

**Skills (role competency):**
- [sales-development-strategy](../skills/sales-development-strategy.md)
- [sales-development-leadership](../skills/sales-development-leadership.md)

**Purpose: Targeting**
- P0 — /icp-builder — [Account Scoring & ICP Quantifier](../../gtm-os/agents/icp-builder.md)
- P1 — /prospect-stack-gap-finder — [Prospect Tech Stack Gap Identifier](../../gtm-os/agents/prospect-stack-gap-finder.md)

**Purpose: Objection Handling**
- P1 — /competitive-battlecard — [Market Intelligence & Trap-Setting](../../gtm-os/agents/competitive-battlecard.md)

**Purpose: Outreach Execution**
- P0 — /sequence-builder — [Multi-Channel Outbound Campaign Architect](../../gtm-os/agents/sequence-builder.md)
- P1 — /cold-call-script — [Objection-First Discovery Opener](../../gtm-os/agents/cold-call-script.md)
- P1 — /email-optimizer — [Spam & Deliverability Copy Polisher](../../gtm-os/agents/email-optimizer.md)
- P2 — /voicemail-script — [Cold Voicemail Script Generator](../../gtm-os/agents/voicemail-script.md)
- P2 — /linkedin-social-selling-script — [LinkedIn Social Selling Touch Builder](../../gtm-os/agents/linkedin-social-selling-script.md)

**Purpose: Pipeline Recovery**
- P1 — /win-back-reactivation-sequence-builder — [Closed-Lost & Dormant Account Reactivation Builder](../../gtm-os/agents/win-back-reactivation-sequence-builder.md)

**Purpose: Research & Prep**
- P0 — /account-research-brief — [Prospect Trigger-Event & Pain Compiler](../../gtm-os/agents/account-research-brief.md)

**Purpose: Legal Compliance**
- P0 — /casl-cold-outreach-compliance-checker — [CASL Cold Outreach Compliance Checker](../../gtm-os/agents/casl-cold-outreach-compliance-checker.md)

## Account Executive

**Skills (role competency):**
- [business-development](../skills/business-development.md)
- [account-executive](../skills/account-executive.md)

**Purpose: Pre-Call Preparation**
- P0 — /account-brief-generator — [Pre-Call Account Brief Compiler](../../gtm-os/agents/account-brief-generator.md)

**Purpose: Deal Support**
- P1 — /rfp-proposal-generator — [RFP & Proposal First-Draft Generator](../../gtm-os/agents/rfp-proposal-generator.md)

**Purpose: Demo**
- P0 — /demo-narrative-architect — [Demo Flow & Narrative Arc Builder](../../gtm-os/agents/demo-narrative-architect.md)

**Purpose: Negotiation & Closing**
- P0 — /mutual-close-plan-builder — [Mutual Close Plan Architect](../../gtm-os/agents/mutual-close-plan-builder.md)

**Purpose: Technical Validation**
- P1 — /poc-pilot-success-plan-builder — [POC/Pilot Success Plan Builder](../../gtm-os/agents/poc-pilot-success-plan-builder.md)

## Customer Success

**Skills (role competency):**
- [account-management-customer-success](../skills/account-management-customer-success.md)

**Purpose: Advocacy**
- P2 — /advocacy-program-builder — [Customer Advocacy & Reference Program Builder](../../gtm-os/agents/advocacy-program-builder.md)

**Purpose: Adoption & Retention**
- P1 — /qbr-builder — [Quarterly Business Review Builder](../../gtm-os/agents/qbr-builder.md)

**Purpose: Onboarding**
- P0 — /customer-onboarding-playbook-builder — [Customer Onboarding Playbook Builder](../../gtm-os/agents/customer-onboarding-playbook-builder.md)

**Purpose: Risk Management**
- P1 — /escalation-runbook — [Customer Escalation Runbook Builder](../../gtm-os/agents/escalation-runbook.md)

**Purpose: Renewal**
- P0 — /renewal-playbook — [Proactive Renewal Motion Builder](../../gtm-os/agents/renewal-playbook.md)

**Purpose: Expansion**
- P1 — /expansion-upsell-play-builder — [Expansion & Upsell Play Builder](../../gtm-os/agents/expansion-upsell-play-builder.md)

## RevOps

**Skills (role competency):**
- [revops-engineering](../skills/revops-engineering.md)
- [data-pipeline-analytics](../skills/data-pipeline-analytics.md)

**Purpose: Integration**
- P1 — /webhook-transformer — [JSON Payload Parser & Data Mapper](../../gtm-os/agents/webhook-transformer.md)

**Purpose: Data Model**
- P0 — /revops-schema — [CRM Custom Object & Lifecycle Modeler](../../gtm-os/agents/revops-schema.md)

**Purpose: Reporting**
- P1 — /sql-pipeline — [Revenue Data Warehousing & SQL Query Engine](../../gtm-os/agents/sql-pipeline.md)
- P1 — /attribution-model — [Multi-Touch Revenue Attribution Architect](../../gtm-os/agents/attribution-model.md)

**Purpose: Data Quality**
- P1 — /crm-hygiene-auto-updater — [CRM Hygiene & Auto-Update Agent Spec](../../gtm-os/agents/crm-hygiene-auto-updater.md)

**Purpose: Tooling Audit**
- P1 — /tech-stack-audit — [SaaS Utilization & Redundancy Inspector](../../gtm-os/agents/tech-stack-audit.md)

**Purpose: Forecasting**
- P0 — /forecast-rollup — [Multi-Rep Forecast Roll-Up Builder](../../gtm-os/agents/forecast-rollup.md)

**Purpose: Data Enrichment**
- P0 — /clay-waterfall — [Data Enrichment & Scraping Strategy](../../gtm-os/agents/clay-waterfall.md)

## Partner & Channel

**Purpose: Enablement**
- P2 — /partner-channel-enablement-brief — [Partner & Channel Enablement Brief Builder](../../gtm-os/agents/partner-channel-enablement-brief.md)

## GTM Strategy & Leadership

**Skills (role competency):**
- [gtm-leadership](../skills/gtm-leadership.md)
- [sales-leadership](../skills/sales-leadership.md)

**Purpose: Pricing**
- P1 — /pricing-packaging-optimizer — [Tier & Packaging Design Optimizer](../../gtm-os/agents/pricing-packaging-optimizer.md)

**Purpose: Executive Reporting**
- P2 — /board-investor-narrative-builder — [Board & Investor Revenue Narrative Builder](../../gtm-os/agents/board-investor-narrative-builder.md)

**Purpose: Messaging**
- P1 — /positioning-framework — [Messaging & Value Prop Architect](../../gtm-os/agents/positioning-framework.md)

**Purpose: Diagnostics**
- P0 — /gtm-audit — [Revenue Funnel & Friction Diagnostic](../../gtm-os/agents/gtm-audit.md)

**Purpose: Deal Forensics**
- P1 — /win-loss-analyzer — [Deal Forensics Engine](../../gtm-os/agents/win-loss-analyzer.md)

**Purpose: Cross-Functional Alignment**
- P1 — /marketing-sales-sla-builder — [Marketing-to-Sales SLA & Handoff Builder](../../gtm-os/agents/marketing-sales-sla-builder.md)

**Purpose: Strategic Planning**
- P1 — /gtm-motion-selector — [GTM Motion Selector (PLG vs. Sales-Led vs. Hybrid)](../../gtm-os/agents/gtm-motion-selector.md)

**Purpose: Compensation Design**
- P1 — /commission-plan — [Variable Compensation & Incentive Structurer](../../gtm-os/agents/commission-plan.md)

## Cross-Functional / Engineering & Utility

**Skills (role competency):**
- [ai-agentic-workflows](../skills/ai-agentic-workflows.md)

**Purpose: Output Refinement**
- P2 — /loop — [Recursive Iteration & Output Refinement](../../gtm-os/agents/loop.md)

**Purpose: Agent Design**
- P1 — /agentic-workflow — [Multi-Step Autonomous Agent Specifier](../../gtm-os/agents/agentic-workflow.md)

**Purpose: Meta-Tooling**
- P2 — /prompt-expand — [Meta-Prompt Engineering Engine](../../gtm-os/agents/prompt-expand.md)

**Purpose: Planning**
- P2 — /goal — [Objective-to-Task Decomposition](../../gtm-os/agents/goal.md)

**Purpose: Automation Build**
- P1 — /python-gtm-script — [Revenue Operations & API Automation Builder](../../gtm-os/agents/python-gtm-script.md)

**Purpose: Local Tooling**
- P2 — /cli-tool-builder — [Shell & Zsh Automation Architect](../../gtm-os/agents/cli-tool-builder.md)

**Purpose: Strategic Decisions**
- P1 — /decision — [Strategic Trade-Off & Matrix Evaluator](../../gtm-os/agents/decision.md)

**Purpose: Agent Tooling**
- P1 — /mcp-server-spec — [MCP Tool/Server Definition Writer](../../gtm-os/agents/mcp-server-spec.md)

**Purpose: Knowledge Management**
- P2 — /obsidian-format — [Note Sanitizer & Wikilink Engine](../../gtm-os/agents/obsidian-format.md)

**Purpose: Vault Governance & Maintenance**
- P1 — /vault-health-audit — [Vault Structural Health Auditor](../../gtm-os/agents/vault-health-audit.md) -- net-new, built from the 2026-09-25 audit

## Priority Legend
- **P0** — highest leverage / build or use first (time-sensitive, high-frequency, revenue- or compliance-critical)
- **P1** — solid value, not urgent
- **P2** — nice-to-have, lower frequency or lower leverage

## Sources
[The Default 9 RevOps Jobs](../../raw-sources/articles/full-org-agent-research/01-default-9-revops-jobs.md) . [Mutual Close Plan Research](../../raw-sources/articles/full-org-agent-research/02-mutual-close-plan.md) . [CS Playbook Framework](../../raw-sources/articles/full-org-agent-research/03-cs-playbook-framework.md)

## See Also
[00-Prompt-Library-Index](../../gtm-os/agents/00-Prompt-Library-Index.md) . [Sub-Agent Layer](../../gtm-os/agents/sub-agents/00-Sub-Agent-Layer-Index.md) . [_Skill_Matrix_Hub](../skills/_Skill_Matrix_Hub.md) . [gtm-stack-integration-architecture](gtm-stack-integration-architecture.md)
