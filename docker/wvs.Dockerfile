FROM ros:iron-ros-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ros-iron-web-video-server ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Simpler healthcheck: just verify port 8080 is listening
HEALTHCHECK --interval=10s --timeout=3s --retries=60 \
  CMD bash -lc 'exec 3<>/dev/tcp/127.0.0.1/8080 || exit 1'

ENV ROS_DISTRO=iron
CMD bash -lc "source /opt/ros/$ROS_DISTRO/setup.bash && \
              ros2 run web_video_server web_video_server --port 8080 --address 0.0.0.0"
