#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/robot-project}"
BRANCH="${BRANCH:-main}"

cd "$REPO_DIR"

# Ensure upstream exists
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repo: $REPO_DIR" >&2
  exit 1
fi
if ! git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  echo "Warning: origin/$BRANCH not found; will push and create it on first run."
fi

# Pull latest (fast-forward only to avoid surprises in unattended runs)
git fetch origin || true
git merge --ff-only "origin/$BRANCH" 2>/dev/null || true

# Stage and commit if there are changes
git add -A

if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

HOST="$(hostname -s || echo host)"
TS="$(date +'%Y-%m-%d %H:%M:%S %z')"
MSG="backup($HOST): automated commit at $TS"

git commit -m "$MSG"

# Push with a simple retry if the network blips
for i in 1 2 3; do
  if git push origin "$BRANCH"; then
    echo "Backup pushed to GitHub: $MSG"
    exit 0
  fi
  echo "Push failed (attempt $i). Retrying in 5s..."
  sleep 5
done

echo "Push failed after retries." >&2
exit 1
