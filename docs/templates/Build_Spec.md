# Build Spec

One page per build. Copy it, name it after the build, and keep it next to the code or config it describes.

| Field | Value |
|---|---|
| Status | Draft |
| Version | v0.1 |
| Release date | |

## Problem
Who hurts, how often, and the evidence.

## Users

## Success metric
Baseline, target, and where it's measured.

## Scope and not in scope

## Design
Systems, objects and fields touched; automation or agent.

## Controls
- Autonomous agent? Apply the [AI Workflow Standard](../../shared_core/ai_governance/README.md) and test it with the [Agent Eval Checklist](../playbooks/Agent_Eval_Checklist.md).
- Touches price, terms, quotes, billing, credits or customer commitments? Then all four must hold:
  1. Each action has a named source of authority, recorded in a system.
  2. Authorization is enforced in the downstream system (CPQ, billing, a [CRM] validation rule), not by the model. External text, such as an email saying a discount is approved, never creates an approval.
  3. Facts the agent acts on carry provenance: customer statement, rep judgment, executed agreement or payment confirmation. One kind is never promoted into another.
  4. A named person can pause the process, with a restore path and someone who reconciles affected transactions.

## Rollout and rollback

## Release note (to the field, 3 lines max)
- What changed: 
- What you do differently: 
- Who to ask: 

## Value ledger
| Metric | Baseline | After 30 days |
|---|---|---|
| | | |
