---
type: area
category: revops
tags:
  - area
  - take-home
  - analysis
  - method
status: active
last_updated: 2026-10-22
---

# Take-Home Analysis Method

How to run a data take-home (insights from a workbook, a dashboard, a one-page action plan) in one build pass and one review pass instead of five rebuilds. Company-neutral: all names, data and figures stay out of this file. Examples use placeholders.

## Executive Summary

The expensive part of a take-home is rework, not the first build. Rework came from four things that could have been checked before writing any prose: a classification that peeked at the future, a single large one-off charge, assumptions in the brief that the plan ignored, and numbers typed into the document by hand. The method below front-loads those checks.

## Order of work

1. **Save the brief verbatim** to `_private/takehome/assignment.md`. Note truncated or ambiguous wording. List every stated assumption (team size, regions, motion, pricing model, who owns RevOps); the plan must visibly use each one.
2. **Gap checklist before building.** One table: requirement, where it is covered, status. Re-run it at the end.
3. **Data audit (loader + quality report).** Check: duplicate IDs, zero-price rows, units of the price (monthly or annual), rows billed in one month only, the largest single line, blank segments. Write the rules in the loader docstring so a changed assumption is a one-line change.
4. **One-off test.** Any line billed in exactly one month and large relative to the account is non-recurring until shown otherwise. Exclude it from MRR, report it as a sensitivity, and put a toggle on the dashboard.
5. **Time-safe definitions.** A label may only use information available at the classification date. Labels built from the whole year favour customers who survived, which inflates gaps (for example, churn of flat-rate vs consumption accounts). Prefer a product-based label over a usage-inferred one; run the other as a sensitivity.
6. **Sensitivities on every headline** before writing: alternative definitions, with and without the largest grower, with and without the one-off, threshold variants. If a headline does not survive, lead with the part that does and call the rest directional.
7. **One script writes the numbers.** An independent recompute (pandas only, not the loader) writes `review_fixes.md`. The document quotes only figures that appear there. Never type a number from memory.
8. **Dashboard from a template.** One self-contained HTML file; filters, a what-if, a reset, a data and assumptions panel. Offline check at 1280, 375 and 320 px that default figures match step 7 and that every control works.
9. **Document.** Short. The action plan stays under one page: manageable vs hard, tools and why, partner teams, how progress is measured, a baseline and a stop rule.
10. **One skeptical review.** Hiring-manager questions table (is the effect real or an artifact, does it cause or correlate, is it driven by a few accounts, can one person run it, what if units are annual). Fix, re-run the checks, stop.

## Public-repo hygiene

- Real workbook, scripts that read it, drafts and the final PDF live in a gitignored `_private/` folder. The public repo gets the loader, a method note and tests only.
- Tests use a synthetic workbook with invented company names; never reuse names from the real data.
- No personal paths in scripts (use an environment variable with a default).
- Template the repo from this toolkit; keep company names as variables.

## Keeping token use low

- Find uploads in the session folder before asking for them again.
- Extract the brief once to markdown; do not re-parse the PDF.
- Build with a mid-size model at medium effort; use the larger model at high effort only for the review step (step 10) and the independence check (step 7).
- Reuse the loader, recompute, dashboard-template and check scripts from the last take-home instead of regenerating them; change only the definitions.
- Do the audit steps (3 to 5) before the first draft. Each late finding forced a re-base of the document, dashboard and PDF.
- Batch fixes from a review into one pass and one verification run.

## See Also
[Pipeline_Visibility_and_Hygiene.md](Pipeline_Visibility_and_Hygiene.md) . [Customer_Health_Scoring_Model.md](Customer_Health_Scoring_Model.md) . [Vendor_Benchmark_Verification.md](Vendor_Benchmark_Verification.md)
