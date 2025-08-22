#!/usr/bin/env bash
# prep_review_bundle.sh
# Purpose: Gather all pertinent config/YAML/source files + useful diagnostics
# into a single human-readable TXT and a tarball for offline review.
# Safe to run multiple times. Designed for ~/robot-project layout.
#
# Output:
#   /tmp/review/robot-review-<host>-<timestamp>.txt
#   /tmp/review/robot-review-<host>-<timestamp>.tgz
#
# Usage:
#   chmod +x prep_review_bundle.sh
#   ./prep_review_bundle.sh [<repo_root>]
#
# Notes:
# - Tries hard to degrade gracefully if some tools/containers aren't present.
# - Avoids including heavy/binary files and build artifacts.

set -Eeuo pipefail

REPO_ROOT="${1:-$HOME/robot-project}"
HOST="$(hostname 2>/dev/null || echo host)"
TS="$(date +%Y%m%d-%H%M%S)"
OUT_DIR="/tmp/review"
OUT_TXT="$OUT_DIR/robot-review-${HOST}-${TS}.txt"
OUT_TGZ="$OUT_DIR/robot-review-${HOST}-${TS}.tgz"

# --- helpers ---------------------------------------------------------------

section () {
  printf '\n\n===== %s =====\n' "$1" | tee -a "$OUT_TXT"
}

subsection () {
  printf '\n--- %s ---\n' "$1" | tee -a "$OUT_TXT"
}

add_file () {
  # $1 = path
  local p="$1"
  if [ -f "$p" ]; then
    printf '\n\n==== FILE: %s ====\n' "$p" | tee -a "$OUT_TXT"
    # Try to detect if it's text
    if file -b "$p" | grep -qiE 'text|json|xml|yaml|yml|javascript|python|html|shell|empty'; then
      sed -e 's/\t/    /g' "$p" | tee -a "$OUT_TXT" >/dev/null
    else
      echo "(binary or unknown type; skipped content)" | tee -a "$OUT_TXT" >/dev/null
    fi
  fi
}

