FROM ros:iron-ros-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends ros-iron-v4l2-camera v4l-utils && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# sensible defaults; override in compose if you like
ENV VIDEO_DEVICE=/dev/video0 \
    IMAGE_WIDTH=640 \
    IMAGE_HEIGHT=480 \
    FRAME_RATE=15 \
    IO_METHOD=mmap \
    ROS_DOMAIN_ID=0

ENTRYPOINT ["/entrypoint.sh"]
