---
id: sub-agent-layer
type: hub
tags: [hub, sub-agent-layer]
last_modified: 2026-09-25
confidence_score: 0.45
---

# Sub-Agent Layer

11 shared, single-purpose sub-agents that multiple top-level agents call, instead of each top-level agent re-deriving the same logic. This mirrors the role_map pattern already used in [pipeline-risk-contract](../../contracts/pipeline-risk-contract.md) (its `data_audit_agent` and `synthesis_agent` are exactly this pattern, just not yet generalized).

## Reuse Map (sub-agent -> how many parents call it)
- [Usage Data Summarizer](usage-data-summarizer.md) -- called by 5: account-brief-generator, qbr-builder, expansion-upsell-play-builder, renewal-playbook, escalation-runbook
- [Competitive Intel Lookup](competitive-intel-lookup.md) -- called by 5: account-brief-generator, competitive-battlecard, rfp-proposal-generator, positioning-framework, prospect-stack-gap-finder
- [ICP Fit Scorer](icp-fit-scorer.md) -- called by 5: icp-builder, lead-scoring, inbound-lead-qualifier, prospect-stack-gap-finder, account-research-brief
- [Buying Committee Mapper](buying-committee-mapper.md) -- called by 4: account-brief-generator, mutual-close-plan-builder, demo-narrative-architect, poc-pilot-success-plan-builder
- [Deal Health Scorer](deal-health-scorer.md) -- called by 4: forecast-rollup, mutual-close-plan-builder, account-brief-generator, win-loss-analyzer
- [Source Citation Verifier](source-citation-verifier.md) -- called by 4: account-research-brief, win-loss-analyzer, rfp-proposal-generator, inbound-lead-qualifier
- [Objection Mapper](objection-mapper.md) -- called by 4: cold-call-script, competitive-battlecard, sequence-builder, positioning-framework
- [Milestone Sequencer](milestone-sequencer.md) -- called by 4: customer-onboarding-playbook-builder, mutual-close-plan-builder, renewal-playbook, poc-pilot-success-plan-builder
- [CRM Field Writer (Protected-Field Aware)](crm-field-writer.md) -- called by 3: crm-hygiene-auto-updater, inbound-lead-qualifier, clay-waterfall
- [Compliance/Consent Checker](compliance-consent-checker.md) -- called by 3: casl-cold-outreach-compliance-checker, sequence-builder, account-research-brief
- [Trigger Event Detector](trigger-event-detector.md) -- called by 3: account-research-brief, win-back-reactivation-sequence-builder, icp-builder

## When a Sub-Agent Should Become Part of a Real Workflow Contract
If any parent agent above is promoted from a human-invoked prompt to an autonomous `gtm-os/contracts/` Workflow Contract (see [full-org-agent-taxonomy](../../../wiki/concepts/full-org-agent-taxonomy.md)'s recommendation to promote `/inbound-lead-qualifier` and `/speed-to-lead-sla-enforcer` first), the sub-agents it calls belong in that contract's `role_map`, exactly as `pipeline-risk-contract.yaml` already splits its work into `data_audit_agent` and `synthesis_agent`.

## See Also
[00-Prompt-Library-Index](../00-Prompt-Library-Index.md) . [full-org-agent-taxonomy](../../../wiki/concepts/full-org-agent-taxonomy.md) . [pipeline-risk-contract](../../contracts/pipeline-risk-contract.md)