import os
import sys
import json
from datetime import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: 'anthropic' package required. Install via: pip install anthropic")
    sys.exit(1)

MODEL_NAME = "claude-3-5-sonnet-20241022"
DEFAULT_VAULT_PATH = Path("/Users/peytonbackus/GTM 2nd Brain")

SYSTEM_PROMPT = """You are an elite GTM Engineering and RevOps Executive Assistant.
Analyze raw revenue, sales pipeline, and outbound metrics for B2B SaaS leadership.
Generate a concise, high-impact Markdown report formatted for Obsidian notes.

Guidelines:
1. Include an 'Executive Summary' with top-line wins and critical risks.
2. Provide a 'Pipeline Metrics Breakdown' table (Stage, Deal Count, Total Value).
3. Highlight 'Outbound & Signal Performance' (Emails Sent, Open/Reply Rates, Meetings Booked).
4. Outline 'Recommended Action Items' (3-5 concrete steps for the upcoming week).
5. Output pure Markdown with no conversational intro or outro.
"""

def generate_digest(metrics_data: dict) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set.")

    client = anthropic.Anthropic(api_key=api_key)
    user_prompt = f"Generate an executive GTM report based on the following raw weekly data:\n\n{json.dumps(metrics_data, indent=2)}"

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1500,
        temperature=0.2,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.content[0].text

def save_digest_to_vault(markdown_content: str, vault_dir: Path, client_name: str = "Internal") -> Path:
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_dir = vault_dir / "10_Projects" / "Deal_Reviews"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = output_dir / f"{date_str}_GTM_Digest_{client_name.replace(' ', '_')}.md"
    header = f"---\ntags:\n  - gtm/reporting\n  - revops/digest\ndate: {date_str}\nclient: {client_name}\n---\n\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + markdown_content)
        
    return file_path

if __name__ == "__main__":
    sample_metrics = {
        "period": "Week of Aug 24 - Aug 28, 2026",
        "client_name": "Acme Corp",
        "summary": {
            "new_pipeline_added": "$125,000",
            "closed_won": "$35,000",
            "active_opportunities": 14
        },
        "pipeline_stages": [
            {"stage": "Discovery Booked", "count": 6, "value": "$45,000"},
            {"stage": "Audit / Proposal Sent", "count": 5, "value": "$65,000"},
            {"stage": "Negotiation / Legal", "count": 3, "value": "$50,000"}
        ],
        "outbound_signals": {
            "signals_captured": 42,
            "prospects_enriched_clay": 180,
            "emails_sent": 450,
            "open_rate": "64%",
            "reply_rate": "8.2%",
            "meetings_booked": 4
        },
        "blockers": [
            "Legal delay on Acme Corp Enterprise renewal terms.",
            "HubSpot API sync error on custom lead scoring property."
        ]
    }

    print("Generating GTM Pipeline Digest via Claude API...")
    try:
        digest_md = generate_digest(sample_metrics)
        output_file = save_digest_to_vault(digest_md, DEFAULT_VAULT_PATH, sample_metrics["client_name"])
        print(f"Success! Digest written to: {output_file}")
    except Exception as e:
        print(f"Error generating digest: {e}")
