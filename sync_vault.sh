#!/bin/bash

VAULT_DIR="$HOME/GTM 2nd Brain"
cd "$VAULT_DIR" || exit 1

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
git commit -m "$COMMIT_MSG"

echo "[!] Pushing changes to GitHub..."
git push origin main

echo ""
echo "[✓] Sync complete! Remote main is up to date."
echo "=========================================="
