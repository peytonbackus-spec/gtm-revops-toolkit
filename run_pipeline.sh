#!/bin/zsh
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

RESEARCH_LOG="$HOME/GTM 2nd Brain/research.log"
SYNC_LOG="$HOME/GTM 2nd Brain/sync.log"

echo "=== PIPELINE RUN: $(date) ===" >> "$RESEARCH_LOG"
python3 "$HOME/GTM 2nd Brain/30_Resources/Code/gtm_researcher.py" >> "$RESEARCH_LOG" 2>&1

echo "=== SYNC RUN: $(date) ===" >> "$SYNC_LOG"
"$HOME/GTM 2nd Brain/sync_vault.sh" >> "$SYNC_LOG" 2>&1
