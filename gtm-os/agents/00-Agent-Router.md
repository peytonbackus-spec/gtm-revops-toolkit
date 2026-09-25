---
id: agent-router
type: hub
tags: [hub, router, routing-table]
last_modified: 2026-09-25
---

# Agent Router -- Lookup Table

Routing reference for the Router Protocol in CLAUDE.md: given a plain-language request, find the best-matching row by function/purpose/use-case, not by requiring the person to know the slash command.

## Top-Level Agents by Function

### Inbound SDR
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P0 | `/inbound-lead-qualifier` | [Inbound Lead Intake & Qualification Orchestrator](inbound-lead-qualifier.md) | The full inbound intake job -- broader than pure scoring: enrichment + dedup + ownership + score in one pass, matching how top RevOps teams... |
| P0 | `/inbound-playbook` | [Speed-to-Lead Triage & SLA Structurer](inbound-playbook.md) | Optimizing conversion rates on inbound demo requests and contact forms. |
| P0 | `/lead-scoring` | [Behavioral & Demographic Scoring Engine](lead-scoring.md) | Optimizing inbound lead triage and inbound-to-outbound routing rules. |
| P0 | `/speed-to-lead-sla-enforcer` | [Speed-to-Lead SLA & No-Show Recovery Agent](speed-to-lead-sla-enforcer.md) | Speed-to-lead is the single highest-leverage inbound metric -- this formalizes it as an enforceable SLA with a no-show recovery motion, not... |

### Outbound SDR
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P0 | `/account-research-brief` | [Prospect Trigger-Event & Pain Compiler](account-research-brief.md) | Pre-call/pre-sequence research so outbound leads with a real trigger event instead of a generic pitch. |
| P0 | `/casl-cold-outreach-compliance-checker` | [CASL Cold Outreach Compliance Checker](casl-cold-outreach-compliance-checker.md) | Peyton's consulting firm is Ontario-registered and its core delivery stack (Apollo/Clay/sequences) is cold outbound to B2B contacts -- CASL... |
| P0 | `/icp-builder` | [Account Scoring & ICP Quantifier](icp-builder.md) | Quantifying target account profiles before launching outbound pipeline generation campaigns. |
| P0 | `/sequence-builder` | [Multi-Channel Outbound Campaign Architect](sequence-builder.md) | Designing outbound sequences for SDR/BDR campaigns. |
| P1 | `/cold-call-script` | [Objection-First Discovery Opener](cold-call-script.md) | Equipping outbound teams with phone playbooks that bypass initial resistance. |
| P1 | `/competitive-battlecard` | [Market Intelligence & Trap-Setting](competitive-battlecard.md) | Equipping sales development reps and account executives with objection handling against market incumbents. |
| P1 | `/email-optimizer` | [Spam & Deliverability Copy Polisher](email-optimizer.md) | Ensuring cold email copy bypasses spam filters and maximizes reply rates. |
| P1 | `/prospect-stack-gap-finder` | [Prospect Tech Stack Gap Identifier](prospect-stack-gap-finder.md) | Selling INTO a gap in a prospect's stack, distinct from /tech-stack-audit which reviews your own or a client's existing stack for... |
| P1 | `/win-back-reactivation-sequence-builder` | [Closed-Lost & Dormant Account Reactivation Builder](win-back-reactivation-sequence-builder.md) | Closed-lost pipeline is a common, high-ROI, and previously uncovered source of new pipeline -- distinct from both outbound prospecting... |
| P2 | `/linkedin-social-selling-script` | [LinkedIn Social Selling Touch Builder](linkedin-social-selling-script.md) | Channel-specific script -- sequence-builder covers LinkedIn generically as one touch in a multi-channel sequence; this is the dedicated... |
| P2 | `/voicemail-script` | [Cold Voicemail Script Generator](voicemail-script.md) | High-frequency micro-skill for dial-heavy outbound (Orum/parallel dialing) -- distinct enough from the full cold-call-script to warrant its... |

