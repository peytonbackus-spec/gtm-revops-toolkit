---
type: area
category: revops
tags:
  - area
  - sync
  - product-usage
  - crm
  - n8n
status: active
last_updated: 2026-10-29
---

# Usage-to-CRM Sync Pattern

Module: `docs/specs/architecture`. A design pattern for moving product-usage data from the warehouse or product database into [CRM] at [COMPANY_NAME] so account teams can act on it. It is a pattern document, not a deployed implementation in this repo. Related: [Salesforce & HubSpot sync architecture](Salesforce_HubSpot_Sync_Architecture.md), [Sync inclusion rules](Sync_Inclusion_Rules.md), and the PQL logic in [`sfdc_pql_ingestor.py`](../../../prototypes/sfdc_pql_ingestor.py).

## Executive Summary

Compute usage metrics in the warehouse. Push a small, named set of them to [CRM] on a schedule, matched to the right account or contact, through the CRM API or a low-code tool such as n8n. Check data quality before every write, and never overwrite a field a person owns.

## Flow

```
Product DB / warehouse  ->  usage model (SQL view)  ->  extract (scheduled)
   ->  match to CRM record  ->  data-quality checks  ->  write via API or n8n
   ->  reconcile and log
```

## 1. Choose the metrics

- Sync only metrics a person or a rule will act on (a health score input, a PQL trigger, a renewal signal). If no report or automation reads a field, do not create it.
- Prefer aggregates and trends (30-day active users, percent change, utilization) over event-level data.
- Each metric has a definition, an owner and a refresh cadence in [`metric-definitions.md`](../../../shared_core/metrics/metric-definitions.md).

## 2. Field mapping

Keep the mapping in a reviewed table, versioned with the code.

| Warehouse field | Grain | CRM object and field | Type | Direction | Refresh | Overwrite rule |
|---|---|---|---|---|---|---|
| `active_users_30d` | Account | Account.`Active_Users_30d__c` | Number | Warehouse to CRM | Daily | Always overwrite (system-owned) |
| `usage_trend_pct` | Account | Account.`Usage_Trend_Pct__c` | Percent | Warehouse to CRM | Daily | Always overwrite |
| `last_active_at` | Contact | Contact.`Last_Product_Activity__c` | Datetime | Warehouse to CRM | Daily | Only if newer |
| `pql_flag` | Contact | Contact.`PQL__c` | Boolean | Warehouse to CRM | Hourly | Set; clearing needs an owner review |

Field names above are examples. Rules:
- System-owned fields are prefixed or grouped so people know not to edit them.
- A field a person edits is never overwritten without a rule that says so.
- Units, time zones and null handling are written in the mapping, not assumed.

## 3. Matching and dedupe

1. **Key** each usage row with a stable ID from the product (account ID, user ID).
2. **Match** to [CRM] in order: stored external ID, then verified email domain for accounts, then exact email for contacts. Fuzzy matching only produces candidates for review, never a write.
3. **Store the external ID** on the [CRM] record once a match is confirmed, so later runs do not rematch.
4. **Unmatched rows** go to a review queue, with a reason, and are never created blindly as new records.
5. **Duplicates:** if one usage row matches more than one [CRM] record, write to none and queue it. If several usage rows map to one record, aggregate first.
6. **Idempotent writes:** use upsert on the external ID so a re-run does not create duplicates.

## 4. Data-quality checks (before every write)

- [ ] **Freshness:** the source view was refreshed within the expected window; otherwise skip the run and alert.
- [ ] **Volume:** row count is within the usual range of the last runs; a large drop or spike stops the run.
- [ ] **Nulls and types:** required keys present, values numeric where numeric, percentages within range.
- [ ] **Match rate:** the share of rows matched to a record is above the floor `[ASSUME]`; below it, hold the run.
- [ ] **Change size:** the number of fields about to change is within the usual range.
- [ ] **Dry run:** the first run of any new mapping writes a diff to a file, not to [CRM].
- [ ] **Fail closed:** if a check cannot run, nothing is written.

## 5. Write path

| Option | Use when | Watch for |
|---|---|---|
| CRM bulk or REST API from a scheduled job | Many records, versioned code, tests | API limits, retries, partial failures |
| n8n workflow (schedule or webhook, then CRM node) | Few fields, quick change, low-code ownership | Keep the mapping in one node, add an error branch and an alert |
| Reverse-ETL tool | Many syncs managed centrally | Cost and mapping review process |

Always: batch the writes, retry with backoff, log each attempted record, and stop on repeated failures.

## 6. Reconcile and log

- Each run records source rows, matched, written, skipped and errored, with reasons.
- A weekly spot check compares a sample of [CRM] values with the warehouse.
- Errors and decisions are logged where the team will find them.
- Alert the owner on a failed run, a low match rate or a stale source.

## Where it plugs in

- Health scoring: [Customer Health Scoring Model](../../playbooks/Customer_Health_Scoring_Model.md).
- PQL routing: [PLG PQL routing](../lead-management/PLG_PQL_Routing.md).
- Write governance: [field and agent write governance](../../../shared_core/data_quality/field-and-agent-write-governance.md).
