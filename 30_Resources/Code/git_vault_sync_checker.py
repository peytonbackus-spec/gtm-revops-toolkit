"""
---
type: resource
category: code
tags:
  - resource
  - python
  - git
  - obsidian
status: active
last_updated: 2026-08-21
---
"""

import os
import subprocess
import sys

def check_vault_git_status():
    vault_dir = os.path.expanduser("~/GTM 2nd Brain")
    
    if not os.path.exists(os.path.join(vault_dir, ".git")):
        print(f"[!] Directory {vault_dir} is not a git repository.")
        sys.exit(1)

    os.chdir(vault_dir)

    print("==========================================")
    print(" OBSIDIAN VAULT GIT STATUS CHECKER")
    print("==========================================")
    print(f"Vault Location: {vault_dir}")
    print()

    # Fetch branch info
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip()
    print(f"Current Branch: {branch}")
    print()

    # Run git status --porcelain
    status_output = subprocess.check_output(["git", "status", "--porcelain"]).decode("utf-8").strip()

    if not status_output:
        print("[✓] Vault is clean! All files are committed and in sync.")
    else:
        print("[!] Local changes detected:")
        print()
        lines = status_output.split("\n")
        untracked = [line[3:] for line in lines if line.startswith("??")]
        modified = [line[3:] for line in lines if line.startswith(" M") or line.startswith("M ")]
        staged = [line[3:] for line in lines if line.startswith("A ") or line.startswith("M ")]

        if staged:
            print("  Staged Files:")
            for f in staged:
                print(f"    + {f}")
            print()

        if modified:
            print("  Modified Files:")
            for f in modified:
                print(f"    ~ {f}")
            print()

        if untracked:
            print("  Untracked Files (New):")
            for f in untracked:
                print(f"    ? {f}")
            print()

    print("==========================================")

if __name__ == "__main__":
    check_vault_git_status()
