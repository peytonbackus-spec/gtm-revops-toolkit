# Enterprise GTM & RevOps Engineering Toolkit

An end-to-end framework for revenue architecture, enterprise deal orchestration, AI-driven lead routing, and MEDDPICC validation.

## 🏗️ Architecture Overview

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

## 📦 Directory Structure

- `20_Areas/RevOpp/Specs/`: Technical field specifications & SFDC validation rules.
- `20_Areas/RevOpp/Architectures/`: Multi-touch attribution and deal routing diagrams.
- `30_Resources/Code/orchestrators/`: Multi-agent pipeline triggers and Webhook handlers.
- `30_Resources/Code/scoring/`: Automated MEDDPICC qualification and PQL engines.
- `30_Resources/Code/attribution/`: SQL & Python scripts for W-shaped attribution modelling.

## 🚀 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Execute PQL Ingestion (Dry-run mode)
python3 30_Resources/Code/sfdc_pql_ingestor.py
```
