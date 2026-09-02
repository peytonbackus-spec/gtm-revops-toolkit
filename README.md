# GTM & RevOps Infrastructure Toolkit

A production-grade toolkit of specifications, Python scoring engines, evaluation frameworks, and workflow automation templates designed for modern GTM Engineering, AI-native revenue operations, and sales ops teams.

---

## 🏗️ Architecture Overview

<details>
<summary><b>View Interactive Mermaid Architecture Diagram</b></summary>

```mermaid
flowchart TD
    subgraph Ingestion ["1. Signal Ingestion & Webhooks"]
        A[Inbound Webhooks / Web Activity]
        B[6sense / Intent Data]
        C[CRM Event Triggers]
    end

    subgraph Enrichment ["2. PQL & Enrichment Engine"]
        D[Clay Waterfall Enrichment]
        E[Domain & ICP Matcher]
    end

    subgraph Scoring ["3. Scoring & Risk Engine"]
        F[Pipeline Health Model]
        G[MEDDPICC & Deal Scoring]
    end

    subgraph Action ["4. Action Execution & Workflows"]
        H[Outreach / Sales Execution]
        I[Slack / Teams Real-time Alerts]
        J[RFP Vector RAG Service]
    end

    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    G --> I
    G --> J
```

</details>

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
        └── gtm_revops_architecture.png
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
