---
type: area
category: revops
tags:
  - area
  - crm
  - migration
  - data-quality
status: active
last_updated: 2026-10-29
---

# CRM Migration Checklist

Module: `shared_core/data_quality`. A checklist for moving leads, contacts, accounts and opportunities from one CRM to another at [COMPANY_NAME], for example from [MARKETING_AUTOMATION] to [CRM] after an acquisition. Run it with the RevOps lead as co-owner. Related: [Salesforce & HubSpot sync architecture](../specs/architecture/Salesforce_HubSpot_Sync_Architecture.md), [Sync inclusion rules](../specs/architecture/Sync_Inclusion_Rules.md), [CRM Health Scoring](CRM_Health_Scoring.md) and the [CRM cleanup contract](../contracts/crm-cleanup-contract.md).

## Executive Summary

Decide what moves and what stays before touching data. Map every field. Clean and dedupe in the source or a staging area, not in the target. Load in dependency order, reconcile counts, and keep the source system until the target has been checked.

## 1. Scope

- [ ] List the objects: accounts, contacts, opportunities, leads, and any activity or custom objects.
- [ ] Record volumes per object from the source.
- [ ] **Decide what stays behind.** Example rule: leads stay in the source system unless a new event occurs, and a new event moves the lead. Write the rule and the event list down.
- [ ] Decide the history that moves (closed opportunities, activity, stage history) and the history that is archived.
- [ ] Name the owners: RevOps lead, technical owner, sales leadership approver.
- [ ] Freeze date and cutover plan agreed with sales leadership.

## 2. Field mapping

| Source object.field | Target object.field | Transform | Required in target | Owner | Notes |
|---|---|---|---|---|---|
| (one row per field) | | | | | |

- [ ] Every source field is mapped, deliberately dropped, or archived. None is left unlisted.
- [ ] Picklist values mapped one-to-one in a lookup table.
- [ ] Owner, stage, record-type and lifecycle mappings agreed with the business.
- [ ] Required target fields have a source or a default.
- [ ] Unique external IDs from the source are kept on the target record for traceability and re-runs.
- [ ] Mapping reviewed and signed off before the first load.

## 3. Dedupe and cleanup (before load)

- [ ] **Accounts:** match on domain, then normalized name; define the surviving-record rule and which fields win.
- [ ] **Contacts:** match on email; handle shared and role addresses.
- [ ] **Opportunities:** check every opportunity has an account, a valid stage, an amount and a close date.
- [ ] Standardize country, state, phone and company-name formats.
- [ ] Remove or flag records with no activity, no email, or bad data per the agreed rules.
- [ ] Keep a merge log: which records merged into which, and why.
- [ ] Respect opt-outs, consent and suppression flags; they migrate with the record.

## 4. Load

- [ ] Rehearse on a sandbox with a sample, then a full copy.
- [ ] **Order:** accounts, then contacts, then opportunities and their contact roles, then any leads that move.
- [ ] Use upsert on the external ID so a re-run does not duplicate.
- [ ] Disable automation that would fire on load (routing, emails, task creation) and re-enable after checks.
- [ ] Log every record attempted with its result.

## 5. Reconcile

- [ ] Counts per object: source, cleaned, loaded, rejected. The numbers tie out.
- [ ] Sample 50 to 100 records per object against the source, field by field `[ASSUME]` sample size.
- [ ] Total opportunity amount and stage counts match for the loaded set.
- [ ] Every account has an owner; every contact has an account where one should exist.
- [ ] Run the [data-quality monitor](../../shared_core/data_quality/dq_monitor.py) rules on the target and review the failures.

## 6. Cutover and after

- [ ] Integrations repointed (marketing automation, sequencer, forecasting, reporting) and tested.
- [ ] Reports and dashboards rebuilt on target fields and compared to the source.
- [ ] Users trained; a support channel open for the first weeks.
- [ ] Source system kept read-only until the checks above hold for the agreed period.
- [ ] Decisions, merge log and open issues written down for whoever inherits the system.
