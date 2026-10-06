#!/usr/bin/env bash
# Remove private paths from ALL git history. Destructive: rewrites every commit hash.
# Run only in a fresh clone / after confirming the remote. You run the force-push yourself.
#   1. git clone <remote> purge-work && cd purge-work   (never run in your only copy)
#   2. bash scripts/purge_private_history.sh scripts/private_paths.txt
#   3. inspect: git log --stat | less ; git grep -i <a private term> $(git rev-list --all)
#   4. git remote -v   # confirm it is the repo you intend
#   5. git push --force --all && git push --force --tags
# Anyone with an old clone or fork still has the old history; rotate any secret that was ever in it.
set -euo pipefail
LIST="${1:-scripts/private_paths.txt}"
[ -s "$LIST" ] || { echo "path list $LIST missing or empty"; exit 1; }
command -v git-filter-repo >/dev/null || { echo "install git-filter-repo first (pip install git-filter-repo)"; exit 1; }
args=()
while IFS= read -r p; do [ -n "$p" ] && [[ "$p" != \#* ]] && args+=(--path "$p"); done < "$LIST"
git filter-repo --invert-paths "${args[@]}" --force
echo "Done. Review before pushing."
