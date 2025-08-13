#!/usr/bin/env bash
set -euo pipefail

export VIDEO_DEVICE="${VIDEO_DEVICE:-/dev/video0}"
export IMAGE_WIDTH="${IMAGE_WIDTH:-640}"
export IMAGE_HEIGHT="${IMAGE_HEIGHT:-480}"
export FRAME_RATE="${FRAME_RATE:-15}"
export IO_METHOD="${IO_METHOD:-mmap}"

# Pick a good pixel format automatically: prefer MJPG on USB, fallback to YUYV
if v4l2-ctl --device="$VIDEO_DEVICE" --list-formats-ext 2>/dev/null | grep -q "MJPG"; then
  PIXEL_FORMAT="${PIXEL_FORMAT:-MJPG}"
else
  PIXEL_FORMAT="${PIXEL_FORMAT:-YUYV}"
fi

# (Optional) show formats at boot for debugging
v4l2-ctl --device="$VIDEO_DEVICE" --list-formats-ext || true

source /opt/ros/iron/setup.bash
exec ros2 run v4l2_camera v4l2_camera_node --ros-args \
  -p video_device:="$VIDEO_DEVICE" \
  -p image_size:="[$IMAGE_WIDTH,$IMAGE_HEIGHT]" \
  -p pixel_format:="$PIXEL_FORMAT" \
  -p io_method:="$IO_METHOD" \
  -p frame_rate:=$FRAME_RATE
