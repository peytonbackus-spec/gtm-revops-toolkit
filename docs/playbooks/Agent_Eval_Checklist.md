---
type: area
category: revops
tags:
  - area
  - evals
  - ai-governance
status: active
last_updated: 2026-10-29
---

# Agent Eval Checklist

Module: `shared_core/ai_governance`. Practical checklist for any agent that writes text a person will read or act on at [COMPANY_NAME]. Complements the [AI evaluation framework](../specs/gtm-engineering/ai_eval_framework.md) and the harness in [`eval_harness.py`](../../shared_core/ai_governance/eval_harness.py). The agent specs it applies to are in [agent-specs](../specs/gtm-engineering/agent-specs/README.md).

## Executive Summary

Write the right answer by hand first. Test every prompt change against those answers. Put a person between the agent and the reader. Log what went wrong and what you decided. Then tailor the output to the reader, because a correct output in the wrong shape still gets ignored.

## Before launch

- [ ] **Human-written reference outputs.** For each agent, a person writes the outputs they would be proud to send, covering language and tone as well as facts. Cover each segment and edge case the agent will meet.
- [ ] **Test set.** The reference cases are saved as fixed inputs with expected checks (`*/evals/*.json`). Add a case whenever a real failure turns up.
- [ ] **Checks that can fail.** Each case has at least one hard check (required keys present, every number has a source tag, length within the channel limit) and, where judgment is needed, a reviewer rubric.
- [ ] **Output contract.** Responses missing required keys are rejected, not patched.
- [ ] **Data boundary.** Only allow-listed fields reach the prompt; PII is redacted first.
- [ ] **Baseline.** The impact metric is measured before launch, so the result can be compared.
- [ ] **Named reviewer.** Every agent has a person who reviews its output before delivery, and a named owner for the agent itself.

## On every prompt change

- [ ] **Re-run the full test set.** A change that fixes one case must not break another.
- [ ] **Compare to the last passing run,** case by case, not only the pass rate.
- [ ] **Version the prompt** and record the version with each output.
- [ ] **Roll back** if a hard check regresses.

## Before delivery (every output)

- [ ] **Human review before delivery.** The reviewer accepts, edits or rejects. Nothing reaches a customer, a record or a channel unreviewed.
- [ ] **Fail closed.** If the review or a guarding check cannot run, the output waits.
- [ ] **Sources visible.** The reviewer can see where each figure came from.

## After delivery

- [ ] **Log errors and decisions.** Keep one log where the team will find it: what went wrong, what was decided, what changed in the prompt or the rules. Date each entry.
- [ ] **Track rework.** Count edits and rejections by reason. A repeated reason is a prompt or contract change, not a reminder to reviewers. Typical reworks: a channel character limit that the output exceeded, or a send frequency that was too high for the reader.
- [ ] **Review a sample** even when nothing looks wrong.
- [ ] **Promote autonomy only from the log** ([earned autonomy](../../shared_core/ai_governance/earned-autonomy.md)).

## Tailor to the reader

- [ ] **Per-reader style.** Keep a short profile for each person who receives agent output: preferred length, tone, level of detail, and how often they want to hear from the agent.
- [ ] **Apply it in the prompt,** not in a post-edit, and include profile cases in the test set.
- [ ] **Let the reader correct it.** Rework from a person feeds back into their profile.
- [ ] **Channel rules are contract rules.** A character limit or formatting rule belongs in the output contract and in a hard check.

## Stop rule

Name what pauses the agent (for example an unsourced number reaching a customer) and who is notified. Write it down before launch.
