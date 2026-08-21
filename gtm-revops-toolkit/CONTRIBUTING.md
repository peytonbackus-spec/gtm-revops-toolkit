# RevOps & GTM Architecture Contribution Guidelines

To maintain production standards across our revenue engine, all additions to this repository must follow these standards:

## 📐 SQL Models (`/attribution`, `/dashboards`)
* Must compile with **dbt** (data build tool) formatting standards.
* Always handle division-by-zero errors using `NULLIF`.
* Include model materialization metadata tags.

## ⚡ Automations (`/automation`)
* Webhook endpoints must be stateless and handle rate limits gracefully.
* Secrets (API Keys, Bearer tokens) **must** be stored in environment variables, never hardcoded.

## 📊 Dashboard Schemas (`/dashboards`)
* Metric definitions must follow standard SaaS formulas (e.g., NRR, ARR Waterfall, Pipeline Multiples).
