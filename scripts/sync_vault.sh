#!/bin/bash

VAULT_DIR="$HOME/GTM 2nd Brain"
cd "$VAULT_DIR" || exit 1

notify() {
  local title="$1"
  local message="$2"
  osascript -e "display notification \"$message\" with title \"$title\""
}

echo "=========================================="
echo " OBSIDIAN VAULT AUTOMATED GIT SYNC"
echo "=========================================="
echo "Vault Directory: $VAULT_DIR"
echo "Time: $(date)"
echo ""

if [[ -z $(git status --porcelain) ]]; then
  echo "[✓] No local changes to commit. Vault is up to date."
  exit 0
fi

echo "[!] Changes detected. Staging files..."
git add .

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
COMMIT_MSG="auto(vault-sync): update GTM assets ($TIMESTAMP)"

echo "[!] Committing: '$COMMIT_MSG'..."
if ! git commit -m "$COMMIT_MSG"; then
  notify "Obsidian Vault Sync Failed" "Git commit failed."
  exit 1
fi

echo "[!] Pushing changes to GitHub..."
if git push origin main; then
  echo ""
  echo "[✓] Sync complete! Remote main is up to date."
  notify "Obsidian Vault Synced" "Changes successfully pushed to GitHub."
else
  echo ""
  echo "[!] Push failed."
  notify "Obsidian Vault Sync Failed" "Git push to GitHub failed."
  exit 1
fi
echo "=========================================="
