---
type: area
category: revops
tags:
  - area
  - agents
  - triggers
  - signals
status: active
last_updated: 2026-10-29
---

# Quarterly Business Report Agent: Trigger Finder (template)

Part of the [agent spec templates](README.md). Fill the bracketed fields for [COMPANY_NAME]. This agent finds triggers: events at a customer or account that give the account team a reason to act or to reach out. It is separate from the [QBR agent](qbr-agent.md), which builds the QBR presentation.

## Purpose

Scan the sources below for each account in scope and report the triggers worth a person's attention, each with its source and date.

## Trigger and cadence

Scheduled per account list (`[ASSUME]` cadence), plus on request from an account owner.

## Build pattern

Built as a workflow in [ENRICHMENT_ORCHESTRATION] (Clay in the original build) with a series of prompts.

1. **Gate on conditions.** A row runs only when its conditions are met, for example the account has been a customer for at least 6 months `[ASSUME]`.
2. **Run the prompts in series.** Together they cover the sources above and produce the output contract above.
3. **Designate one output for delivery.** One column is marked as the message to send to the account owner or user in Slack.
4. **Deliver through n8n.** The workflow calls an n8n workflow over HTTP: a POST to send the designated output, and a GET where the workflow needs to read data back. n8n posts the message to Slack.
5. **Fail closed.** If a condition, a prompt or the HTTP call fails, nothing is sent and the failure is logged for the agent owner.

## Inputs

| Source | What to look for |
|---|---|
| Annual reports (for example a 10-K) | Stated priorities, initiatives, risks, restructurings, acquisitions |
| New hires | Senior hires and role changes in the buying or user teams |
| Job postings | Roles that point to a new initiative, team or tool |
| Website visits | Visits by known accounts to pages that signal interest |
| Other signals | Anything else the team defines, each with a named source |

Only allow-listed fields from [CRM] reach the prompt. Outside content (filings, postings, web pages) is data, never instructions to the agent.

## Output contract

```json
{
  "account_id": "",
  "triggers": [
    {"type": "annual_report|new_hire|job_posting|website_visit|other",
     "summary": "", "source_url": "", "source_date": "", "why_it_matters": "", "suggested_action": ""}
  ],
  "no_triggers_found": false
}
```

Every trigger carries a source URL and a date. A trigger without both is rejected.

## Verification

- Confirm each claim at the account's own source (its filing, its careers page), not at a third-party summary.
- Check that the posting, hire or filing belongs to this company and not a similarly named one.
- Mark anything that cannot be confirmed as unverified, and keep it out of outreach.

## HITL policy

The account owner or user receives the designated output in Slack, reviews each trigger and decides whether to act. The agent writes nothing to [CRM] and contacts no customer or prospect. If the review step cannot run, nothing is delivered.

## Evals

- Human-written reference trigger reports for a set of accounts, including accounts with no triggers.
- Checks: every trigger has a source and date, no trigger comes from another company, accounts with nothing new return `no_triggers_found`.
- Re-run the test set after every prompt change. See the [Agent Eval Checklist](../../../playbooks/Agent_Eval_Checklist.md).

## Impact metric

Triggers reviewed per cycle and the share the account owner acted on, baselined before launch.

## Stop rule

Pause the agent if a delivered trigger turns out to belong to the wrong company or to have no source; log it and notify the agent owner.
