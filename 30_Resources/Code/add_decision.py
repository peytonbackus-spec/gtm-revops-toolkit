import os
import sys
from datetime import datetime

if len(sys.argv) < 3:
    print('Usage: python3 add_decision.py "Decision text" "Reason / Context"')
    sys.exit(1)

decision = sys.argv[1]
reason = sys.argv[2]
date_str = datetime.now().strftime("%Y-%m-%d")

log_path = os.path.expanduser("~/GTM 2nd Brain/00_System/Errors_and_Preferences.md")
if os.path.exists(log_path):
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"| {date_str} | {decision} | {reason} | Active |\n")
    print(f"[✓] Decision logged to {log_path}")
else:
    print(f"[!] Error: Log file not found at {log_path}")
