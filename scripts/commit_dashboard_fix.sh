#!/usr/bin/env bash
set -euo pipefail
cd ~/robot-project

# Show what's changed (for visibility)
echo "=== Git status before ==="
git status --short || true

# Stage the files we updated today (conditionally, if they exist/changed)
git add site/index.html || true
git add site/nginx/conf.d/robot.conf || true
git add docker/docker-compose.yml || true
# If you applied the optional server-side uptime JSON change:
if git status --porcelain -- services/netstatus/app.py | grep -qE '^( M|A )'; then
  git add services/netstatus/app.py
fi
# If you copied the review bundle script into the repo:
[ -f scripts/prep_review_bundle.sh ] && git add scripts/prep_review_bundle.sh

# Commit
git commit -m "Dashboard stabilization: live video + telemetry
- Nginx: robust upstreams with Docker DNS (resolver 127.0.0.11); proxies /status*, /stream, /snapshot
- Dashboard UI: fixed ROS topic handling (removed URL-encoding, auto-prefix '/'); added size control (480/640/800)
- Telemetry: resilient uptime parsing (supports uptime_sec/uptime_seconds/plain text); CPU %, load, temp, disk; raw JSON viewer
- Compose: unified stack on 'robot-net' (video-dashboard, web-video-server, netstatus, usb-cam, ros-core)
- Notes: Snapshot mode 1 FPS; stream variant cycling (raw/ros_compressed) via UI"

# Push to current branch
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
echo "Pushing to origin/${BRANCH}…"
git push origin "${BRANCH}"

# Optional: tag this milestone
TAG="v0.2-dashboard-stabilization"
if ! git rev-parse "${TAG}" >/dev/null 2>&1; then
  git tag -a "${TAG}" -m "Dashboard stabilized: video + telemetry working"
  git push origin "${TAG}" || true
fi

echo "=== Done. Current HEAD ==="
git --no-pager log -1 --oneline
