#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-$HOME/robot-project}"     # optional arg: repo path
BRANCH="${GIT_BRANCH:-main}"         # override with env if needed
MSG="${GIT_MSG:-}"                   # override with env or here-doc
DATE="$(date +%Y-%m-%d)"
DATE_TAG="$(date +%Y%m%d)"
TAG_PREFIX="${TAG_PREFIX:-v}"        # e.g., "v" -> v20250810-1
TAG_ON_COMMIT="${TAG_ON_COMMIT:-1}"  # set 0 to disable tagging
PUSH_REMOTE="${PUSH_REMOTE:-origin}" # allow override if needed

cd "$REPO"

git fetch --all --prune
git checkout "$BRANCH"
git pull --rebase --autostash "$PUSH_REMOTE" "$BRANCH" || true

# Default commit message if not provided
if [[ -z "$MSG" ]]; then
  MSG="Daily checkpoint: dashboard & netstatus updates ($DATE)"
fi

# Optional: prepend CHANGELOG entry (if provided and file exists)
if [[ -n "${CHANGELOG_TXT:-}" && -f CHANGELOG.md ]]; then
  awk -v d="## [$DATE]" -v t="$CHANGELOG_TXT" '
    BEGIN { print d "\n" t "\n" }
    { print }
  ' CHANGELOG.md > CHANGELOG.md.new && mv CHANGELOG.md.new CHANGELOG.md
fi

git add -A
if git diff --staged --quiet; then
  echo "No changes to commit."
  exit 0
fi

git commit -m "$MSG"
git push "$PUSH_REMOTE" "$BRANCH"
echo "Pushed to $BRANCH ✔"

# --- Tagging ---
if [[ "$TAG_ON_COMMIT" == "1" ]]; then
  # Find next available tag number for the day
  base="${TAG_PREFIX}${DATE_TAG}"
  # existing tags like v20250810-1, v20250810-2 ...
  last_num=$(git tag --list "${base}-*" | sed -E "s#^${base}-##" | sort -n | tail -n1 || true)
  if [[ -z "$last_num" ]]; then
    next=1
  else
    next=$((last_num + 1))
  fi
  tag="${base}-${next}"

  # Create and push annotated tag
  git tag -a "$tag" -m "$MSG"
  git push "$PUSH_REMOTE" "$tag"
  echo "Created and pushed tag: $tag ✔"
fi
