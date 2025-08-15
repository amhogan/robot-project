#!/usr/bin/env bash
set -Ee -o pipefail

: "${CAM_DEV:=/dev/video1}"
: "${IMAGE_WIDTH:=640}"
: "${IMAGE_HEIGHT:=480}"
: "${FRAME_RATE:=15.0}"     # default is already a float
: "${PIXEL_FORMAT:=mjpeg}"
: "${IO_METHOD:=mmap}"

# Avoid set -u blowups inside ROS setup
export AMENT_TRACE_SETUP_FILES=${AMENT_TRACE_SETUP_FILES:-}

source /opt/ros/iron/setup.bash

# Ensure FRAME_RATE is a float (usb_cam expects double)
case "$FRAME_RATE" in
  *.*) FR="$FRAME_RATE" ;;
  *)   FR="${FRAME_RATE}.0" ;;
esac

exec ros2 run usb_cam usb_cam_node_exe --ros-args \
  -p video_device:="${CAM_DEV}" \
  -p framerate:="${FR}" \
  -p image_width:="${IMAGE_WIDTH}" \
  -p image_height:="${IMAGE_HEIGHT}" \
  -p pixel_format:="${PIXEL_FORMAT}" \
  -p io_method:="${IO_METHOD}"
