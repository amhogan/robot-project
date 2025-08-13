#!/usr/bin/env sh
set -eu

# ==== Config ===============================================================
ROOT="${HOME}/robot-project"
BACKUP_DIR="/tmp/robot-backups"
NOW="$(date +%F)"
TIME="$(date +%H%M)"
STATE="${ROOT}/STATE.md"

# Set to "1" to run quick endpoint checks (dashboard/web-video)
RUN_CHECKS="${RUN_CHECKS:-1}"

# ==== Internals ============================================================
COMPLETED_TMP="$(mktemp)"
CLEANUPS=""

log() { printf "\n[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

cleanup() {
  [ -n "$COMPLETED_TMP" ] && [ -f "$COMPLETED_TMP" ] && rm -f "$COMPLETED_TMP" || true
}
CLEANUPS="cleanup $CLEANUPS"
trap 'for f in $CLEANUPS; do $f || true; done' EXIT INT TERM

add_completed_line() {
  # keep backticks literal
  printf "%s\n" "$1" >> "$COMPLETED_TMP"
}

ensure_layout() {
  mkdir -p \
    "$ROOT/docker/compose" \
    "$ROOT/site/nginx/conf.d" \
    "$ROOT/services" \
    "$ROOT/robot_ws/src" \
    "$ROOT/scripts" \
    "$ROOT/docs/wiring"
}

backup_trees() {
  log "Backing up existing project trees to ${BACKUP_DIR}..."
  mkdir -p "$BACKUP_DIR"
  tar -C / -czf "${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz" \
    robot-docker robot-project robot-dashboard 2>/dev/null || true
  log "Backup archive: ${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz"
}

copy_dir() {
  # copy_dir <src> <dst>
  src="$1"; dst="$2"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a "$src"/ "$dst"/
  else
    mkdir -p "$dst"
    cp -a "$src"/. "$dst"/
  fi
}

rsync_logged() {
  # rsync_logged <src_dir> <dst_dir> <desc>
  src="$1"; dst="$2"; desc="$3"
  if [ -d "$src" ]; then
    log "Syncing: $src -> $dst"
    copy_dir "$src" "$dst"
    add_completed_line "- ${NOW} – Migrated ${desc}: \`$src\` → \`$dst\`."
  else
    log "Skip (missing): $src"
  fi
}

move_content() {
  rsync_logged "${HOME}/robot-dashboard" "${ROOT}/site" "dashboard static files"
  rsync_logged "${HOME}/robot-docker/robot_ws" "${ROOT}/robot_ws" "ROS 2 workspace"
  rsync_logged "${HOME}/robot-docker/scripts" "${ROOT}/scripts" "utility scripts"

  if [ -d "${HOME}/robot-docker/site/nginx/conf.d" ]; then
    log "Syncing nginx snippets from robot-docker → site/nginx/conf.d"
    mkdir -p "${ROOT}/site/nginx/conf.d"
    copy_dir "${HOME}/robot-docker/site/nginx/conf.d" "${ROOT}/site/nginx/conf.d"
    add_completed_line "- ${NOW} – Migrated nginx snippets: \`${HOME}/robot-docker/site/nginx/conf.d\` → \`${ROOT}/site/nginx/conf.d\`."
  fi
}

create_scaffold_files_if_missing() {
  [ -f "${ROOT}/docker/compose/base.yml" ] || {
    cat > "${ROOT}/docker/compose/base.yml" <<'YAML'
version: "3.9"
name: robot
services: {}
networks:
  robot-net: {}
volumes:
  robot-data: {}
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/base.yml\`."
  }

  [ -f "${ROOT}/docker/compose/web.yml" ] || {
    cat > "${ROOT}/docker/compose/web.yml" <<'YAML'
version: "3.9"
services:
  video-dashboard:
    image: nginx:stable
    container_name: video-dashboard
    restart: unless-stopped
    ports: ["${DASHBOARD_PORT:-8081}:80"]
    networks: [robot-net]
    volumes:
      - ../site:/usr/share/nginx/html:ro
      - ../site/nginx/conf.d:/etc/nginx/conf.d:ro

  netstatus:
    build:
      context: ../services/netstatus
    container_name: netstatus
    restart: unless-stopped
    expose: ["5000"]
    networks: [robot-net]
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/web.yml\`."
  }

  [ -f "${ROOT}/docker/compose/ros.yml" ] || {
    cat > "${ROOT}/docker/compose/ros.yml" <<'YAML'
version: "3.9"
services:
  ros-core:
    image: ros:iron-ros-core
    container_name: ros-core
    restart: unless-stopped
    networks: [robot-net]
    command: ["bash","-lc","source /opt/ros/iron/setup.bash && sleep infinity"]

  web-video-server:
    image: ros:iron-ros-base
    container_name: web-video-server
    restart: unless-stopped
    networks: [robot-net]
    ports: ["${WVS_PORT:-8080}:8080"]
    command: >
      bash -lc "
      apt-get update &&
      apt-get install -y ros-iron-web-video-server &&
      source /opt/ros/iron/setup.bash &&
      ros2 run web_video_server web_video_server --port 8080 --address 0.0.0.0
      "
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/ros.yml\`."
  }

  [ -f "${ROOT}/docker/.env" ] || {
    cat > "${ROOT}/docker/.env" <<'ENV'
DASHBOARD_PORT=8081
WVS_PORT=8080
ROBOT_HOSTNAME=RPi-Robot
ENV
    add_completed_line "- ${NOW} – Added \`docker/.env\` with default ports."
  }

  [ -f "${ROOT}/Makefile" ] || {
    cat > "${ROOT}/Makefile" <<'MAKE'
COMPOSE = docker compose -p robot -f docker/compose/base.yml -f docker/compose/web.yml -f docker/compose/ros.yml

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f --tail=200

rebuild:
	$(COMPOSE) build --no-cache

ps:
	$(COMPOSE) ps

restart:
	$(COMPOSE) down && $(COMPOSE) up -d
MAKE
    add_completed_line "- ${NOW} – Created \`Makefile\` (make up / logs / rebuild / ps / restart)."
  }
}

ensure_state_md() {
  [ -f "$STATE" ] || {
    cat > "$STATE" <<'EOF'
# 🛠 Robot Project – State Tracker

**Last Updated:** YYYY-MM-DD  
**Maintainer:** Drew  

---

## 📌 Current Phase
Dashboard & Metrics Integration + RoboClaw Motor Control Recovery

---

## ✅ Completed Since Last Update
- YYYY-MM-DD – Initial consolidation scaffold created (compose skeletons, Makefile, layout).

---

## 🚧 In Progress
- Directory consolidation and path updates across compose & mounts.
- Dashboard metrics for CPU %, memory %, disk.
- RoboClaw firmware recovery.

---

## 🗒 Next Actions
1. Review consolidated layout and mounts.
2. Bring stack up: `make up`.
3. Finish metrics and verify endpoints via dashboard.

---

## ⚠ Issues / Blockers
- RoboClaw device in bootloader; awaiting recovery path.
- Some services still referencing legacy paths.

---

## 📂 Project Structure Reference
robot-project/
docker/compose/ → Compose YAMLs
site/ → Dashboard + nginx
services/ → Small backends (e.g., netstatus)
robot_ws/src/ → ROS 2 packages
scripts/ → Helper scripts
docs/ → Design docs & diagrams
STATE.md → This file


---

## 🔌 System Reference
**Host:** RPi-Robot  
**Ports:** Dashboard :8081, Web Video :8080, Netstatus :5000 (in-network)

---

## 🧩 Active Containers
| Name              | Purpose                  | Restart |
|-------------------|--------------------------|---------|
| video-dashboard   | Nginx + UI               | unless-stopped |
| netstatus         | Metrics API              | unless-stopped |
| ros-core          | ROS 2 base               | unless-stopped |
| web-video-server  | Video server             | unless-stopped |
EOF
    log "Created new STATE.md"
  }
}

update_last_updated() {
  awk -v today="$NOW" '
    BEGIN{done=0}
    {
      if (!done && $0 ~ /^\*\*Last Updated:\*\*/) {
        print "**Last Updated:** " today "  "
        done=1
      } else {
        print
      }
    }
  ' "$STATE" > "${STATE}.tmp" && mv "${STATE}.tmp" "$STATE"
}

insert_completed_lines() {
  grep -q "^## ✅ Completed Since Last Update" "$STATE" || {
    printf "\n\n## ✅ Completed Since Last Update\n" >> "$STATE"
  }
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    if ! grep -Fq "$line" "$STATE"; then
      awk -v ins="$line" '
        BEGIN{added=0}
        {print}
        /^## ✅ Completed Since Last Update$/ && !added {print ins; added=1}
      ' "$STATE" > "${STATE}.tmp" && mv "${STATE}.tmp" "$STATE"
    fi
  done < "$COMPLETED_TMP"
}

create_symlinks() {
  ln -snf "$ROOT/docker" "${HOME}/robot-docker.new"
  ln -snf "$ROOT/site"   "${HOME}/robot-dashboard.new"
  add_completed_line "- ${NOW} – Added convenience links: \`${HOME}/robot-docker.new\` and \`${HOME}/robot-dashboard.new\`."
}

have_cmd() { command -v "$1" >/dev/null 2>&1; }

check_url() {
  # check_url <url> <desc>
  url="$1"; desc="$2"
  if have_cmd curl; then
    if curl -fsS --max-time 2 "$url" >/dev/null 2>&1; then
      add_completed_line "- ${NOW} – CHECK PASS: ${desc} reachable at ${url}."
    else
      add_completed_line "- ${NOW} – CHECK FAIL: ${desc} not reachable at ${url}."
    fi
  elif have_cmd wget; then
    if wget -q -T 2 -O - "$url" >/dev/null 2>&1; then
      add_completed_line "- ${NOW} – CHECK PASS: ${desc} reachable at ${url}."
    else
      add_completed_line "- ${NOW} – CHECK FAIL: ${desc} not reachable at ${url}."
    fi
  else
    add_completed_line "- ${NOW} – CHECK SKIP: No curl/wget to test ${desc} at ${url}."
  fi
}

run_checks() {
  [ "$RUN_CHECKS" = "1" ] || { log "Checks disabled (RUN_CHECKS=0)"; return 0; }
  log "Running quick endpoint checks (best-effort)…"
  check_url "http://localhost:8081/" "Dashboard root"
  check_url "http://localhost:8081/status" "Netstatus via Nginx"
  check_url "http://localhost:8080/streams" "Web Video Server streams"
}

summary() {
  log "Done. Next:"
  cat <<TXT

1) Inspect the new layout:
   tree -L 3 ${ROOT} 2>/dev/null || ls -la ${ROOT}

2) Bring the stack up:
   cd ${ROOT}
   make up && make ps

3) Quick checks (already attempted if RUN_CHECKS=1):
   curl -I http://localhost:8081/ || true
   curl -s http://localhost:8081/status | head -n 5 || true
   curl -s http://localhost:8080/streams | head -n 5 || true

Legacy convenience links:
  ${HOME}/robot-docker.new  -> ${ROOT}/docker
  ${HOME}/robot-dashboard.new -> ${ROOT}/site

Backup archive:
  ${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz
TXT
}

main() {
  log "Starting consolidation into ${ROOT}"
  ensure_layout
  backup_trees
  move_content
  create_scaffold_files_if_missing
  ensure_state_md
  add_completed_line "- ${NOW} – Consolidated repos into \`${ROOT}\` monorepo layout."
  create_symlinks
  run_checks
  update_last_updated
  insert_completed_lines
  summary
}

main "$@"