add_glob () {
  # Add all files matching the glob, if any, in lexical order
  local pattern="$1"
  shopt -s nullglob dotglob
  local matches=($pattern)
  shopt -u nullglob dotglob
  if [ ${#matches[@]} -gt 0 ]; then
    for p in "${matches[@]}"; do
      [ -f "$p" ] && add_file "$p"
    done
  fi
}

cmd () {
  # Log a command + output, but never fail the whole script on errors.
  # Usage: cmd "description" "actual command"
  local desc="$1"
  local command="$2"
  printf '\n$ %s\n' "$command" | tee -a "$OUT_TXT"
  # shellcheck disable=SC2086
  bash -lc "$command" >>"$OUT_TXT" 2>&1 || {
    printf '(%s failed)\n' "$desc" | tee -a "$OUT_TXT" >/dev/null
  }
}

ensure_tools () {
  # Not strictly required, but helpful when present.
  for t in file awk sed find grep sha256sum tree jq curl wget docker; do
    command -v "$t" >/dev/null 2>&1 || true
  done
}

# --- begin -----------------------------------------------------------------

mkdir -p "$OUT_DIR"
: > "$OUT_TXT"  # truncate/create

section "Robot Review Bundle"
echo "Host: $HOST" | tee -a "$OUT_TXT"
echo "Time: $(date -Is)" | tee -a "$OUT_TXT"
echo "Repo root: $REPO_ROOT" | tee -a "$OUT_TXT"

section "System Info"
cmd "uname" "uname -a"
cmd "lsb_release" "lsb_release -a"
cmd "docker version" "docker --version"
cmd "docker compose version" "docker compose version"

section "Directory Overview"
if command -v tree >/dev/null 2>&1; then
  cmd "tree" "tree -a -I '.git|node_modules|build|dist|install|log|__pycache__|*.mp4' '$REPO_ROOT'"
else
  cmd "find" "find '$REPO_ROOT' -type d -maxdepth 6 -printf '%p\n'"
  cmd "find files" "find '$REPO_ROOT' -type f -maxdepth 6 -printf '%p\n'"
fi

section "Key Files Index (path  size  sha256)"
# Build an index of the key files we plan to include.
# We collect paths into a temporary list, then de-dup.
TMP_LIST="$(mktemp)"
# root docs
find "$REPO_ROOT" -maxdepth 1 -type f -name '*.md' -print >>"$TMP_LIST" 2>/dev/null || true
[ -f "$REPO_ROOT/STATE.md" ] && echo "$REPO_ROOT/STATE.md" >> "$TMP_LIST"
# docker + compose
find "$REPO_ROOT/docker" -type f \( -name '*.yml' -o -name '*.yaml' \) -print >>"$TMP_LIST" 2>/dev/null || true
[ -f "$REPO_ROOT/docker/docker-compose.yml" ] && echo "$REPO_ROOT/docker/docker-compose.yml" >> "$TMP_LIST"
# site & nginx
find "$REPO_ROOT/site" -type f \( -name '*.html' -o -name '*.js' -o -name '*.css' -o -name '*.conf' \) -print >>"$TMP_LIST" 2>/dev/null || true
# services & scripts
find "$REPO_ROOT/services" -type f -print >>"$TMP_LIST" 2>/dev/null || true
find "$REPO_ROOT/scripts" -type f -name '*.sh' -print >>"$TMP_LIST" 2>/dev/null || true
# env files
[ -f "$REPO_ROOT/.env" ] && echo "$REPO_ROOT/.env" >> "$TMP_LIST"
for f in "$REPO_ROOT"/.env.*; do [ -f "$f" ] && echo "$f"; done >> "$TMP_LIST" 2>/dev/null || true

# Deduplicate and print index with size + sha256
sort -u "$TMP_LIST" | while IFS= read -r p; do
  if [ -f "$p" ]; then
    size=$(stat -c%s "$p" 2>/dev/null || wc -c <"$p")
    sum=$(sha256sum "$p" 2>/dev/null | awk '{print $1}')
    printf '%s\t%s\t%s\n' "$p" "$size" "$sum" | tee -a "$OUT_TXT"
  fi
done

section "Rendered docker compose (for each compose file)"
# For each compose file, try 'docker compose config'
while IFS= read -r cf; do
  [ -f "$cf" ] || continue
  subsection "docker compose config: $cf"
  cmd "docker compose config" "docker compose -f '$cf' config"
done < <(find "$REPO_ROOT" -type f -name 'docker-compose*.yml' -o -name 'compose*.yml' 2>/dev/null | sort -u || true)

section "Running Containers (snapshot)"
cmd "docker ps" "docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'"

# Attempt to discover likely container names
DASH_CONT="$(docker ps --format '{{.Names}}' | grep -Ei 'video[-]?dashboard|robot-video-dashboard' | head -n1 || true)"
WVS_CONT="$(docker ps --format '{{.Names}}' | grep -Ei 'web[-]?video[-]?server' | head -n1 || true)"
CAM_CONT="$(docker ps --format '{{.Names}}' | grep -Ei 'v4l2|usb.*cam|ros2-.*camera|camera' | head -n1 || true)"
NETS_CONT="$(docker ps --format '{{.Names}}' | grep -Ei 'netstatus|telemetry' | head -n1 || true)"

section "Container Diagnostics (best-effort)"

if [ -n "$DASH_CONT" ]; then
  subsection "Nginx config from $DASH_CONT (nginx -T)"
  cmd "nginx -T" "docker exec -i '$DASH_CONT' sh -lc 'nginx -T'"
  subsection "Try dashboard endpoints via container loopback"
  cmd "GET /status" "docker exec -i '$DASH_CONT' sh -lc 'wget -S -O - http://127.0.0.1/status 2>&1 | head -n 60 || curl -sS -D- http://127.0.0.1/status | head -n 60'"
  cmd "GET /status_temp" "docker exec -i '$DASH_CONT' sh -lc 'wget -S -O - http://127.0.0.1/status_temp 2>&1 | head -n 60 || curl -sS -D- http://127.0.0.1/status_temp | head -n 60'"
  cmd "GET /status_uptime" "docker exec -i '$DASH_CONT' sh -lc 'wget -S -O - http://127.0.0.1/status_uptime 2>&1 | head -n 60 || curl -sS -D- http://127.0.0.1/status_uptime | head -n 60'"
  subsection "Try WVS snapshot through dashboard proxy (if /snapshot exposed)"
  cmd "GET /snapshot?topic=/image_raw" "docker exec -i '$DASH_CONT' sh -lc 'wget -S -O - \"http://127.0.0.1/snapshot?topic=/image_raw\" 2>&1 | head -n 40 || true'"
fi

if [ -n "$WVS_CONT" ]; then
  subsection "web_video_server logs ($WVS_CONT)"
  cmd "logs" "docker logs --tail=200 '$WVS_CONT'"
  subsection "ROS topics inside $WVS_CONT"
  cmd "ros2 topic list -t" "docker exec -i '$WVS_CONT' bash -lc '. /opt/ros/iron/setup.bash; ros2 topic list -t || true'"
  subsection "Try local snapshot inside $WVS_CONT"
  cmd "curl snapshot" "docker exec -i '$WVS_CONT' bash -lc 'command -v curl >/dev/null || (apt-get update && apt-get install -y curl); curl -sS -o /tmp/snap.jpg \"http://127.0.0.1:8080/snapshot?topic=/image_raw\"; file /tmp/snap.jpg && ls -lh /tmp/snap.jpg || true'"
fi

if [ -n "$CAM_CONT" ]; then
  subsection "Camera container header/sample ($CAM_CONT)"
  cmd "echo header" "docker exec -i '$CAM_CONT' bash -lc '. /opt/ros/iron/setup.bash 2>/dev/null || true; ros2 topic echo /image_raw --field header --qos-reliability best_effort --once || ros2 topic echo /camera/image_raw --field header --qos-reliability best_effort --once || true'"
  cmd "topic hz" "docker exec -i '$CAM_CONT' bash -lc '. /opt/ros/iron/setup.bash 2>/dev/null || true; ros2 topic hz /image_raw --qos-reliability best_effort --window 10 || ros2 topic hz /camera/image_raw --qos-reliability best_effort --window 10 || true'"
fi

if [ -n "$NETS_CONT" ]; then
  subsection "Telemetry backend ($NETS_CONT) sample"
  cmd "backend /status" "docker exec -i '$NETS_CONT' sh -lc 'wget -qO- http://127.0.0.1:5000/status || curl -sS http://127.0.0.1:5000/status || true'"
  cmd "backend /status_temp" "docker exec -i '$NETS_CONT' sh -lc 'wget -qO- http://127.0.0.1:5000/status_temp || curl -sS http://127.0.0.1:5000/status_temp || true'"
  cmd "backend /status_uptime" "docker exec -i '$NETS_CONT' sh -lc 'wget -qO- http://127.0.0.1:5000/status_uptime || curl -sS http://127.0.0.1:5000/status_uptime || true'"
fi

section "Selected File Contents"

# Root docs first
add_glob "$REPO_ROOT/README*"
add_file "$REPO_ROOT/STATE.md"

# Compose/YAML
add_glob "$REPO_ROOT/docker/docker-compose.yml"
add_glob "$REPO_ROOT/docker/*.yml"
add_glob "$REPO_ROOT/docker/*.yaml"
add_glob "$REPO_ROOT/docker/compose/*.yml"
add_glob "$REPO_ROOT/docker/compose/*.yaml"

# Site + Nginx
add_glob "$REPO_ROOT/site/index.html"
add_glob "$REPO_ROOT/site/*.html"
add_glob "$REPO_ROOT/site/nginx/conf.d/*.conf"
add_glob "$REPO_ROOT/site/js/*.js"
add_glob "$REPO_ROOT/site/css/*.css"

# Services + scripts
add_glob "$REPO_ROOT/services/*/*"
add_glob "$REPO_ROOT/scripts/*.sh"
add_glob "$REPO_ROOT/.env"
add_glob "$REPO_ROOT/.env.*"

# Tarball of the interesting files (mirrors index selection)
section "Creating tarball"
# Build a manifest and tar it
MANIFEST="$(mktemp)"
sort -u "$TMP_LIST" > "$MANIFEST"
# Filter out non-existent and obviously large/binary directories
grep -E -v '\.(mp4|mkv|avi|zip|tar\.gz|tgz)$' "$MANIFEST" > "${MANIFEST}.ok" || true

cmd "tarball" "tar -czf '$OUT_TGZ' -T '${MANIFEST}.ok'"

section "Done"
echo "Wrote: $OUT_TXT" | tee -a "$OUT_TXT"
echo "Tar:   $OUT_TGZ" | tee -a "$OUT_TXT"

exit 0
