# Changelog

## 0.4.2
- SQL: current fiscal quarter and as-of date now come from config ({{CURRENT_FISCAL_QUARTER}}, {{AS_OF}}) instead of being hardcoded.
- Scaffold: generated repos no longer carry the scaffold test (it failed once the scaffolder removed itself) or the template-only how-to page.
- CI: pinned ruff to an explicit rule set (newer ruff defaults had turned on 100+ style rules); fixed the real findings, including an undefined-name bug in a prototype prompt.
- Sample data: forecast quarters are now labelled from the configured fiscal calendar, so calendar-year companies get correct labels.

## 0.4.1
- README rewritten: role colour system, lifecycle and template diagrams, config map, AI governance summary.

## 0.4.0 (template restructure)
- Single config (`config/example.yaml`) drives scoring, routing, SQL fiscal calendar, prompts and sample data.
- Shared core plus two role tracks (GTM Engineer, Strategy & Ops); earlier engines folded in or moved to `prototypes/`.
- `scripts/new_company.py` / `make new` scaffold a company repo.
- Private material moved out to a separate private vault; history-purge script provided.
