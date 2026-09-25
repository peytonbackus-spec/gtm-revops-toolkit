---
id: prompt-library-index
type: hub
tags: [hub, prompt-library]
last_modified: 2026-09-25
---

# Prompt Library Index (gtm-os/agents/)

32 reusable slash-command style prompts. These are human-invoked utility prompts, not autonomous background automations -- per CLAUDE.md's bounded-autonomy rule, only agents that act *without* a human invoking them each time need a declared Workflow Contract in `gtm-os/contracts/`.

**New here?** Skip memorizing the commands below -- use [the Agent Router](00-Agent-Router.md) and just describe what you need in plain language; it maps your request to the right agent/sub-agent and expands it automatically (see CLAUDE.md's Router Protocol).

## By Category

### Utility / Execution
- /loop -- [Recursive Iteration & Output Refinement](loop.md) -- Status: net-new
- /goal -- [Objective-to-Task Decomposition](goal.md) -- Status: net-new

### Utility / Strategy
- /decision -- [Strategic Trade-Off & Matrix Evaluator](decision.md) -- Status: partial overlap

### Utility / Engineering
- /prompt-expand -- [Meta-Prompt Engineering Engine](prompt-expand.md) -- Status: net-new

### Utility / Knowledge Management
- /obsidian-format -- [Note Sanitizer & Wikilink Engine](obsidian-format.md) -- Status: already enforced structurally

### Utility / Vault Governance
- /vault-health-audit -- [Vault Structural Health Auditor](vault-health-audit.md) -- Status: net-new, 2026-09-25 audit

### GTM Strategy & Advisory
- /gtm-audit -- [Revenue Funnel & Friction Diagnostic](gtm-audit.md) -- Status: partial overlap
- /positioning-framework -- [Messaging & Value Prop Architect](positioning-framework.md) -- Status: partial overlap
- /icp-builder -- [Account Scoring & ICP Quantifier](icp-builder.md) -- Status: net-new
- /competitive-battlecard -- [Market Intelligence & Trap-Setting](competitive-battlecard.md) -- Status: partial overlap
- /win-loss-analyzer -- [Deal Forensics Engine](win-loss-analyzer.md) -- Status: net-new
- /pricing-packaging-optimizer -- [Tier & Packaging Design Optimizer](pricing-packaging-optimizer.md) -- Status: net-new, identified via external research

### Revenue Operations
- /revops-schema -- [CRM Custom Object & Lifecycle Modeler](revops-schema.md) -- Status: strong overlap
- /lead-scoring -- [Behavioral & Demographic Scoring Engine](lead-scoring.md) -- Status: net-new
- /attribution-model -- [Multi-Touch Revenue Attribution Architect](attribution-model.md) -- Status: confirmed gap
- /commission-plan -- [Variable Compensation & Incentive Structurer](commission-plan.md) -- Status: partial overlap
- /tech-stack-audit -- [SaaS Utilization & Redundancy Inspector](tech-stack-audit.md) -- Status: strong overlap
- /renewal-playbook -- [Proactive Renewal Motion Builder](renewal-playbook.md) -- Status: net-new, identified via external research
- /forecast-rollup -- [Multi-Rep Forecast Roll-Up Builder](forecast-rollup.md) -- Status: net-new, identified via external research

### Sales Development
- /sequence-builder -- [Multi-Channel Outbound Campaign Architect](sequence-builder.md) -- Status: partial overlap
- /cold-call-script -- [Objection-First Discovery Opener](cold-call-script.md) -- Status: net-new
- /email-optimizer -- [Spam & Deliverability Copy Polisher](email-optimizer.md) -- Status: net-new
- /clay-waterfall -- [Data Enrichment & Scraping Strategy](clay-waterfall.md) -- Status: strong overlap
- /inbound-playbook -- [Speed-to-Lead Triage & SLA Structurer](inbound-playbook.md) -- Status: partial overlap
- /account-research-brief -- [Prospect Trigger-Event & Pain Compiler](account-research-brief.md) -- Status: net-new, identified via external research
- /prospect-stack-gap-finder -- [Prospect Tech Stack Gap Identifier](prospect-stack-gap-finder.md) -- Status: net-new, identified via external research
- /demo-narrative-architect -- [Demo Flow & Narrative Arc Builder](demo-narrative-architect.md) -- Status: net-new, identified via external research

### Engineering & AI
- /python-gtm-script -- [Revenue Operations & API Automation Builder](python-gtm-script.md) -- Status: strong overlap
- /sql-pipeline -- [Revenue Data Warehousing & SQL Query Engine](sql-pipeline.md) -- Status: partial overlap
- /webhook-transformer -- [JSON Payload Parser & Data Mapper](webhook-transformer.md) -- Status: partial overlap
- /agentic-workflow -- [Multi-Step Autonomous Agent Specifier](agentic-workflow.md) -- Status: strong overlap
- /cli-tool-builder -- [Shell & Zsh Automation Architect](cli-tool-builder.md) -- Status: net-new
- /mcp-server-spec -- [MCP Tool/Server Definition Writer](mcp-server-spec.md) -- Status: net-new, identified via external research

See the organized breakdown in [Full-Org Taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) (Function -> Purpose -> Priority).

See also the [Sub-Agent Layer](sub-agents/00-Sub-Agent-Layer-Index.md) -- 11 shared primitives these agents call instead of duplicating logic.

## See Also
[_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md) . [gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md)
