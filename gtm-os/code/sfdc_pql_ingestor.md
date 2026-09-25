---
id: code-sfdc-pql-ingestor
type: code-index
tags: [code, revops-engineering, pql]
last_modified: 2026-09-25
---

# PQL Ingestion Engine

Companion note for `sfdc_pql_ingestor.py` -- resolves `[sfdc_pql_ingestor](sfdc_pql_ingestor.md)` wikilinks.

**Real file:** `gtm-os/code/sfdc_pql_ingestor.py`

Processes inbound product-qualified-lead (PQL) webhook payloads (`domain`, `pql_score`, `employee_count`) and gates on `employee_count >= 50 and pql_score >= 80` before routing. Supports a `dry_run` mode. Referenced by [00-Code-Index](00-Code-Index.md) as the entry point for the PQL -> CRM pipeline.

## See Also
[00-Code-Index](00-Code-Index.md) . [gtm-stack-integration-architecture](../../wiki/concepts/gtm-stack-integration-architecture.md)
