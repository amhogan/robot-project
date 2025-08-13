FROM ros:iron-ros-base

# Install once at build time (fast container start)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ros-iron-v4l2-camera v4l-utils && \
    rm -rf /var/lib/apt/lists/*

ENV ROS_DISTRO=iron
# Will be overridden via env; default is a common Pi capture node
ENV CAM_DEV=/dev/video20

# Run the driver
CMD bash -lc "source /opt/ros/$ROS_DISTRO/setup.bash && \
              ros2 run v4l2_camera v4l2_camera_node \
                --ros-args \
                -p video_device:=${CAM_DEV} \
                -p output_encoding:=rgb8 \
                -r image:=/image_raw"