### Account Executive
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P0 | `/account-brief-generator` | [Pre-Call Account Brief Compiler](account-brief-generator.md) | The highest-frequency AE prep task -- directly grounded in real-world RevOps automation practice (account-brief generation is one of the... |
| P0 | `/demo-narrative-architect` | [Demo Flow & Narrative Arc Builder](demo-narrative-architect.md) | Turning generic feature-tour demos into pain-anchored narratives that map to MEDDPICC qualification. |
| P0 | `/mutual-close-plan-builder` | [Mutual Close Plan Architect](mutual-close-plan-builder.md) | Closes the biggest gap in the original 25: negotiation/closing had no dedicated agent. Grounded in the co-created 'shared timeline' model... |
| P1 | `/poc-pilot-success-plan-builder` | [POC/Pilot Success Plan Builder](poc-pilot-success-plan-builder.md) | No agent existed anywhere in this repo for technical validation/pilot management -- a distinct motion from discovery or demo, common in... |
| P1 | `/rfp-proposal-generator` | [RFP & Proposal First-Draft Generator](rfp-proposal-generator.md) | Turns a multi-day RFP response into a first-draft-plus-review cycle instead of writing from scratch each time. |

### Customer Success
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P0 | `/customer-onboarding-playbook-builder` | [Customer Onboarding Playbook Builder](customer-onboarding-playbook-builder.md) | The single biggest gap found: no onboarding agent existed anywhere in this repo despite it being the foundational CS motion... |
| P0 | `/renewal-playbook` | [Proactive Renewal Motion Builder](renewal-playbook.md) | Distinct from reactive churn scoring (see churn_prediction_pipeline) -- this is the proactive, calendar-driven renewal motion. |
| P1 | `/escalation-runbook` | [Customer Escalation Runbook Builder](escalation-runbook.md) | Distinct from health scoring (which detects risk) -- this is the response runbook for what happens once risk is detected. |
| P1 | `/expansion-upsell-play-builder` | [Expansion & Upsell Play Builder](expansion-upsell-play-builder.md) | CS playbook frameworks explicitly separate Adoption/Renewal from Expansion as its own lifecycle stage -- this fills that gap. |
| P1 | `/qbr-builder` | [Quarterly Business Review Builder](qbr-builder.md) | Promotes the inline QBR prompt already sketched in the AM/CS skill note into its own standalone reusable agent. |
| P2 | `/advocacy-program-builder` | [Customer Advocacy & Reference Program Builder](advocacy-program-builder.md) | CS playbook frameworks list Advocacy as its own lifecycle stage alongside onboarding/adoption/renewal -- previously uncovered here. |

### RevOps
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P0 | `/clay-waterfall` | [Data Enrichment & Scraping Strategy](clay-waterfall.md) | Engineering automated outbound data enrichment pipelines inside Clay or Python. |
| P0 | `/forecast-rollup` | [Multi-Rep Forecast Roll-Up Builder](forecast-rollup.md) | Turning individual deal health scores (see meddpicc_health_engine) into a team/org-level forecast view for sales leadership. |
| P0 | `/revops-schema` | [CRM Custom Object & Lifecycle Modeler](revops-schema.md) | Designing scalable CRM architectures, deal pipeline schemas, and automated data flows. |
| P1 | `/attribution-model` | [Multi-Touch Revenue Attribution Architect](attribution-model.md) | Measuring pipeline generation efficiency and channel ROI across complex tech stacks. |
| P1 | `/crm-hygiene-auto-updater` | [CRM Hygiene & Auto-Update Agent Spec](crm-hygiene-auto-updater.md) | One of the highest-frequency real RevOps automation jobs (keeping CRM records current from call activity) -- was not covered by any of the... |
| P1 | `/sql-pipeline` | [Revenue Data Warehousing & SQL Query Engine](sql-pipeline.md) | Extracting revenue performance metrics from analytical databases or BI platforms. |
| P1 | `/tech-stack-audit` | [SaaS Utilization & Redundancy Inspector](tech-stack-audit.md) | Conducting tool stack audits to optimize SaaS spend and eliminate workflow overlap. |
| P1 | `/webhook-transformer` | [JSON Payload Parser & Data Mapper](webhook-transformer.md) | Connecting disparate RevOps tools (e.g., Typeform -> Webhook -> Python -> CRM). |

### Partner & Channel
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P2 | `/partner-channel-enablement-brief` | [Partner & Channel Enablement Brief Builder](partner-channel-enablement-brief.md) | Partner/Channel was a completely absent function across all prior work -- worth flagging even though it may be lower priority until... |

### GTM Strategy & Leadership
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P0 | `/gtm-audit` | [Revenue Funnel & Friction Diagnostic](gtm-audit.md) | Generating diagnostic deliverables and strategic audit decks for clients or internal leadership. |
| P1 | `/commission-plan` | [Variable Compensation & Incentive Structurer](commission-plan.md) | Designing performance-aligned compensation structures for sales and revenue teams. |
| P1 | `/gtm-motion-selector` | [GTM Motion Selector (PLG vs. Sales-Led vs. Hybrid)](gtm-motion-selector.md) | A foundational strategic decision GTM leaders make before building any of the other playbooks in this repo -- was assumed implicitly... |
| P1 | `/marketing-sales-sla-builder` | [Marketing-to-Sales SLA & Handoff Builder](marketing-sales-sla-builder.md) | This entire vault is sales/RevOps-focused with no marketing-alignment agent -- the marketing-sales handoff is one of the most common... |
| P1 | `/positioning-framework` | [Messaging & Value Prop Architect](positioning-framework.md) | Building core messaging frameworks and value propositions for new product launches or GTM campaigns. |
| P1 | `/pricing-packaging-optimizer` | [Tier & Packaging Design Optimizer](pricing-packaging-optimizer.md) | Structuring or re-structuring service/product pricing tiers for a new offer. |
| P1 | `/win-loss-analyzer` | [Deal Forensics Engine](win-loss-analyzer.md) | Extracting actionable insights from post-deal evaluations to refine sales strategy. |
| P2 | `/board-investor-narrative-builder` | [Board & Investor Revenue Narrative Builder](board-investor-narrative-builder.md) | Sales-leadership.md already covers internal forecast roll-ups; this is the external-facing narrative layer that was missing. |

### Cross-Functional/Engineering & Utility
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P1 | `/vault-health-audit` | [Vault Structural Health Auditor](vault-health-audit.md) | Catching the kind of drift this repo has already accumulated once: content merged into the repo but never linked into navigation, stale... |

### Cross-Functional / Engineering & Utility
| Priority | Command | Agent | Matches a request about... |
|---|---|---|---|
| P1 | `/agentic-workflow` | [Multi-Step Autonomous Agent Specifier](agentic-workflow.md) | Designing autonomous AI workflows for lead research, company diagnostics, or code generation. |
| P1 | `/decision` | [Strategic Trade-Off & Matrix Evaluator](decision.md) | Evaluating vendor tool choices (e.g., Clay + Apollo vs. ZoomInfo + Outreach) or build vs. buy software decisions. |
| P1 | `/mcp-server-spec` | [MCP Tool/Server Definition Writer](mcp-server-spec.md) | Specifying new MCP tools for agentic GTM workflows -- directly relevant to Peyton's own Claude/MCP-based tooling work. |
| P1 | `/python-gtm-script` | [Revenue Operations & API Automation Builder](python-gtm-script.md) | Building custom API integrations, webhook listeners, or data pipelines. |
| P2 | `/cli-tool-builder` | [Shell & Zsh Automation Architect](cli-tool-builder.md) | Building local productivity scripts and workspace tools. |
| P2 | `/goal` | [Objective-to-Task Decomposition](goal.md) | Converting high-level strategic directives into execution roadmaps. |
| P2 | `/loop` | [Recursive Iteration & Output Refinement](loop.md) | Polishing proposal angles, refining complex code scripts, or elevating strategy decks to C-suite standards. |
| P2 | `/obsidian-format` | [Note Sanitizer & Wikilink Engine](obsidian-format.md) | Normalizing session logs for direct terminal insertion into GTM-2nd-Brain or Personal-Vault. |
| P2 | `/prompt-expand` | [Meta-Prompt Engineering Engine](prompt-expand.md) | Transforming quick, conversational queries into high-yield, structured system prompts for Claude, OpenAI, or automated agents. |

## Sub-Agents (invoked BY a top-level agent, not usually called directly)
| Sub-Agent | Handles... |
|---|---|
| [Sub-Agent: Buying Committee Mapper](sub-agents/buying-committee-mapper.md) | Given known contacts on an account, map each to a MEDDPICC role (economic buyer, champion, technical evaluator, blocker) with... |
| [Sub-Agent: Competitive Intel Lookup](sub-agents/competitive-intel-lookup.md) | Given a named competitor, retrieve and synthesize the relevant profile from wiki/competitive/ (tool profile, friction/objection heatmap... |
| [Sub-Agent: Compliance/Consent Checker](sub-agents/compliance-consent-checker.md) | Given a target contact for outreach, check whether implied consent (existing business relationship) applies or express consent is required... |
| [Sub-Agent: CRM Field Writer (Protected-Field Aware)](sub-agents/crm-field-writer.md) | Given a proposed CRM field write, check it against the protected-field list (lead status, opportunity stage, lifecycle stage, and any... |
| [Sub-Agent: Deal Health Scorer](sub-agents/deal-health-scorer.md) | Apply the meddpicc_health_engine.py weighting (economic buyer 25pts, quantified ROI 15, paper process 15, quantified pain 15, decision... |
| [Sub-Agent: ICP Fit Scorer](sub-agents/icp-fit-scorer.md) | Score an account against the defined ICP's firmographic and technographic criteria, returning a Tier 1/2/3 classification with the specific... |
| [Sub-Agent: Milestone Sequencer](sub-agents/milestone-sequencer.md) | Given a set of tasks and rough phases, sequence them into a dated timeline with a named owner per milestone, flagging any milestone with no... |
| [Sub-Agent: Objection Mapper](sub-agents/objection-mapper.md) | Given a target persona or account, pull the most frequent relevant objections from the Buyer Objections Heatmap and Friction Heatmap data... |
| [Sub-Agent: Source Citation Verifier](sub-agents/source-citation-verifier.md) | Check every factual claim in the given draft for a cited source (URL, transcript timestamp, or CRM field change record). Flag any uncited... |
| [Sub-Agent: Trigger Event Detector](sub-agents/trigger-event-detector.md) | Scan available signals (funding, hiring, leadership change, regulatory change) for a given account and return the single strongest trigger... |
| [Sub-Agent: Usage Data Summarizer](sub-agents/usage-data-summarizer.md) | Condense raw product usage/telemetry data into a health-relevant summary: trend direction, adoption breadth across the buying committee,... |

## See Also
[00-Prompt-Library-Index](00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../wiki/concepts/full-org-agent-taxonomy.md) . [Sub-Agent Layer](sub-agents/00-Sub-Agent-Layer-Index.md) . [_Skill_Matrix_Hub](../../wiki/skills/_Skill_Matrix_Hub.md)
