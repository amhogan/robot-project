cmake_minimum_required(VERSION 3.5)
project(roboclaw_driver)

# Add this line:
find_package(ament_cmake_python REQUIRED)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python package
ament_python_install_package(${PROJECT_NAME})

# Install the executable script
install(PROGRAMS
  roboclaw_driver/roboclaw_driver.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
