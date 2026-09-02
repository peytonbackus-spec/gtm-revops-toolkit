# GTM & RevOps Infrastructure Toolkit

A production-grade toolkit of specifications, Python scoring engines, evaluation frameworks, and workflow automation templates designed for modern GTM Engineering, AI-native revenue operations, and sales ops teams.

---

## 🛠️ Module Overview

| Category | Module Directory | Key Capabilities |
| :--- | :--- | :--- |
| **GTM Engineering** | `modules/gtm_engineering/ai_agents/` | Workflow orchestration, Clay enrichments, API tool calling |
| **Deal Scoring** | `modules/gtm_engineering/deal_scoring/` | Algorithmic deal-risk & pipeline-health evaluation (`pipeline_health_model.py`) |
| **AI Evals & Guardrails** | `modules/gtm_engineering/evaluation_guardrails/` | Observability, data privacy, and Human-in-the-Loop (HITL) specs |
| **RFP Automation** | `modules/gtm_engineering/rfp_automation/` | Vector retrieval architecture for automated security & technical RFPs |
| **SalesOps & Planning** | `modules/salesops/capacity_planning/` | Funnel modeling, capacity planning, and headcount performance tracking |

---

## 📂 Directory Architecture

```text
gtm-revops-toolkit/
├── modules/
│   ├── gtm_engineering/
│   │   ├── ai_agents/
│   │   │   └── agent_orchestration_spec.md
│   │   ├── deal_scoring/
│   │   │   └── pipeline_health_model.py
│   │   ├── evaluation_guardrails/
│   │   │   └── ai_eval_framework.md
│   │   └── rfp_automation/
│   │       └── rfp_pipeline_spec.md
│   └── salesops/
│       └── capacity_planning/
└── templates/
    └── architecture_diagrams/
```

---

## 🚀 Getting Started

```bash
# Clone repository
git clone https://github.com/peytonbackus-spec/gtm-revops-toolkit.git
cd gtm-revops-toolkit

# Run deal health scoring model example
python3 modules/gtm_engineering/deal_scoring/pipeline_health_model.py
```
