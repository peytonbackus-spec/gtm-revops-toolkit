# Universal Variable Substitution Guide — GTM & RevOps Toolkit

This repository is designed as a company-agnostic, modular GTM Operating System template. Substitute the bracketed variables below across the Markdown frameworks, Python scripts, and SQL schemas to customize for any target company.

| Variable Tag | Description | Example Values |
| :--- | :--- | :--- |
| `[COMPANY_NAME]` | Target enterprise or client organization | ACME Corp, SaaS Corp |
| `[TARGET_BUYER_PERSONA]` | Core decision maker titles | VP Engineering, CFO, Head of RevOps |
| `[PRIMARY_PRODUCT_SUITE]` | Core software or service offering | Enterprise Analytics, Predictive Maintenance |
| `[PRIMARY_PARTNER_ECOSYSTEM]` | Primary OEM or channel integration | Salesforce, AWS, Siemens |
| `[ACV_RANGE]` | Average Contract Value brackets | $50k - $150k ARR |
| `[SALES_CYCLE_LENGTH]` | Standard conversion timeline | 60 - 90 Days |
| `[PRIMARY_SIGNAL_TRIGGERS]` | Intent and enrichment triggers | Executive hires, Job posts, FX Volatility |

## Where This Is Used

These tags appear directly in the System Prompt of the agents below, so running one only requires filling in the bracketed values -- no rewriting the prompt itself:

- [`gtm-os/agents/icp-builder.md`](gtm-os/agents/icp-builder.md)
- [`gtm-os/agents/positioning-framework.md`](gtm-os/agents/positioning-framework.md)
- [`gtm-os/agents/competitive-battlecard.md`](gtm-os/agents/competitive-battlecard.md)
- [`gtm-os/agents/gtm-motion-selector.md`](gtm-os/agents/gtm-motion-selector.md)
- [`gtm-os/agents/pricing-packaging-optimizer.md`](gtm-os/agents/pricing-packaging-optimizer.md)

Any other agent in [`gtm-os/agents/`](gtm-os/agents/) can adopt the same tags as it's extended -- these five are the ones with a System Prompt built to consume them directly today.

## Worked Example

Filling in the table for a hypothetical mid-market target, "Northwind Analytics" (a supply-chain intelligence SaaS vendor):

| Variable Tag | Filled Value |
| :--- | :--- |
| `[COMPANY_NAME]` | Northwind Analytics |
| `[TARGET_BUYER_PERSONA]` | VP Supply Chain Operations, Director of RevOps |
| `[PRIMARY_PRODUCT_SUITE]` | Supply Chain Intelligence Platform |
| `[PRIMARY_PARTNER_ECOSYSTEM]` | NetSuite, SAP |
| `[ACV_RANGE]` | $40k - $120k ARR |
| `[SALES_CYCLE_LENGTH]` | 45 - 75 Days |
| `[PRIMARY_SIGNAL_TRIGGERS]` | ERP migration announcements, new VP Supply Chain hires, warehouse expansion press releases |

Dropped into [`gtm-os/agents/gtm-motion-selector.md`](gtm-os/agents/gtm-motion-selector.md)'s System Prompt, the generic "the product's price point, buyer complexity, and time-to-value" becomes a concrete ask: *"Given Northwind Analytics' $40k-$120k ARR price point, a VP Supply Chain Operations / Director of RevOps buying committee, and a 45-75 day sales cycle, recommend a primary GTM motion..."* -- the same prompt, now scoped to an actual deal instead of an abstraction.
