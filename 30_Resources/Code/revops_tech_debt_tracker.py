import os
from datetime import datetime

vault = os.path.expanduser("~/GTM 2nd Brain")
dashboard_path = os.path.join(vault, "20_Areas/RevOps/Tech_Debt_Dashboard.md")

tech_debt_items = []

for root, _, files in os.walk(vault):
    for file in files:
        if file.endswith(".md") and file != "Tech_Debt_Dashboard.md":
            file_p = os.path.join(root, file)
            with open(file_p, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                for idx, line in enumerate(lines):
                    if "#tech-debt" in line or "TECH-DEBT:" in line:
                        clean_line = line.replace("#tech-debt", "").replace("TECH-DEBT:", "").strip()
                        rel_path = os.path.relpath(file_p, vault)
                        tech_debt_items.append({
                            "file": file,
                            "path": rel_path,
                            "line": idx + 1,
                            "description": clean_line if clean_line else "Unlabeled debt item"
                        })

date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
total_items = len(tech_debt_items)

rows = []
if tech_debt_items:
    for item in tech_debt_items:
        rows.append(f"| [{item['file']}]({item['path']}) | Line {item['line']} | {item['description']} | Open |")
else:
    rows.append("| *No active tech debt found* | - | Tag items with `#tech-debt` across vault notes to track | - |")

rows_str = "\n".join(rows)

content = f"""---
type: area
category: revops
tags:
  - revops
  - tech-debt
  - dashboard
date: {date_str[:10]}
status: active
---

# RevOps Technical Debt Dashboard

*Last Scanned: {date_str}* | **Active Debt Items: {total_items}**

---

## Active Technical Debt Backlog

| Source Note | Location | Description / Remedy | Status |
| :--- | :--- | :--- | :--- |
{rows_str}

---

## Usage Guide
To register a new piece of RevOps technical debt, add `#tech-debt` followed by an explanation anywhere in your Obsidian notes, then run:

```bash
python3 \"$HOME/GTM 2nd Brain/30_Resources/Code/revops_tech_debt_tracker.py\"
```
"""

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"[✓] Generated Tech Debt Dashboard at {dashboard_path} with {total_items} item(s).")
