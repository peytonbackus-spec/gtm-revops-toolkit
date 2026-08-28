import os
import json
import dataclasses
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclasses.dataclass
class LeadProfile:
    first_name: str
    last_name: str
    company_name: str
    title: str
    employee_count: int
    tech_stack: List[str]
    recent_funding: bool
    hiring_roles: List[str]

class OutboundSkillEngine:
    @staticmethod
    def score_icp_fit(lead: LeadProfile) -> Dict[str, Any]:
        score = 0
        reasons = []
        if 50 <= lead.employee_count <= 500:
            score += 40
            reasons.append("Mid-market headcount fits ideal target")
        if lead.recent_funding:
            score += 30
            reasons.append("Recent funding indicates active budget")
        target_skills = ["Salesforce", "HubSpot", "Outreach", "Marketo"]
        matched_tech = [t for t in lead.tech_stack if t in target_skills]
        if matched_tech:
            score += 30
            reasons.append("Matching tech stack: " + ", ".join(matched_tech))
        return {"icp_score": score, "qualified": score >= 70, "fit_reasons": reasons}

    @staticmethod
    def generate_copy(lead: LeadProfile, icp_eval: Dict[str, Any]) -> Dict[str, str]:
        trigger = lead.hiring_roles[0] if lead.hiring_roles else "growth targets"
        primary_tech = lead.tech_stack[0] if lead.tech_stack else "your tech stack"
        tech_list = ", ".join(lead.tech_stack[:2])
        subject = f"Quick question re: {lead.company_name}'s {trigger}"
        body = (
            f"Hi {lead.first_name},\n\n"
            f"Noticed {lead.company_name} is actively expanding roles around {trigger}.\n\n"
            f"Usually when teams scale at your stage ({lead.employee_count} employees), "
            f"managing signal capture across {tech_list} starts leaking qualified pipeline.\n\n"
            "We automated this pipeline audit workflow for similar teams, cutting manual stage checks by 40%.\n\n"
            f"Worth a 5-minute look at how this plugs into {primary_tech}?\n\n"
            "Best,\nGTM Systems"
        )
        return {"subject": subject, "body": body}

class ObsidianOutboundExporter:
    def __init__(self, vault_path: Optional[str] = None):
        self.vault_path = vault_path or os.path.expanduser("~/GTM 2nd Brain/Outbound Sequences")

    def export_lead_note(self, lead: LeadProfile, icp_eval: Dict[str, Any], copy: Dict[str, str]) -> str:
        os.makedirs(self.vault_path, exist_ok=True)
        filename = f"Prospect - {lead.company_name} - {lead.first_name} {lead.last_name}.md"
        filepath = os.path.join(self.vault_path, filename)
        today_str = datetime.now().strftime("%Y-%m-%d")
        
        tech_str = ", ".join(lead.tech_stack)
        is_qualified = str(icp_eval["qualified"]).lower()
        icp_score = icp_eval["icp_score"]
        
        lines = [
            "---",
            "type: prospect_outreach",
            f'company: "{lead.company_name}"',
            f'contact_name: "{lead.first_name} {lead.last_name}"',
            f'title: "{lead.title}"',
            f"icp_score: {icp_score}",
            f"qualified: {is_qualified}",
            f"created_date: {today_str}",
            "tags:",
            "  - gtm/outbound",
            "  - sequence/draft",
            "---",
            "",
            f"# Prospect: {lead.first_name} {lead.last_name} ({lead.company_name})",
            "",
            "## Qualification Overview",
            f"- **Title:** {lead.title}",
            f"- **Headcount:** {lead.employee_count}",
            f"- **ICP Fit Score:** `{icp_score} / 100`",
            f"- **Primary Tech Stack:** {tech_str}",
            "",
            "### Fit Triggers"
        ]
        
        for reason in icp_eval["fit_reasons"]:
            lines.append(f"- {reason}")
            
        lines.extend([
            "---",
            "",
            "## Outbound Email Sequence (Step 1)",
            "",
            f"**Subject:** `{copy['subject']}`",
            "",
            "```text",
            copy['body'],
            "```",
            "",
            "---",
            "",
            "## Task Execution",
            "- [ ] Send Step 1 email via Outreach / manual send",
            f"- [ ] Connect with {lead.first_name} on LinkedIn",
            "- [ ] Log activity in SFDC / CRM"
        ])
        
        with open(filepath, "w") as f:
            f.write("\n".join(lines))
        return filepath

if __name__ == '__main__':
    prospects = [
        LeadProfile("Sarah", "Connor", "Cyberdyne Systems", "VP of Sales Operations", 150, ["Salesforce", "Outreach", "Marketo"], True, ["Revenue Operations Manager", "SDR Lead"]),
        LeadProfile("Alex", "Murphy", "OCP Tech", "Director of Growth", 25, ["HubSpot"], False, [])
    ]
    engine = OutboundSkillEngine()
    exporter = ObsidianOutboundExporter()
    for prospect in prospects:
        eval_result = engine.score_icp_fit(prospect)
        print(f"Evaluating {prospect.first_name} {prospect.last_name} ({prospect.company_name})...")
        if eval_result["qualified"]:
            email_copy = engine.generate_copy(prospect, eval_result)
            note_path = exporter.export_lead_note(prospect, eval_result, email_copy)
            print(f"  --> Saved to Obsidian Vault: {note_path}")
        else:
            print("  --> Disqualified (Below ICP threshold)")
