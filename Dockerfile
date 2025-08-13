# Base image with ROS 2 Iron base
FROM ros:iron-ros-base

# Install OpenCV and ROS Python build tools
RUN apt-get update && apt-get install -y \
    ros-iron-cv-bridge \
    python3-opencv \
    python3-colcon-common-extensions \
    python3-pip \
    python3-numpy \
    libboost-all-dev \
    libopencv-dev \
    libopencv-imgproc-dev \
    libopencv-core-dev \
    libopencv-imgcodecs-dev \
    && rm -rf /var/lib/apt/lists/*

# Install ament_python if needed
RUN pip3 install -U setuptools

# Copy the ROS 2 workspace
COPY ../robot_ws /ros2_ws

# Set working directory
WORKDIR /ros2_ws

# Build the workspace with symlink-install
RUN /bin/bash -c "source /opt/ros/iron/setup.bash && colcon build --packages-select opencv_node --symlink-install"

# Source and run the node
CMD ["/bin/bash", "-c", "source /opt/ros/iron/setup.bash && source /ros2_ws/install/setup.bash && ros2 run opencv_node opencv_node"]
