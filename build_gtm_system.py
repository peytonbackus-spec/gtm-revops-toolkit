import os
import re
import argparse
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, List


def setup_templates(vault_path: str):
    templates_dir = os.path.join(vault_path, "Templates")
    os.makedirs(templates_dir, exist_ok=True)

    templates = {
        "tpl_signal.md": "---\ntype: intent_signal\ncompany: \"{{company}}\"\ndomain: \"{{domain}}\"\nsignal_type: \"{{signal_type}}\"\nsource: \"{{source}}\"\nimpact_score: {{impact_score}}\nheadcount: {{headcount}}\nfunding_stage: \"{{funding_stage}}\"\ncreated_date: {{created_date}}\ntags:\n  - gtm/signal\n  - intelligence/account\n---\n\n# Intent Signal: {{company}} - {{signal_type}}\n\n## Account Intelligence\n- **Company:** {{company}} (`{{domain}}`)\n- **Headcount:** {{headcount}}\n- **Funding Stage:** {{funding_stage}}\n- **Tech Stack:** {{tech_stack}}\n- **Trigger:** `{{signal_type}}` (Impact: `{{impact_score}}/10`)\n\n## Detected Raw Signal\n> {{raw_text}}\n\n---\n\n## Actionable Strategy\n{{gtm_angle}}\n\n- [ ] Route signal trigger to account owner\n- [ ] Trigger sequence customized to {{tech_stack}}\n"
    }

    for name, content in templates.items():
        filepath = os.path.join(templates_dir, name)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


def validate_and_render(template_name: str, template_str: str, context: Dict[str, Any]) -> str:
    required_vars = set(re.findall(r"\{\{\s*(\w+)\s*\}\}", template_str))
    provided_vars = set(context.keys())

    missing_vars = required_vars - provided_vars
    if missing_vars:
        raise KeyError(
            f"[Schema Violation] Template '{template_name}' missing required keys: {missing_vars}"
        )

    rendered = template_str
    for k, v in context.items():
        rendered = rendered.replace(f"{{{{{k}}}}}", str(v if v is not None else ""))
    return rendered


class AccountEnricher:
    @staticmethod
    def enrich_domain(domain: str) -> Dict[str, Any]:
        return {
            "headcount": 350,
            "funding_stage": "Series C",
            "tech_stack": "Salesforce, Outreach, Gong, Snowflake"
        }


@dataclass
class IntentSignal:
    company_name: str
    domain: str
    signal_type: str
    source: str
    raw_text: str
    impact_score: int


class SignalCaptureEngine:
    def __init__(self, vault_path: str):
        self.vault_path = vault_path
        self.templates_dir = os.path.join(vault_path, "Templates")

    def load_template(self, template_file: str) -> str:
        path = os.path.join(self.templates_dir, template_file)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def process_signal(self, signal: IntentSignal) -> str:
        template_raw = self.load_template("tpl_signal.md")
        enrichment = AccountEnricher.enrich_domain(signal.domain)

        context = {
            "company": signal.company_name,
            "domain": signal.domain,
            "signal_type": signal.signal_type,
            "source": signal.source,
            "raw_text": signal.raw_text,
            "impact_score": signal.impact_score,
            "headcount": enrichment["headcount"],
            "funding_stage": enrichment["funding_stage"],
            "tech_stack": enrichment["tech_stack"],
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "gtm_angle": f"Reach out to RevOps leadership at {signal.company_name} regarding their recent {signal.signal_type}. Tailor message around their {enrichment['tech_stack']} stack."
        }

        rendered_md = validate_and_render("tpl_signal.md", template_raw, context)

        out_dir = os.path.join(self.vault_path, "Signals")
        os.makedirs(out_dir, exist_ok=True)
        filename = f"{context['created_date']}_Signal_{context['company'].replace(' ', '_')}.md"
        filepath = os.path.join(out_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(rendered_md)
        return filepath


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture and process GTM Intent Signals directly into Obsidian.")
    parser.add_argument("--company", type=str, default="Aperture Labs", help="Company Name")
    parser.add_argument("--domain", type=str, default="aperturelabs.com", help="Company Domain")
    parser.add_argument("--type", type=str, default="VP RevOps Hire", help="Signal Trigger Type")
    parser.add_argument("--source", type=str, default="LinkedIn Jobs", help="Signal Data Source")
    parser.add_argument("--raw", type=str, default="Hired former VP of Operations to lead revenue automation team.", help="Raw Text")
    parser.add_argument("--impact", type=int, default=9, help="Impact Score (1-10)")

    args = parser.parse_args()
    vault_path = os.getcwd()
    setup_templates(vault_path)

    sig_engine = SignalCaptureEngine(vault_path)
    s_path = sig_engine.process_signal(IntentSignal(
        company_name=args.company,
        domain=args.domain,
        signal_type=args.type,
        source=args.source,
        raw_text=args.raw,
        impact_score=args.impact
    ))
    print(f" [✓] Signal Captured: {s_path}")
