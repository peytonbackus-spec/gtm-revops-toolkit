# GTM RevOps Toolkit

An end-to-end framework for revenue architecture, enterprise deal
orchestration, AI-driven lead routing, and MEDDPICC validation.
Also contains the complete business planning documents for the
consulting firm built on top of this toolkit.

## Architecture Overview

```
[Inbound Webhooks / Product Events]
                │
                ▼
 ┌─────────────────────────────┐
 │ PQL & Enrichment Pipeline    │ ── (Apollo / L2A Matching)
 └──────────────┬──────────────┘
                │
                ▼
 ┌─────────────────────────────┐
 │ MEDDPICC Scoring & Health    │ ── (SFDC REST API / Validation Rules)
 └──────────────┬──────────────┘
                │
                ▼
 ┌─────────────────────────────┐
 │ Revenue Intelligence & Risk │ ── (Attribution & Churn Models)
 └─────────────────────────────┘
```

## Repository Structure

| Folder | Contents |
|--------|----------|
| `00_Meta/` | Templates and system config |
| `00_System/` | System-level documentation |
| `10_Projects/` | Active project files |
| `20_Areas/` | RevOps specs, architectures, field definitions |
| `30_Resources/` | Code: orchestrators, scoring, attribution |
| `50_Business/` | Business planning, GTM strategy, execution roadmap |
| `Audits/` | Client audit templates |
| `Inbound/` | Inbound pipeline configurations |
| `Scripts/` | Utility scripts |
| `Signals/` | Buying signal definitions and scoring |
| `Templates/` | Reusable templates |

## Quick Start (Toolkit)

```bash
# Install dependencies
pip install -r requirements.txt

# Execute PQL Ingestion (Dry-run mode)
python3 30_Resources/Code/sfdc_pql_ingestor.py
```

## Business Planning (`50_Business/`)

The `50_Business/` folder contains the full business strategy and
execution plan for the Autonomous AI GTM Consulting firm. See
[`50_Business/README.md`](50_Business/README.md) for details.

