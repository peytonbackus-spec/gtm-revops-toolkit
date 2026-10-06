# GTM & RevOps Toolkit (template)

A config-driven GTM engineering and RevOps toolkit, built to be copied. One YAML file describes a company; every script, SQL model, prompt and spec reads from it. Runs end to end on synthetic data with no network and no API key.

```bash
pip install -r requirements.txt
make data demo test
```

## Start a new company repo

```bash
make new COMPANY="Acme Corp" FY_START=1      # or: python scripts/new_company.py "Acme Corp" --dest ~/work/acme
```

This copies the template (never private material), writes `config/company.yaml`, resolves the `[VARIABLE]` tokens in docs, and generates `VARIABLES.md` and a README. See `docs/overview/new-company-repo.md`.

## Layout

| Path | What it holds |
|---|---|
| `config/example.yaml` | The one config: segments, personas, scoring, routing, stages, SLAs, quota, fiscal calendar, stack |
| `shared_core/` | Config loader, schemas, metrics SQL semantic layer, data-quality monitor, AI governance (HITL, PII guard, eval harness, mock LLM) |
| `gtm_engineer/` | Lead to opportunity: scoring, routing, lifecycle SLAs, funnel, SDR capacity, enrichment waterfall, L2A matcher, AI account research |
| `gtm_strategy_ops/` | Opportunity to renewal: pipeline, forecast accuracy, renewals, closed-lost, AI deal risk |
| `prototypes/` | Earlier standalone engines (MEDDPICC health, churn, PQL ingestion, tech debt) kept for reference |
| `sample_data/`, `scripts/` | Synthetic CSVs and the generator that keeps them in step with the config |
| `tests/`, `evals/` | Unit tests and prompt evals |
| `docs/` | Overview, specs, playbooks, examples |

Config resolution: `$GTM_CONFIG`, then `config/company.yaml`, then `config/example.yaml`.

## Principles

Synthetic data only. LLM calls are mocked by default (`GTM_LLM_MODE=anthropic` for live). Humans approve AI output before it touches a record. PII is redacted before any model call. Assumptions are tagged `[ASSUME]` until sourced.

Keep strategy, financials, prospect lists and client notes out of this repo; they belong in a private vault.
