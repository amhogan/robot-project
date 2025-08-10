#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-$HOME/robot-project}"     # optional arg: repo path
BRANCH="${GIT_BRANCH:-main}"         # override with env if needed
MSG="${GIT_MSG:-}"                   # override with env or here-doc
DATE="$(date +%Y-%m-%d)"

cd "$REPO"

# Make sure we're on the right branch and up to date
git fetch --all --prune
git checkout "$BRANCH"
git pull --rebase --autostash origin "$BRANCH" || true

# Auto message if none provided
if [[ -z "$MSG" ]]; then
  MSG="Daily checkpoint: dashboard & netstatus updates ($DATE)"
fi

# Optional: append to CHANGELOG.md if it exists and we have a longer note
if [[ -n "${CHANGELOG_TXT:-}" && -f CHANGELOG.md ]]; then
  awk -v d="## [$DATE]" -v t="$CHANGELOG_TXT" '
    BEGIN { print d "\n" t "\n" }
    { print }
  ' CHANGELOG.md > CHANGELOG.md.new && mv CHANGELOG.md.new CHANGELOG.md
fi

# Stage, commit (only if there are changes), push
git add -A
if git diff --staged --quiet; then
  echo "No changes to commit."
  exit 0
fi

git commit -m "$MSG"
git push origin "$BRANCH"
echo "Pushed to $BRANCH ✔"
