FROM ros:iron-ros-base
RUN bash -lc 'set -e; for i in 1 2 3 4 5; do \
      apt-get update && \
      apt-get install -y --no-install-recommends ros-iron-web-video-server python3 && \
      rm -rf /var/lib/apt/lists/* && exit 0 || sleep 10; \
  done; exit 1'
RUN bash -lc '. /opt/ros/iron/setup.bash && which ros2'
