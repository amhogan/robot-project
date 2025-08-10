#!/usr/bin/env bash
set -euo pipefail

HOSTNAME_SHORT="$(hostname -s || echo RPi)"
BACKUP_ROOT="/tmp/robot-backups"
TIMESTAMP="$(date +'%Y%m%d-%H%M%S')"
ARCHIVE_NAME="robot-backup-${HOSTNAME_SHORT}-${TIMESTAMP}.tar.gz"
ARCHIVE_PATH="${BACKUP_ROOT}/${ARCHIVE_NAME}"

PROJECT_DIRS=("/home/pi/robot-project")

SMB_ENABLE="${SMB_ENABLE:-0}"
SMB_URL="${SMB_URL:-}"
SMB_USER="${SMB_USER:-}"
SMB_PASS="${SMB_PASS:-}"
SMB_DEST_SUBDIR="${SMB_DEST_SUBDIR:-share}"

echo "Creating archive: ${ARCHIVE_PATH}"
mkdir -p "${BACKUP_ROOT}"

tar -czf "${ARCHIVE_PATH}" \
  --exclude-vcs \
  --exclude='**/node_modules' \
  --exclude='**/__pycache__' \
  --exclude='**/build' \
  --exclude='**/install' \
  --exclude='**/log' \
  --exclude='**/*.mp4' \
  --exclude='**/.DS_Store' \
  --transform="s|^/||" \
  "${PROJECT_DIRS[@]}"

echo "Archive size: $(du -h "${ARCHIVE_PATH}" | cut -f1)"

if [[ "${SMB_ENABLE}" == "1" ]]; then
  echo "Uploading to SMB share: ${SMB_URL}/${SMB_DEST_SUBDIR}"
  if ! command -v smbclient >/dev/null 2>&1; then
    sudo apt-get update -y && sudo apt-get install -y smbclient
  fi
  echo "mkdir ${SMB_DEST_SUBDIR}" | smbclient "${SMB_URL}" "${SMB_PASS}" -U "${SMB_USER}" -c "ls" >/dev/null 2>&1 || true
  smbclient "${SMB_URL}" "${SMB_PASS}" -U "${SMB_USER}" -c "cd ${SMB_DEST_SUBDIR}; put ${ARCHIVE_PATH} ${ARCHIVE_NAME}"
  echo "Upload complete."
else
  echo "SMB upload disabled. Archive is at: ${ARCHIVE_PATH}"
fi
