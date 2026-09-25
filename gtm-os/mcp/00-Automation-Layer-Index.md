---
id: automation-layer-index
type: hub
tags: [hub, mcp, automation]
last_modified: 2026-09-25
confidence_score: 0.5
---

# Automation Layer Index (gtm-os/mcp/)

Real, executable implementations of the Workflow Contracts' `allowed_mcp_tools` -- as opposed to `gtm-os/agents/`, which is human-invoked prompt templates. Before 2026-09-25 this directory was empty even though all 4 contracts declared MCP tools they expected to exist (see the audit, Critical Finding #3).

## Built
- [Speed-to-Lead SLA Server](speed-to-lead/README.md) (proof of concept) -- implements [speed-to-lead-sla-contract](../contracts/speed-to-lead-sla-contract.md). 1 of 5 tools is real logic; 4 are mocked pending real CRM/calendar/Slack/sequencer credentials. Schema: I/O Schema.

## Not yet built
- [pipeline-risk-contract](../contracts/pipeline-risk-contract.md) -- `sfdc_read`, `gong_search`, `slack_notify`
- [inbound-lead-qualifier-contract](../contracts/inbound-lead-qualifier-contract.md) -- `crm_read`, `crm_write_custom_fields_only`, `clay_enrich`, `slack_notify`
- [casl-compliance-gate-contract](../contracts/casl-compliance-gate-contract.md) -- `consent_db_read`, `sequencer_read_draft`, `slack_notify` (should gate `sequencer_enqueue` calls from the speed-to-lead server once outreach automation goes live)

Recommended build order: `pipeline-risk` next (reuses the `slack_notify` pattern already proven here), then `casl-compliance-gate` (needed before `sequencer_enqueue` can safely go live for real), then `inbound-lead-qualifier`.

## See Also
index . [Workflow Contracts](../contracts/pipeline-risk-contract.md) . [00-Code-Index](../code/00-Code-Index.md)
