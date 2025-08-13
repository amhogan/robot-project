FROM ros:iron-ros-base
RUN apt-get update && apt-get install -y --no-install-recommends ros-iron-image-tools && \
    rm -rf /var/lib/apt/lists/*
ENV ROS_DISTRO=iron
CMD bash -lc "source /opt/ros/$ROS_DISTRO/setup.bash && \
              ros2 run image_tools cam2image --ros-args -r image:=/image_raw"
