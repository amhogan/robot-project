#!/usr/bin/env bash
# make_project_snapshot.sh
# Create a single-file Markdown snapshot of the robot project with:
#  - Directory tree (with sensible excludes)
#  - Index of included files (clickable within Markdown viewers)
#  - Concatenated file contents for easy review
# Usage:
#   ./make_project_snapshot.sh [PROJECT_DIR] [OUTPUT_DIR]
# Defaults:
#   PROJECT_DIR = ~/robot-project
#   OUTPUT_DIR  = $PROJECT_DIR/_snapshots

set -euo pipefail

# ---------- Config ----------
PROJECT_DIR="${1:-$HOME/robot-project}"
OUTPUT_DIR="${2:-$PROJECT_DIR/_snapshots}"
DATE_UTC="$(date -u '+%Y-%m-%d %H:%M:%S UTC')"
STAMP="$(date -u '+%Y%m%d-%H%M%S')"
OUTFILE="$OUTPUT_DIR/project-snapshot-$STAMP.md"

# Glob settings
shopt -s globstar nullglob extglob

# Exclusions for tree/find
TREE_IGNORE='node_modules|.git|build|install|log|__pycache__|.venv|dist|*.mp4|*.mov|*.mpg|*.avi|*.mkv|.DS_Store'

# File patterns to include in the snapshot
# (Add/remove here if you want more/less content)
INCLUDE_GLOBS=(
  "docker/**/*.yml"
  "docker/**/*.yaml"
  "docker/**/compose*.yml"
  "docker/**/Dockerfile"
  "docker/**/dockerfile"
  "site/**/*.html"
  "site/**/*.js"
  "site/**/*.css"
  "site/nginx/**/*.conf"
  "nginx/**/*.conf"
  "services/**/*.@(py|sh|yml|yaml)"
  "scripts/**/*.sh"
  "scripts/**/*.py"
  "ros*/**/*.py"
  "ros*/**/package.xml"
  "ros*/**/setup.cfg"
  "ros*/**/CMakeLists.txt"
  "**/requirements.txt"
  "**/.env"
  "STATE.md"
  "README.md"
  "index.html"
)

# ---------- Pre-flight checks ----------
if [[ ! -d "$PROJECT_DIR" ]]; then
  echo "ERROR: Project dir not found: $PROJECT_DIR" >&2
  exit 1
fi
mkdir -p "$OUTPUT_DIR"

# ---------- Collect matching files ----------
declare -A SEEN
FILES=()

pushd "$PROJECT_DIR" >/dev/null

for pattern in "${INCLUDE_GLOBS[@]}"; do
  for f in $pattern; do
    if [[ -f "$f" ]]; then
      # normalize to relative, de-dup
      rel="${f#./}"
      if [[ -z "${SEEN[$rel]+x}" ]]; then
        SEEN[$rel]=1
        FILES+=("$rel")
      fi
    fi
  done
done

# Sort file list
IFS=$'\n' FILES=($(printf '%s\n' "${FILES[@]}" | sort -u))
unset IFS

# ---------- Build directory tree ----------
TREE_BLOCK=""
if command -v tree >/dev/null 2>&1; then
  TREE_BLOCK="$(tree -a -I "$TREE_IGNORE" -F)"
else
  # Fallback to find + sed for a crude tree if 'tree' is unavailable
  # Prune common heavy dirs
  TREE_BLOCK="$(
    find . \
      -path './.git' -prune -o \
      -path './node_modules' -prune -o \
      -path './build' -prune -o \
      -path './install' -prune -o \
      -path './log' -prune -o \
      -path './__pycache__' -prune -o \
      -path './.venv' -prune -o \
      -type d -print -o -type f -print \
    | sed 's|^\./||' \
    | awk '{
        n=gsub(/[^\/]/,"");
        gsub(/[^\/]/,"");
        indent=length($0)-length(gensub(/[^\/]/,"","g"));
        gsub(/[^\/]/,"");
      }1' \
    | awk -F/ '{
        depth = NF-1;
        pad = "";
        for(i=0;i<depth;i++) pad=pad"  ";
        print pad $NF
      }'
  )"
fi

# ---------- Git context (optional) ----------
GIT_REMOTE=""
GIT_BRANCH=""
GIT_COMMIT=""
if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  GIT_REMOTE="$(git remote -v | awk 'NR==1{print $2}')"
  GIT_BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
  GIT_COMMIT="$(git rev-parse --short HEAD 2>/dev/null || true)"
fi

# ---------- Helper: make an anchor id from a path ----------
slugify() {
  # lowercase, replace spaces with '-', replace slashes with '--', strip invalids
  local s="${1,,}"
  s="${s// /-}"
  s="${s//\//--}"
  s="$(echo -n "$s" | sed 's/[^a-z0-9._-]/-/g')"
  printf "%s" "$s"
}

# ---------- Write header & index ----------
{
  echo "# Robot Project Snapshot"
  echo ""
  echo "- **Generated:** $DATE_UTC"
  echo "- **Host:** $(hostname 2>/dev/null || echo 'unknown')"
  if [[ -n "$GIT_COMMIT" ]]; then
    echo "- **Git:** \`$GIT_BRANCH@$GIT_COMMIT\`  ${GIT_REMOTE:+(remote: $GIT_REMOTE)}"
  fi
  echo ""
  echo "## Directory Tree"
  echo ""
  echo '```text'
  [[ -n "$TREE_BLOCK" ]] && echo "$TREE_BLOCK" || echo "(tree unavailable)"
  echo '```'
  echo ""
  echo "## Index"
  echo ""
  if ((${#FILES[@]}==0)); then
    echo "_No matching files found with current patterns._"
  else
    i=1
    for f in "${FILES[@]}"; do
      anchor="file-$(slugify "$f")"
      printf "%2d. [%s](#%s)\n" "$i" "$f" "$anchor"
      ((i++))
    done
  fi
  echo ""
  echo "---"
  echo ""
} > "$OUTFILE"

# ---------- Append file contents ----------
if ((${#FILES[@]})); then
  for f in "${FILES[@]}"; do
    anchor="file-$(slugify "$f")"
    echo "### File: $f {#$anchor}" >> "$OUTFILE"
    echo "" >> "$OUTFILE"

    # choose a fence language for nicer syntax highlighting
    ext="${f##*.}"
    case "${ext,,}" in
      yml|yaml) lang="yaml" ;;
      sh)       lang="bash" ;;
      py)       lang="python" ;;
      js)       lang="javascript" ;;
      html|htm) lang="html" ;;
      css)      lang="css" ;;
      conf)     lang="nginx" ;;
      xml)      lang="xml" ;;
      md)       lang="markdown" ;;
      txt|env)  lang="text" ;;
      *)        lang="" ;;
    esac

    if [[ -n "$lang" ]]; then
      echo "\`\`\`$lang" >> "$OUTFILE"
    else
      echo "\`\`\`" >> "$OUTFILE"
    fi
    cat -- "$f" >> "$OUTFILE" || true
    echo "" >> "$OUTFILE"
    echo "\`\`\`" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
    echo "---" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
  done
fi

popd >/dev/null

echo "Snapshot written to: $OUTFILE"
