# Robot Project Snapshot

- **Generated:** 2025-08-14 14:56:58 UTC
- **Host:** RPi-Robot
- **Git:** `main@e8cf11b`  (remote: git@github.com:amhogan/robot-project.git)

## Directory Tree

```text
./
├── .gitignore
├── Dockerfile
├── Dockerfile.roboclaw
├── Dockerfile.ros-core
├── Dockerfile.usb-camera
├── Makefile
├── README.md
├── STATE.md
├── STATUS.md
├── _snapshots/
│   └── project-snapshot-20250814-145507.md
├── docker/
│   ├── .env -> /home/pi/robot-project/docker/compose/.env
│   ├── camtest.Dockerfile
│   ├── compose/
│   │   ├── .env
│   │   ├── .env.bak.1755138148
│   │   ├── Dockerfile
│   │   ├── Dockerfile.roboclaw
│   │   ├── Dockerfile.ros-core
│   │   ├── Dockerfile.usb-camera
│   │   ├── base.yml
│   │   ├── docker-compose.yml.off
│   │   ├── ros.yml
│   │   ├── ros.yml.bak.1755026774
│   │   ├── ros.yml.bak.1755138148
│   │   ├── test.yml
│   │   ├── web.yml
│   │   └── web.yml.bak
│   ├── docker-compose.yml.old
│   ├── overrides/
│   ├── v412-camera/
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   ├── entrypoint.sh
│   │   ├── entrypoint.sh.bak.1755140136
│   │   └── entrypoint.sh.bak.1755140908
│   ├── v412.Dockerfile
│   ├── v4l2.Dockerfile
│   └── wvs.Dockerfile
├── docker-compose.yml
├── docs/
│   ├── PROGRESS-2025-08-10.md
│   ├── Robot_Project_Design_Document_2025-08-11.pdf
│   ├── status/
│   ├── wiring/
│   └── wiring-diagrams/
├── nginx/
│   └── conf.d/
│       ├── robot-mjpeg.conf
│       ├── robot-mjpeg.conf.bak.1754870742
│       ├── robot-mjpeg.conf.bak.1754870764
│       ├── robot-mjpeg.conf.bak.1754871569
│       ├── robot-mjpeg.conf.bak.1754943379
│       ├── robot-mjpeg.conf.bak.1754943685
│       ├── robot-mjpeg.conf.bak.1754944481
│       ├── robot.conf
│       └── status-proxy.conf.disabled
├── reports/
│   └── 2025-08-12.md
├── robot_ws/
│   ├── Dockerfile.roboclaw
│   └── src/
│       ├── async_web_server_cpp/
│       │   ├── .clang-format
│       │   ├── .github/
│       │   │   └── workflows/
│       │   │       └── main.yml
│       │   ├── CHANGELOG.rst
│       │   ├── CMakeLists.txt
│       │   ├── LICENSE
│       │   ├── README.md
│       │   ├── find_dependencies.cmake.in
│       │   ├── include/
│       │   │   └── async_web_server_cpp/
│       │   │       ├── http_connection.hpp
│       │   │       ├── http_header.hpp
│       │   │       ├── http_reply.hpp
│       │   │       ├── http_request.hpp
│       │   │       ├── http_request_handler.hpp
│       │   │       ├── http_request_parser.hpp
│       │   │       ├── http_server.hpp
│       │   │       ├── websocket_connection.hpp
│       │   │       ├── websocket_message.hpp
│       │   │       └── websocket_request_handler.hpp
│       │   ├── package.xml
│       │   ├── src/
│       │   │   ├── http_connection.cpp
│       │   │   ├── http_reply.cpp
│       │   │   ├── http_request.cpp
│       │   │   ├── http_request_handler.cpp
│       │   │   ├── http_request_parser.cpp
│       │   │   ├── http_server.cpp
│       │   │   ├── websocket_connection.cpp
│       │   │   ├── websocket_message.cpp
│       │   │   └── websocket_request_handler.cpp
│       │   └── test/
│       │       ├── CMakeLists.txt
│       │       ├── simple_http_requests_test.py*
│       │       ├── test.html
│       │       ├── test_dir/
│       │       │   └── test_file.txt
│       │       ├── test_web_server.cpp
│       │       ├── tests.py.in*
│       │       └── websocket_test.py*
│       ├── demos/
│       │   ├── .github/
│       │   │   ├── ISSUE_TEMPLATE.md
│       │   │   └── workflows/
│       │   │       └── mirror-rolling-to-master.yaml
│       │   ├── .gitignore
│       │   ├── CODEOWNERS
│       │   ├── CONTRIBUTING.md
│       │   ├── LICENSE
│       │   ├── README.md
│       │   ├── action_tutorials/
│       │   │   ├── README.md
│       │   │   ├── action_tutorials_cpp/
│       │   │   │   ├── CHANGELOG.rst
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── README.md
│       │   │   │   ├── include/
│       │   │   │   │   └── action_tutorials_cpp/
│       │   │   │   │       └── visibility_control.h
│       │   │   │   ├── package.xml
│       │   │   │   └── src/
│       │   │   │       ├── fibonacci_action_client.cpp
│       │   │   │       └── fibonacci_action_server.cpp
│       │   │   ├── action_tutorials_interfaces/
│       │   │   │   ├── CHANGELOG.rst
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── README.md
│       │   │   │   ├── action/
│       │   │   │   │   └── Fibonacci.action
│       │   │   │   └── package.xml
│       │   │   └── action_tutorials_py/
│       │   │       ├── CHANGELOG.rst
│       │   │       ├── README.md
│       │   │       ├── action_tutorials_py/
│       │   │       │   ├── __init__.py
│       │   │       │   ├── fibonacci_action_client.py*
│       │   │       │   └── fibonacci_action_server.py*
│       │   │       ├── package.xml
│       │   │       ├── resource/
│       │   │       │   └── action_tutorials_py
│       │   │       ├── setup.cfg
│       │   │       └── setup.py
│       │   ├── composition/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── Doxyfile
│       │   │   ├── README.md
│       │   │   ├── include/
│       │   │   │   └── composition/
│       │   │   │       ├── client_component.hpp
│       │   │   │       ├── listener_component.hpp
│       │   │   │       ├── node_like_listener_component.hpp
│       │   │   │       ├── server_component.hpp
│       │   │   │       ├── talker_component.hpp
│       │   │   │       └── visibility_control.h
│       │   │   ├── launch/
│       │   │   │   └── composition_demo_launch.py
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── client_component.cpp
│       │   │   │   ├── dlopen_composition.cpp
│       │   │   │   ├── linktime_composition.cpp
│       │   │   │   ├── listener_component.cpp
│       │   │   │   ├── manual_composition.cpp
│       │   │   │   ├── node_like_listener_component.cpp
│       │   │   │   ├── server_component.cpp
│       │   │   │   └── talker_component.cpp
│       │   │   └── test/
│       │   │       ├── composition_all.regex
│       │   │       ├── composition_pubsub.regex
│       │   │       ├── composition_srv.regex
│       │   │       ├── test_api_pubsub_composition.py.in
│       │   │       ├── test_api_srv_composition.py.in
│       │   │       ├── test_api_srv_composition_client_first.py.in
│       │   │       ├── test_dlopen_composition.py.in
│       │   │       ├── test_linktime_composition.py.in
│       │   │       └── test_manual_composition.py.in
│       │   ├── demo_nodes_cpp/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.md
│       │   │   ├── img/
│       │   │   │   ├── allocator_tutorial.png
│       │   │   │   ├── content_filtering_messaging.png
│       │   │   │   ├── even_parameters_node.png
│       │   │   │   ├── one_off_timer.png
│       │   │   │   ├── parameter_blackboard.png
│       │   │   │   ├── serialized_messaging.png
│       │   │   │   ├── server_client.png
│       │   │   │   └── talker_listener.png
│       │   │   ├── include/
│       │   │   │   └── demo_nodes_cpp/
│       │   │   │       └── visibility_control.h
│       │   │   ├── launch/
│       │   │   │   ├── services/
│       │   │   │   │   ├── add_two_ints_async_launch.py
│       │   │   │   │   ├── add_two_ints_async_launch.xml
│       │   │   │   │   ├── add_two_ints_launch.py
│       │   │   │   │   ├── add_two_ints_launch.xml
│       │   │   │   │   └── introspect_services_launch.py
│       │   │   │   └── topics/
│       │   │   │       ├── talker_listener_best_effort_launch.py
│       │   │   │       ├── talker_listener_best_effort_launch.xml
│       │   │   │       ├── talker_listener_best_effort_launch.yaml
│       │   │   │       ├── talker_listener_launch.py
│       │   │   │       ├── talker_listener_launch.xml
│       │   │   │       └── talker_listener_launch.yaml
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── events/
│       │   │   │   │   └── matched_event_detect.cpp
│       │   │   │   ├── parameters/
│       │   │   │   │   ├── even_parameters_node.cpp
│       │   │   │   │   ├── list_parameters.cpp
│       │   │   │   │   ├── list_parameters_async.cpp
│       │   │   │   │   ├── parameter_blackboard.cpp
│       │   │   │   │   ├── parameter_event_handler.cpp
│       │   │   │   │   ├── parameter_events.cpp
│       │   │   │   │   ├── parameter_events_async.cpp
│       │   │   │   │   ├── set_and_get_parameters.cpp
│       │   │   │   │   ├── set_and_get_parameters_async.cpp
│       │   │   │   │   └── set_parameters_callback.cpp
│       │   │   │   ├── services/
│       │   │   │   │   ├── add_two_ints_client.cpp
│       │   │   │   │   ├── add_two_ints_client_async.cpp
│       │   │   │   │   ├── add_two_ints_server.cpp
│       │   │   │   │   ├── introspection_client.cpp
│       │   │   │   │   └── introspection_service.cpp
│       │   │   │   ├── timers/
│       │   │   │   │   ├── one_off_timer.cpp
│       │   │   │   │   └── reuse_timer.cpp
│       │   │   │   └── topics/
│       │   │   │       ├── allocator_tutorial.cpp
│       │   │   │       ├── content_filtering_publisher.cpp
│       │   │   │       ├── content_filtering_subscriber.cpp
│       │   │   │       ├── listener.cpp
│       │   │   │       ├── listener_best_effort.cpp
│       │   │   │       ├── listener_serialized_message.cpp
│       │   │   │       ├── talker.cpp
│       │   │   │       ├── talker_loaned_message.cpp
│       │   │   │       └── talker_serialized_message.cpp
│       │   │   └── test/
│       │   │       ├── add_two_ints_client.txt
│       │   │       ├── add_two_ints_client_async.txt
│       │   │       ├── add_two_ints_server.txt
│       │   │       ├── content_filtering_publisher.txt
│       │   │       ├── content_filtering_subscriber-rmw_connextdds.txt
│       │   │       ├── content_filtering_subscriber-rmw_fastrtps_cpp.txt
│       │   │       ├── content_filtering_subscriber.txt
│       │   │       ├── list_parameters.txt
│       │   │       ├── list_parameters_async.txt
│       │   │       ├── listener.regex
│       │   │       ├── matched_event_detect.txt
│       │   │       ├── parameter_events.txt
│       │   │       ├── parameter_events_async.txt
│       │   │       ├── set_and_get_parameters.txt
│       │   │       ├── set_and_get_parameters_async.txt
│       │   │       ├── talker.txt
│       │   │       └── test_executables_tutorial.py.in
│       │   ├── demo_nodes_cpp_native/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.md
│       │   │   ├── include/
│       │   │   │   └── demo_nodes_cpp_native/
│       │   │   │       └── visibility_control.h
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   └── talker.cpp
│       │   │   └── test/
│       │   │       ├── talker.regex
│       │   │       └── test_executables_tutorial.py.in
│       │   ├── demo_nodes_py/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── README.md
│       │   │   ├── demo_nodes_py/
│       │   │   │   ├── __init__.py
│       │   │   │   ├── events/
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   └── matched_event_detect.py
│       │   │   │   ├── parameters/
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── async_param_client.py
│       │   │   │   │   ├── params.yaml
│       │   │   │   │   └── set_parameters_callback.py
│       │   │   │   ├── services/
│       │   │   │   │   ├── __init__.py
│       │   │   │   │   ├── add_two_ints_client.py
│       │   │   │   │   ├── add_two_ints_client_async.py
│       │   │   │   │   ├── add_two_ints_server.py
│       │   │   │   │   └── introspection.py
│       │   │   │   └── topics/
│       │   │   │       ├── __init__.py
│       │   │   │       ├── listener.py
│       │   │   │       ├── listener_qos.py
│       │   │   │       ├── listener_serialized.py
│       │   │   │       ├── talker.py
│       │   │   │       └── talker_qos.py
│       │   │   ├── img/
│       │   │   │   ├── qos_listener_talker.png
│       │   │   │   ├── serialized_subscriber.png
│       │   │   │   ├── server_client.png
│       │   │   │   ├── set_parameters_callback.png
│       │   │   │   └── talker_listener.png
│       │   │   ├── package.xml
│       │   │   ├── resource/
│       │   │   │   └── demo_nodes_py
│       │   │   ├── setup.cfg
│       │   │   ├── setup.py
│       │   │   └── test/
│       │   │       ├── test_copyright.py
│       │   │       ├── test_flake8.py
│       │   │       └── test_pep257.py
│       │   ├── dummy_robot/
│       │   │   ├── dummy_map_server/
│       │   │   │   ├── CHANGELOG.rst
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── README.md
│       │   │   │   ├── img/
│       │   │   │   │   └── occupancy_grid.png
│       │   │   │   ├── package.xml
│       │   │   │   └── src/
│       │   │   │       └── dummy_map_server.cpp
│       │   │   ├── dummy_robot_bringup/
│       │   │   │   ├── CHANGELOG.rst
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── config/
│       │   │   │   │   └── dummy_robot.rviz
│       │   │   │   ├── launch/
│       │   │   │   │   ├── dummy_robot_bringup_launch.py*
│       │   │   │   │   ├── dummy_robot_bringup_launch.xml
│       │   │   │   │   ├── dummy_robot_bringup_launch.yaml
│       │   │   │   │   └── single_rrbot.urdf
│       │   │   │   └── package.xml
│       │   │   └── dummy_sensors/
│       │   │       ├── CHANGELOG.rst
│       │   │       ├── CMakeLists.txt
│       │   │       ├── README.md
│       │   │       ├── package.xml
│       │   │       └── src/
│       │   │           ├── dummy_joint_states.cpp
│       │   │           └── dummy_laser.cpp
│       │   ├── image_tools/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── Doxyfile
│       │   │   ├── README.md
│       │   │   ├── doc/
│       │   │   │   └── qos-best-effort.png
│       │   │   ├── img/
│       │   │   │   └── result.png
│       │   │   ├── include/
│       │   │   │   └── image_tools/
│       │   │   │       ├── cv_mat_sensor_msgs_image_type_adapter.hpp
│       │   │   │       └── visibility_control.h
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── burger.cpp
│       │   │   │   ├── burger.hpp
│       │   │   │   ├── cam2image.cpp
│       │   │   │   ├── cv_mat_sensor_msgs_image_type_adapter.cpp
│       │   │   │   ├── policy_maps.hpp
│       │   │   │   └── showimage.cpp
│       │   │   └── test/
│       │   │       ├── cam2image.txt
│       │   │       ├── showimage.regex
│       │   │       └── test_executables_demo.py.in
│       │   ├── intra_process_demo/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.md
│       │   │   ├── img/
│       │   │   │   ├── image_pipeline_all_in_one.png
│       │   │   │   ├── image_pipeline_all_in_one_rqtgraph.png
│       │   │   │   ├── image_pipeline_all_separately.png
│       │   │   │   ├── image_pipeline_with_two_image_views.png
│       │   │   │   ├── image_pipeline_with_two_image_views_rqtgraph.png
│       │   │   │   └── two_node_pipeline.png
│       │   │   ├── include/
│       │   │   │   └── image_pipeline/
│       │   │   │       ├── camera_node.hpp
│       │   │   │       ├── common.hpp
│       │   │   │       ├── image_view_node.hpp
│       │   │   │       └── watermark_node.hpp
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── cyclic_pipeline/
│       │   │   │   │   └── cyclic_pipeline.cpp
│       │   │   │   ├── image_pipeline/
│       │   │   │   │   ├── camera_node.cpp
│       │   │   │   │   ├── image_pipeline_all_in_one.cpp
│       │   │   │   │   ├── image_pipeline_with_two_image_view.cpp
│       │   │   │   │   ├── image_view_node.cpp
│       │   │   │   │   └── watermark_node.cpp
│       │   │   │   └── two_node_pipeline/
│       │   │   │       └── two_node_pipeline.cpp
│       │   │   └── test/
│       │   │       ├── cyclic_pipeline.regex
│       │   │       ├── test_executables_demo.py.in
│       │   │       └── two_node_pipeline.regex
│       │   ├── lifecycle/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.rst
│       │   │   ├── launch/
│       │   │   │   └── lifecycle_demo_launch.py*
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── lifecycle_listener.cpp
│       │   │   │   ├── lifecycle_service_client.cpp
│       │   │   │   └── lifecycle_talker.cpp
│       │   │   └── test/
│       │   │       └── test_lifecycle.py
│       │   ├── lifecycle_py/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── README.rst
│       │   │   ├── launch/
│       │   │   │   └── lifecycle_demo_launch.py*
│       │   │   ├── lifecycle_py/
│       │   │   │   ├── __init__.py
│       │   │   │   └── talker.py
│       │   │   ├── package.xml
│       │   │   ├── resource/
│       │   │   │   └── lifecycle_py
│       │   │   ├── setup.cfg
│       │   │   ├── setup.py
│       │   │   └── test/
│       │   │       ├── test_copyright.py
│       │   │       ├── test_flake8.py
│       │   │       ├── test_lifecycle.py
│       │   │       └── test_pep257.py
│       │   ├── logging_demo/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── Doxyfile
│       │   │   ├── include/
│       │   │   │   └── logging_demo/
│       │   │   │       ├── logger_config_component.hpp
│       │   │   │       ├── logger_usage_component.hpp
│       │   │   │       └── visibility_control.h
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── logger_config_component.cpp
│       │   │   │   ├── logger_usage_component.cpp
│       │   │   │   └── logging_demo_main.cpp
│       │   │   ├── srv/
│       │   │   │   └── ConfigLogger.srv
│       │   │   └── test/
│       │   │       ├── logging_demo_main_debug_severity.txt
│       │   │       ├── logging_demo_main_default_severity.txt
│       │   │       └── test_logging_demo.py.in
│       │   ├── pendulum_control/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.md
│       │   │   ├── include/
│       │   │   │   └── pendulum_control/
│       │   │   │       ├── pendulum_controller.hpp
│       │   │   │       ├── pendulum_motor.hpp
│       │   │   │       └── rtt_executor.hpp
│       │   │   ├── package.xml
│       │   │   ├── scripts/
│       │   │   │   └── pendulum_launch.bash*
│       │   │   ├── src/
│       │   │   │   ├── pendulum_demo.cpp
│       │   │   │   ├── pendulum_logger.cpp
│       │   │   │   └── pendulum_teleop.cpp
│       │   │   └── test/
│       │   │       ├── execute_with_delay.py*
│       │   │       ├── pendulum_demo.regex
│       │   │       ├── pendulum_demo_teleop.regex
│       │   │       ├── pendulum_logger.regex
│       │   │       ├── pendulum_teleop.txt
│       │   │       ├── test_pendulum_demo.py.in
│       │   │       └── test_pendulum_teleop.py.in
│       │   ├── pendulum_msgs/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.md
│       │   │   ├── msg/
│       │   │   │   ├── JointCommand.msg
│       │   │   │   ├── JointState.msg
│       │   │   │   └── RttestResults.msg
│       │   │   └── package.xml
│       │   ├── pytest.ini
│       │   ├── quality_of_service_demo/
│       │   │   ├── README.md
│       │   │   ├── rclcpp/
│       │   │   │   ├── CHANGELOG.rst
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── include/
│       │   │   │   │   └── quality_of_service_demo/
│       │   │   │   │       ├── common_nodes.hpp
│       │   │   │   │       └── visibility_control.h
│       │   │   │   ├── package.xml
│       │   │   │   ├── params_file/
│       │   │   │   │   ├── example_qos_overrides.yaml
│       │   │   │   │   └── example_qos_overrides_with_wildcard.yaml
│       │   │   │   └── src/
│       │   │   │       ├── common_nodes.cpp
│       │   │   │       ├── deadline.cpp
│       │   │   │       ├── incompatible_qos.cpp
│       │   │   │       ├── interactive_publisher.cpp
│       │   │   │       ├── interactive_subscriber.cpp
│       │   │   │       ├── lifespan.cpp
│       │   │   │       ├── liveliness.cpp
│       │   │   │       ├── message_lost_listener.cpp
│       │   │   │       ├── message_lost_talker.cpp
│       │   │   │       ├── qos_overrides_listener.cpp
│       │   │   │       ├── qos_overrides_talker.cpp
│       │   │   │       ├── utils.cpp
│       │   │   │       └── utils.hpp
│       │   │   └── rclpy/
│       │   │       ├── .gitignore
│       │   │       ├── CHANGELOG.rst
│       │   │       ├── package.xml
│       │   │       ├── quality_of_service_demo_py/
│       │   │       │   ├── __init__.py
│       │   │       │   ├── common_nodes.py
│       │   │       │   ├── deadline.py
│       │   │       │   ├── incompatible_qos.py
│       │   │       │   ├── lifespan.py
│       │   │       │   ├── liveliness.py
│       │   │       │   ├── message_lost_listener.py
│       │   │       │   ├── qos_overrides_listener.py
│       │   │       │   └── qos_overrides_talker.py
│       │   │       ├── resource/
│       │   │       │   └── quality_of_service_demo_py
│       │   │       ├── setup.cfg
│       │   │       ├── setup.py
│       │   │       └── test/
│       │   │           └── test_linters.py
│       │   ├── topic_monitor/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── README.md
│       │   │   ├── doc/
│       │   │   │   ├── message_size_comparison.png
│       │   │   │   └── reliability_comparison.png
│       │   │   ├── launch/
│       │   │   │   ├── depth_demo_launch.py
│       │   │   │   ├── fragmentation_demo_launch.py
│       │   │   │   └── reliability_demo_launch.py
│       │   │   ├── package.xml
│       │   │   ├── resource/
│       │   │   │   └── topic_monitor
│       │   │   ├── setup.cfg
│       │   │   ├── setup.py
│       │   │   ├── test/
│       │   │   │   ├── test_flake8.py
│       │   │   │   └── test_pep257.py
│       │   │   └── topic_monitor/
│       │   │       ├── README.md
│       │   │       ├── __init__.py
│       │   │       └── scripts/
│       │   │           ├── __init__.py
│       │   │           ├── data_publisher.py*
│       │   │           └── topic_monitor.py*
│       │   └── topic_statistics_demo/
│       │       ├── CHANGELOG.rst
│       │       ├── CMakeLists.txt
│       │       ├── README.md
│       │       ├── include/
│       │       │   └── topic_statistics_demo/
│       │       │       ├── imu_talker_listener_nodes.hpp
│       │       │       ├── string_talker_listener_nodes.hpp
│       │       │       └── topic_statistics_listener.hpp
│       │       ├── package.xml
│       │       └── src/
│       │           ├── display_topic_statistics.cpp
│       │           ├── imu_talker_listener_nodes.cpp
│       │           ├── string_talker_listener_nodes.cpp
│       │           └── topic_statistics_listener.cpp
│       ├── image_common/
│       │   ├── .github/
│       │   │   └── workflows/
│       │   │       └── mirror-rolling-to-ros2.yaml
│       │   ├── .gitignore
│       │   ├── camera_calibration_parsers/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── include/
│       │   │   │   └── camera_calibration_parsers/
│       │   │   │       ├── parse.h
│       │   │   │       ├── parse.hpp
│       │   │   │       ├── parse_ini.h
│       │   │   │       ├── parse_ini.hpp
│       │   │   │       ├── parse_yml.h
│       │   │   │       ├── parse_yml.hpp
│       │   │   │       └── visibility_control.hpp
│       │   │   ├── mainpage.dox
│       │   │   ├── package.xml
│       │   │   ├── setup.py
│       │   │   ├── src/
│       │   │   │   ├── camera_calibration_parsers/
│       │   │   │   │   └── __init__.py
│       │   │   │   ├── convert.cpp
│       │   │   │   ├── parse.cpp
│       │   │   │   ├── parse_ini.cpp
│       │   │   │   ├── parse_wrapper.cpp
│       │   │   │   └── parse_yml.cpp
│       │   │   └── test/
│       │   │       ├── CMakeLists.txt
│       │   │       ├── calib5.ini
│       │   │       ├── calib8.ini
│       │   │       ├── make_calibs.hpp
│       │   │       ├── parser.py
│       │   │       ├── test_parse_ini.cpp
│       │   │       └── test_parse_yml.cpp
│       │   ├── camera_info_manager/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── include/
│       │   │   │   └── camera_info_manager/
│       │   │   │       ├── camera_info_manager.h
│       │   │   │       ├── camera_info_manager.hpp
│       │   │   │       └── visibility_control.h
│       │   │   ├── mainpage.dox
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── camera_info_manager.cpp
│       │   │   │   └── split.hpp
│       │   │   └── tests/
│       │   │       ├── test_calibration.yaml
│       │   │       ├── unit_test.cpp
│       │   │       └── unit_test.test
│       │   ├── image_common/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   └── package.xml
│       │   ├── image_transport/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── default_plugins.xml
│       │   │   ├── include/
│       │   │   │   └── image_transport/
│       │   │   │       ├── camera_common.h
│       │   │   │       ├── camera_common.hpp
│       │   │   │       ├── camera_publisher.h
│       │   │   │       ├── camera_publisher.hpp
│       │   │   │       ├── camera_subscriber.h
│       │   │   │       ├── camera_subscriber.hpp
│       │   │   │       ├── exception.h
│       │   │   │       ├── exception.hpp
│       │   │   │       ├── image_transport.h
│       │   │   │       ├── image_transport.hpp
│       │   │   │       ├── loader_fwds.h
│       │   │   │       ├── loader_fwds.hpp
│       │   │   │       ├── publisher.h
│       │   │   │       ├── publisher.hpp
│       │   │   │       ├── publisher_plugin.h
│       │   │   │       ├── publisher_plugin.hpp
│       │   │   │       ├── raw_publisher.h
│       │   │   │       ├── raw_publisher.hpp
│       │   │   │       ├── raw_subscriber.h
│       │   │   │       ├── raw_subscriber.hpp
│       │   │   │       ├── simple_publisher_plugin.h
│       │   │   │       ├── simple_publisher_plugin.hpp
│       │   │   │       ├── simple_subscriber_plugin.h
│       │   │   │       ├── simple_subscriber_plugin.hpp
│       │   │   │       ├── single_subscriber_publisher.h
│       │   │   │       ├── single_subscriber_publisher.hpp
│       │   │   │       ├── subscriber.h
│       │   │   │       ├── subscriber.hpp
│       │   │   │       ├── subscriber_filter.h
│       │   │   │       ├── subscriber_filter.hpp
│       │   │   │       ├── subscriber_plugin.h
│       │   │   │       ├── subscriber_plugin.hpp
│       │   │   │       ├── transport_hints.h
│       │   │   │       ├── transport_hints.hpp
│       │   │   │       └── visibility_control.hpp
│       │   │   ├── mainpage.dox
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── camera_common.cpp
│       │   │   │   ├── camera_publisher.cpp
│       │   │   │   ├── camera_subscriber.cpp
│       │   │   │   ├── image_transport.cpp
│       │   │   │   ├── list_transports.cpp
│       │   │   │   ├── manifest.cpp
│       │   │   │   ├── publisher.cpp
│       │   │   │   ├── republish.cpp
│       │   │   │   ├── single_subscriber_publisher.cpp
│       │   │   │   └── subscriber.cpp
│       │   │   └── test/
│       │   │       ├── test_camera_common.cpp
│       │   │       ├── test_message_passing.cpp
│       │   │       ├── test_publisher.cpp
│       │   │       ├── test_qos_override.cpp
│       │   │       ├── test_remapping.cpp
│       │   │       ├── test_single_subscriber_publisher.cpp
│       │   │       ├── test_subscriber.cpp
│       │   │       └── utils.hpp
│       │   └── polled_camera/
│       │       ├── CHANGELOG.rst
│       │       ├── CMakeLists.txt
│       │       ├── COLCON_IGNORE
│       │       ├── include/
│       │       │   └── polled_camera/
│       │       │       └── publication_server.h
│       │       ├── mainpage.dox
│       │       ├── package.xml
│       │       ├── src/
│       │       │   ├── poller.cpp
│       │       │   └── publication_server.cpp
│       │       └── srv/
│       │           └── GetPolledImage.srv
│       ├── opencv_node/
│       │   ├── opencv_node/
│       │   │   ├── .opencv_node.py.swp
│       │   │   ├── __init__.py
│       │   │   └── opencv_node.py*
│       │   ├── package.xml
│       │   ├── resource/
│       │   │   └── opencv_node
│       │   ├── setup.cfg
│       │   └── setup.py
│       ├── roboclaw_driver/
│       │   ├── CMakeLists.txt
│       │   ├── package.xml
│       │   ├── resource/
│       │   │   └── roboclaw_driver
│       │   ├── roboclaw_driver/
│       │   │   ├── __init__.py
│       │   │   └── roboclaw_driver.py
│       │   ├── setup.cfg
│       │   └── setup.py
│       ├── robot_ws/
│       ├── vision_opencv/
│       │   ├── .gitignore
│       │   ├── LICENSE-Apache
│       │   ├── LICENSE-BSD
│       │   ├── README.md
│       │   ├── cv_bridge/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── README.md
│       │   │   ├── cmake/
│       │   │   │   └── cv_bridge-extras.cmake.in
│       │   │   ├── doc/
│       │   │   │   ├── conf.py
│       │   │   │   ├── index.rst
│       │   │   │   └── mainpage.dox
│       │   │   ├── include/
│       │   │   │   └── cv_bridge/
│       │   │   │       ├── cv_bridge.h
│       │   │   │       ├── cv_bridge.hpp
│       │   │   │       ├── cv_mat_sensor_msgs_image_type_adapter.hpp
│       │   │   │       ├── rgb_colors.h
│       │   │   │       ├── rgb_colors.hpp
│       │   │   │       └── visibility_control.h
│       │   │   ├── package.xml
│       │   │   ├── python/
│       │   │   │   └── cv_bridge/
│       │   │   │       ├── __init__.py
│       │   │   │       └── core.py
│       │   │   ├── src/
│       │   │   │   ├── CMakeLists.txt
│       │   │   │   ├── cv_bridge.cpp
│       │   │   │   ├── cv_mat_sensor_msgs_image_type_adapter.cpp
│       │   │   │   ├── module.cpp
│       │   │   │   ├── module.hpp
│       │   │   │   ├── module_opencv4.cpp
│       │   │   │   ├── pycompat.hpp
│       │   │   │   └── rgb_colors.cpp
│       │   │   └── test/
│       │   │       ├── CMakeLists.txt
│       │   │       ├── conversions.py
│       │   │       ├── enumerants.py
│       │   │       ├── python_bindings.py
│       │   │       ├── test_compression.cpp
│       │   │       ├── test_dynamic_scaling.cpp
│       │   │       ├── test_endian.cpp
│       │   │       ├── test_rgb_colors.cpp
│       │   │       ├── utest.cpp
│       │   │       └── utest2.cpp
│       │   ├── image_geometry/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── CMakeLists.txt
│       │   │   ├── doc/
│       │   │   │   ├── conf.py
│       │   │   │   ├── index.rst
│       │   │   │   └── mainpage.dox
│       │   │   ├── image_geometry/
│       │   │   │   ├── __init__.py
│       │   │   │   └── cameramodels.py
│       │   │   ├── include/
│       │   │   │   └── image_geometry/
│       │   │   │       ├── pinhole_camera_model.h
│       │   │   │       ├── pinhole_camera_model.hpp
│       │   │   │       ├── stereo_camera_model.h
│       │   │   │       ├── stereo_camera_model.hpp
│       │   │   │       └── visibility_control.hpp
│       │   │   ├── package.xml
│       │   │   ├── src/
│       │   │   │   ├── pinhole_camera_model.cpp
│       │   │   │   └── stereo_camera_model.cpp
│       │   │   └── test/
│       │   │       ├── CMakeLists.txt
│       │   │       ├── directed.py
│       │   │       ├── utest.cpp
│       │   │       └── utest_equi.cpp
│       │   ├── opencv_tests/
│       │   │   ├── CHANGELOG.rst
│       │   │   ├── launch/
│       │   │   │   └── view_img.py
│       │   │   ├── mainpage.dox
│       │   │   ├── opencv_tests/
│       │   │   │   ├── __init__.py
│       │   │   │   ├── broadcast.py*
│       │   │   │   ├── rosfacedetect.py*
│       │   │   │   └── source.py*
│       │   │   ├── package.xml
│       │   │   ├── resource/
│       │   │   │   └── opencv_tests
│       │   │   ├── setup.cfg
│       │   │   └── setup.py
│       │   ├── pytest.ini
│       │   └── vision_opencv/
│       │       ├── CHANGELOG.rst
│       │       ├── CMakeLists.txt
│       │       └── package.xml
│       └── web_video_server/
│           ├── .github/
│           │   └── workflows/
│           │       └── ci.yml
│           ├── .gitignore
│           ├── AUTHORS.md
│           ├── CHANGELOG.rst
│           ├── CMakeLists.txt
│           ├── CONTRIBUTING.md
│           ├── LICENSE
│           ├── README.md
│           ├── include/
│           │   └── web_video_server/
│           │       ├── h264_streamer.hpp
│           │       ├── image_streamer.hpp
│           │       ├── jpeg_streamers.hpp
│           │       ├── libav_streamer.hpp
│           │       ├── multipart_stream.hpp
│           │       ├── png_streamers.hpp
│           │       ├── ros_compressed_streamer.hpp
│           │       ├── utils.hpp
│           │       ├── vp8_streamer.hpp
│           │       ├── vp9_streamer.hpp
│           │       └── web_video_server.hpp
│           ├── mainpage.dox
│           ├── package.xml
│           └── src/
│               ├── h264_streamer.cpp
│               ├── image_streamer.cpp
│               ├── jpeg_streamers.cpp
│               ├── libav_streamer.cpp
│               ├── multipart_stream.cpp
│               ├── png_streamers.cpp
│               ├── ros_compressed_streamer.cpp
│               ├── utils.cpp
│               ├── vp8_streamer.cpp
│               ├── vp9_streamer.cpp
│               ├── web_video_server.cpp
│               └── web_video_server_node.cpp
├── ros2_ws/
│   └── src/
├── scripts/
│   ├── backup_robot.sh*
│   ├── backup_to_github.sh*
│   ├── consolidate_and_update.sh*
│   ├── consolidate_and_update_state.sh*
│   ├── make_project_snapshot.sh*
│   └── prune_docker.sh*
├── services/
│   ├── netstatus/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   ├── app.py.bak.1754942315
│   │   └── requirements.txt
│   └── web-video-server/
│       └── Dockerfile
├── site/
│   ├── index.html
│   ├── index.html.bak.1755028903
│   ├── index.html.bak.1755110298
│   ├── index.html.bak.1755133268
│   ├── index.html.bak.1755133494
│   ├── index.html.bak.1755133772
│   ├── nginx/
│   │   └── conf.d/
│   │       └── robot.conf
│   ├── robot-mjpeg.conf
│   ├── robot-netstatus.conf
│   └── test_mjpeg.html
└── tools/
    └── commit-today.sh*

209 directories, 689 files
```

## Index

 1. [README.md](#file-readme.md)
 2. [STATE.md](#file-state.md)
 3. [docker/.env](#file-docker--.env)
 4. [docker/compose/.env](#file-docker--compose--.env)
 5. [docker/compose/Dockerfile](#file-docker--compose--dockerfile)
 6. [docker/compose/base.yml](#file-docker--compose--base.yml)
 7. [docker/compose/ros.yml](#file-docker--compose--ros.yml)
 8. [docker/compose/test.yml](#file-docker--compose--test.yml)
 9. [docker/compose/web.yml](#file-docker--compose--web.yml)
10. [docker/v412-camera/Dockerfile](#file-docker--v412-camera--dockerfile)
11. [docker/v412-camera/docker-compose.yml](#file-docker--v412-camera--docker-compose.yml)
12. [nginx/conf.d/robot-mjpeg.conf](#file-nginx--conf.d--robot-mjpeg.conf)
13. [nginx/conf.d/robot.conf](#file-nginx--conf.d--robot.conf)
14. [scripts/backup_robot.sh](#file-scripts--backup_robot.sh)
15. [scripts/backup_to_github.sh](#file-scripts--backup_to_github.sh)
16. [scripts/consolidate_and_update.sh](#file-scripts--consolidate_and_update.sh)
17. [scripts/consolidate_and_update_state.sh](#file-scripts--consolidate_and_update_state.sh)
18. [scripts/make_project_snapshot.sh](#file-scripts--make_project_snapshot.sh)
19. [scripts/prune_docker.sh](#file-scripts--prune_docker.sh)
20. [services/netstatus/app.py](#file-services--netstatus--app.py)
21. [services/netstatus/requirements.txt](#file-services--netstatus--requirements.txt)
22. [site/index.html](#file-site--index.html)
23. [site/nginx/conf.d/robot.conf](#file-site--nginx--conf.d--robot.conf)
24. [site/test_mjpeg.html](#file-site--test_mjpeg.html)

---

### File: README.md {#file-readme.md}

```markdown
# Robot Project

Containers + ROS 2 for a Raspberry Pi 5–based robot with a simple web dashboard.

## Repo layout


## Quick start
```bash
# build + run services
docker build -t netstatus:dev services/netstatus
cd docker
docker compose up -d
# Dashboard → http://<RPi-Robot>:8081/

exit



```

---

### File: STATE.md {#file-state.md}

```markdown
# Robot Project Status Report
**Date:** 2025-08-10  
**System:** RPi-Robot (Raspberry Pi 5, Ubuntu, Docker, ROS 2 Iron)

## 1. Current Working Components
- Video Stream: operational via web_video_server (`/stream?topic=/camera/image_raw`).
- System Metrics: CPU temperature + uptime displayed correctly.
- Networking: Nginx proxy healthy; dashboard reachable; inter-container DNS OK.

## 2. Partially Working / In Progress
- Dashboard Stats: CPU%, memory%, disk% placeholders still blank.
- netstatus: serving temp/uptime; needs more metrics endpoints.
- RoboClaw: in bootloader recovery; USB recognized; Motion Studio pending.

## 3. Outstanding Issues
1) Extend netstatus to expose CPU%, Mem%, Disk%, (optional) Net I/O.
2) Complete RoboClaw firmware recovery and regain motor control.
3) Verify all containers restart on boot.
4) Add backup automation via systemd timer (script exists).

## 4. Next Steps
- Short-term: expand netstatus; wire up dashboard; retest.
- Long-term: GPS integration; patrol/security features; manual driving controls.


## ✅ Completed Since Last Update
- 2025-08-12 – CHECK FAIL: Web Video Server streams not reachable at http://localhost:8080/streams.
- 2025-08-12 – CHECK PASS: Netstatus via Nginx reachable at http://localhost:8081/status.
- 2025-08-12 – CHECK PASS: Dashboard root reachable at http://localhost:8081/.
- 2025-08-12 – Added convenience links: `/home/pi/robot-docker.new` and `/home/pi/robot-dashboard.new`.
- 2025-08-12 – Consolidated repos into `/home/pi/robot-project` monorepo layout.
- 2025-08-12 – Created `Makefile` (make up / logs / rebuild / ps / restart).
- 2025-08-12 – Added `docker/.env` with default ports.
- 2025-08-12 – Created compose scaffold: `docker/compose/ros.yml`.
- 2025-08-12 – Created compose scaffold: `docker/compose/web.yml`.
- 2025-08-12 – Created compose scaffold: `docker/compose/base.yml`.
- 2025-08-12 – Migrated ROS 2 workspace: `/home/pi/robot-docker/robot_ws` → `/home/pi/robot-project/robot_ws`.
- 2025-08-12 – Migrated dashboard static files: `/home/pi/robot-dashboard` → `/home/pi/robot-project/site`.

```

---

### File: docker/.env {#file-docker--.env}

```text
PROJECT_ROOT=/home/pi/robot-project
DASHBOARD_PORT=8081
WVS_PORT=8080
CAM_DEV=/dev/video1

```

---

### File: docker/compose/.env {#file-docker--compose--.env}

```text
PROJECT_ROOT=/home/pi/robot-project
DASHBOARD_PORT=8081
WVS_PORT=8080
CAM_DEV=/dev/video1

```

---

### File: docker/compose/Dockerfile {#file-docker--compose--dockerfile}

```
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

```

---

### File: docker/compose/base.yml {#file-docker--compose--base.yml}

```yaml
name: robot

services: {}

networks:
  robot-net: {}

volumes:
  robot-data: {}

```

---

### File: docker/compose/ros.yml {#file-docker--compose--ros.yml}

```yaml
name: robot

services:
  ros-core:
    image: ros:iron-ros-core
    restart: unless-stopped
    networks: [robot-net]
    command: ["bash","-lc","source /opt/ros/iron/setup.bash && sleep infinity"]
    environment:
      - ROS_DOMAIN_ID=0

  web-video-server:
    build:
      context: ${PROJECT_ROOT}
      dockerfile: docker/wvs.Dockerfile
    restart: unless-stopped
    networks: [robot-net]
    ports: ["${WVS_PORT:-8080}:8080"]
    depends_on:
      ros-core:
        condition: service_started
    environment:
      - ROS_DOMAIN_ID=0
    healthcheck:
      # Succeeds as soon as something is listening on :8080 (no reliance on /streams)
      test: ["CMD-SHELL", "bash -lc 'exec 3<>/dev/tcp/127.0.0.1/8080'"]
      interval: 10s
      timeout: 3s
      retries: 10
      start_period: 10s

  usb-camera:
    image: ros:iron-ros-base
    container_name: usb-camera
    restart: unless-stopped
    networks: [robot-net]
    depends_on:
      ros-core:
        condition: service_started
    devices:
      - "${CAM_DEV}:${CAM_DEV}"
    group_add:
      - "video"
    environment:
      - ROS_DOMAIN_ID=0
      - CAM_DEV=${CAM_DEV}
    command: >
      bash -lc "
        set -euo pipefail;
        apt-get update &&
        apt-get install -y --no-install-recommends ros-iron-usb-cam ros-iron-image-transport-plugins &&
        rm -rf /var/lib/apt/lists/*;
        source /opt/ros/iron/setup.bash && exec
        ros2 run usb_cam usb_cam_node_exe --ros-args
          -p video_device:=${CAM_DEV}
          -p framerate:=15
          -p image_width:=640
          -p image_height:=480
          -p pixel_format:=mjpeg
          -p io_method:=mmap
      "

networks:
  robot-net: {}

```

---

### File: docker/compose/test.yml {#file-docker--compose--test.yml}

```yaml
name: robot
services:
  image-test:
    build:
      context: ${PROJECT_ROOT}
      dockerfile: docker/camtest.Dockerfile
    restart: unless-stopped
    networks: [robot-net]
    depends_on:
      ros-core:
        condition: service_started
networks:
  robot-net: {}

```

---

### File: docker/compose/web.yml {#file-docker--compose--web.yml}

```yaml
name: robot

services:
  netstatus:
    build:
      context: ${PROJECT_ROOT}/services/netstatus
    restart: unless-stopped
    expose: ["5000"]
    networks: [robot-net]
  video-dashboard:
    image: nginx:stable
    restart: unless-stopped
    ports: ["${DASHBOARD_PORT:-8081}:80"]
    networks: [robot-net]
    volumes:
      - ${PROJECT_ROOT}/site:/usr/share/nginx/html:ro
      - ${PROJECT_ROOT}/site/nginx/conf.d:/etc/nginx/conf.d:ro
    depends_on:
      web-video-server:
        condition: service_healthy    # wait until /streams works
    healthcheck:
      test: ["CMD-SHELL", "nginx -t || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3

networks:
  robot-net: {}

```

---

### File: docker/v412-camera/Dockerfile {#file-docker--v412-camera--dockerfile}

```
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

```

---

### File: docker/v412-camera/docker-compose.yml {#file-docker--v412-camera--docker-compose.yml}

```yaml
version: "3.8"
services:
  v4l2-camera:
    build: .
    image: local/v4l2-camera:iron
    container_name: v4l2-camera
    network_mode: host              # DDS discovery works out of the box
    restart: unless-stopped
    devices:
      - /dev/video0:/dev/video0
    group_add:
      - video                       # /dev/video* is usually root:video
    environment:
      VIDEO_DEVICE: /dev/video0
      IMAGE_WIDTH: "640"
      IMAGE_HEIGHT: "480"
      FRAME_RATE: "15"
      IO_METHOD: mmap               # if you ever see mmap errors, try "read"
      ROS_DOMAIN_ID: "0"
    healthcheck:
      test: ["CMD-SHELL", "v4l2-ctl --device=$$VIDEO_DEVICE --all >/dev/null 2>&1"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s

```

---

### File: nginx/conf.d/robot-mjpeg.conf {#file-nginx--conf.d--robot-mjpeg.conf}

```nginx
server {
    listen 80 default_server;
    server_name _;

    # Serve the static dashboard
    root /usr/share/nginx/html;
    index index.html;

    # Docker DNS
    resolver 127.0.0.11 ipv6=off valid=30s;

    # ---------- Status endpoints (proxy to netstatus:5000) ----------
    location /status {
        proxy_pass http://netstatus:5000/status;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Connection "";
        proxy_read_timeout 5s;
    }

    location /status_temp {
        proxy_pass http://netstatus:5000/status_temp;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Connection "";
        proxy_read_timeout 5s;
    }

    location /status_uptime {
        proxy_pass http://netstatus:5000/status_uptime;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Connection "";
        proxy_read_timeout 5s;
    }

    # ---------- MJPEG stream (ROS web_video_server) ----------
    location /mjpeg {
        proxy_pass http://web-video-server:8080/stream?topic=/camera/image_raw;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_request_buffering off;
        proxy_read_timeout 1h;
    }
}

```

---

### File: nginx/conf.d/robot.conf {#file-nginx--conf.d--robot.conf}

```nginx
server {
  listen 80;
  server_name _;

  # Serve static dashboard files
  root /usr/share/nginx/html;
  index index.html;

  # --- Simple health ---
  location = /health {
    return 200 "ok\n";
    add_header Content-Type text/plain;
  }

  # --- Netstatus proxies ---
  location /status {
    proxy_pass http://netstatus:5000/status;
    proxy_set_header Host $host;
    proxy_http_version 1.1;
  }

  location /status_temp {
    proxy_pass http://netstatus:5000/status_temp;
    proxy_set_header Host $host;
    proxy_http_version 1.1;
  }

  # --- Web Video Server (ROS web_video_server) ---
  # We proxy it under /wvs/ to avoid hard-coded IPs/ports in the page.
  location /wvs/ {
    proxy_pass http://web-video-server:8080/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_buffering off;
    # Allow long-lived MJPEG streams
    proxy_read_timeout 3600s;
    proxy_send_timeout 3600s;
    add_header X-Proxy wvs;
  }
}

```

---

### File: scripts/backup_robot.sh {#file-scripts--backup_robot.sh}

```bash
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

```

---

### File: scripts/backup_to_github.sh {#file-scripts--backup_to_github.sh}

```bash
#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/robot-project}"
BRANCH="${BRANCH:-main}"

cd "$REPO_DIR"

# Ensure upstream exists
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git repo: $REPO_DIR" >&2
  exit 1
fi
if ! git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  echo "Warning: origin/$BRANCH not found; will push and create it on first run."
fi

# Pull latest (fast-forward only to avoid surprises in unattended runs)
git fetch origin || true
git merge --ff-only "origin/$BRANCH" 2>/dev/null || true

# Stage and commit if there are changes
git add -A

if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

HOST="$(hostname -s || echo host)"
TS="$(date +'%Y-%m-%d %H:%M:%S %z')"
MSG="backup($HOST): automated commit at $TS"

git commit -m "$MSG"

# Push with a simple retry if the network blips
for i in 1 2 3; do
  if git push origin "$BRANCH"; then
    echo "Backup pushed to GitHub: $MSG"
    exit 0
  fi
  echo "Push failed (attempt $i). Retrying in 5s..."
  sleep 5
done

echo "Push failed after retries." >&2
exit 1

```

---

### File: scripts/consolidate_and_update.sh {#file-scripts--consolidate_and_update.sh}

```bash
#!/usr/bin/env sh
set -eu

# ==== Config ===============================================================
ROOT="${HOME}/robot-project"
BACKUP_DIR="/tmp/robot-backups"
NOW="$(date +%F)"
TIME="$(date +%H%M)"
STATE="${ROOT}/STATE.md"

# Set to "1" to run quick endpoint checks (dashboard/web-video)
RUN_CHECKS="${RUN_CHECKS:-1}"

# ==== Internals ============================================================
COMPLETED_TMP="$(mktemp)"
CLEANUPS=""

log() { printf "\n[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

cleanup() {
  [ -n "$COMPLETED_TMP" ] && [ -f "$COMPLETED_TMP" ] && rm -f "$COMPLETED_TMP" || true
}
CLEANUPS="cleanup $CLEANUPS"
trap 'for f in $CLEANUPS; do $f || true; done' EXIT INT TERM

add_completed_line() {
  # keep backticks literal
  printf "%s\n" "$1" >> "$COMPLETED_TMP"
}

ensure_layout() {
  mkdir -p \
    "$ROOT/docker/compose" \
    "$ROOT/site/nginx/conf.d" \
    "$ROOT/services" \
    "$ROOT/robot_ws/src" \
    "$ROOT/scripts" \
    "$ROOT/docs/wiring"
}

backup_trees() {
  log "Backing up existing project trees to ${BACKUP_DIR}..."
  mkdir -p "$BACKUP_DIR"
  tar -C / -czf "${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz" \
    robot-docker robot-project robot-dashboard 2>/dev/null || true
  log "Backup archive: ${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz"
}

copy_dir() {
  # copy_dir <src> <dst>
  src="$1"; dst="$2"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a "$src"/ "$dst"/
  else
    mkdir -p "$dst"
    cp -a "$src"/. "$dst"/
  fi
}

rsync_logged() {
  # rsync_logged <src_dir> <dst_dir> <desc>
  src="$1"; dst="$2"; desc="$3"
  if [ -d "$src" ]; then
    log "Syncing: $src -> $dst"
    copy_dir "$src" "$dst"
    add_completed_line "- ${NOW} – Migrated ${desc}: \`$src\` → \`$dst\`."
  else
    log "Skip (missing): $src"
  fi
}

move_content() {
  rsync_logged "${HOME}/robot-dashboard" "${ROOT}/site" "dashboard static files"
  rsync_logged "${HOME}/robot-docker/robot_ws" "${ROOT}/robot_ws" "ROS 2 workspace"
  rsync_logged "${HOME}/robot-docker/scripts" "${ROOT}/scripts" "utility scripts"

  if [ -d "${HOME}/robot-docker/site/nginx/conf.d" ]; then
    log "Syncing nginx snippets from robot-docker → site/nginx/conf.d"
    mkdir -p "${ROOT}/site/nginx/conf.d"
    copy_dir "${HOME}/robot-docker/site/nginx/conf.d" "${ROOT}/site/nginx/conf.d"
    add_completed_line "- ${NOW} – Migrated nginx snippets: \`${HOME}/robot-docker/site/nginx/conf.d\` → \`${ROOT}/site/nginx/conf.d\`."
  fi
}

create_scaffold_files_if_missing() {
  [ -f "${ROOT}/docker/compose/base.yml" ] || {
    cat > "${ROOT}/docker/compose/base.yml" <<'YAML'
version: "3.9"
name: robot
services: {}
networks:
  robot-net: {}
volumes:
  robot-data: {}
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/base.yml\`."
  }

  [ -f "${ROOT}/docker/compose/web.yml" ] || {
    cat > "${ROOT}/docker/compose/web.yml" <<'YAML'
version: "3.9"
services:
  video-dashboard:
    image: nginx:stable
    container_name: video-dashboard
    restart: unless-stopped
    ports: ["${DASHBOARD_PORT:-8081}:80"]
    networks: [robot-net]
    volumes:
      - ../site:/usr/share/nginx/html:ro
      - ../site/nginx/conf.d:/etc/nginx/conf.d:ro

  netstatus:
    build:
      context: ../services/netstatus
    container_name: netstatus
    restart: unless-stopped
    expose: ["5000"]
    networks: [robot-net]
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/web.yml\`."
  }

  [ -f "${ROOT}/docker/compose/ros.yml" ] || {
    cat > "${ROOT}/docker/compose/ros.yml" <<'YAML'
version: "3.9"
services:
  ros-core:
    image: ros:iron-ros-core
    container_name: ros-core
    restart: unless-stopped
    networks: [robot-net]
    command: ["bash","-lc","source /opt/ros/iron/setup.bash && sleep infinity"]

  web-video-server:
    image: ros:iron-ros-base
    container_name: web-video-server
    restart: unless-stopped
    networks: [robot-net]
    ports: ["${WVS_PORT:-8080}:8080"]
    command: >
      bash -lc "
      apt-get update &&
      apt-get install -y ros-iron-web-video-server &&
      source /opt/ros/iron/setup.bash &&
      ros2 run web_video_server web_video_server --port 8080 --address 0.0.0.0
      "
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/ros.yml\`."
  }

  [ -f "${ROOT}/docker/.env" ] || {
    cat > "${ROOT}/docker/.env" <<'ENV'
DASHBOARD_PORT=8081
WVS_PORT=8080
ROBOT_HOSTNAME=RPi-Robot
ENV
    add_completed_line "- ${NOW} – Added \`docker/.env\` with default ports."
  }

  [ -f "${ROOT}/Makefile" ] || {
    cat > "${ROOT}/Makefile" <<'MAKE'
COMPOSE = docker compose -p robot -f docker/compose/base.yml -f docker/compose/web.yml -f docker/compose/ros.yml

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f --tail=200

rebuild:
	$(COMPOSE) build --no-cache

ps:
	$(COMPOSE) ps

restart:
	$(COMPOSE) down && $(COMPOSE) up -d
MAKE
    add_completed_line "- ${NOW} – Created \`Makefile\` (make up / logs / rebuild / ps / restart)."
  }
}

ensure_state_md() {
  [ -f "$STATE" ] || {
    cat > "$STATE" <<'EOF'
# 🛠 Robot Project – State Tracker

**Last Updated:** YYYY-MM-DD  
**Maintainer:** Drew  

---

## 📌 Current Phase
Dashboard & Metrics Integration + RoboClaw Motor Control Recovery

---

## ✅ Completed Since Last Update
- YYYY-MM-DD – Initial consolidation scaffold created (compose skeletons, Makefile, layout).

---

## 🚧 In Progress
- Directory consolidation and path updates across compose & mounts.
- Dashboard metrics for CPU %, memory %, disk.
- RoboClaw firmware recovery.

---

## 🗒 Next Actions
1. Review consolidated layout and mounts.
2. Bring stack up: `make up`.
3. Finish metrics and verify endpoints via dashboard.

---

## ⚠ Issues / Blockers
- RoboClaw device in bootloader; awaiting recovery path.
- Some services still referencing legacy paths.

---

## 📂 Project Structure Reference
robot-project/
docker/compose/ → Compose YAMLs
site/ → Dashboard + nginx
services/ → Small backends (e.g., netstatus)
robot_ws/src/ → ROS 2 packages
scripts/ → Helper scripts
docs/ → Design docs & diagrams
STATE.md → This file


---

## 🔌 System Reference
**Host:** RPi-Robot  
**Ports:** Dashboard :8081, Web Video :8080, Netstatus :5000 (in-network)

---

## 🧩 Active Containers
| Name              | Purpose                  | Restart |
|-------------------|--------------------------|---------|
| video-dashboard   | Nginx + UI               | unless-stopped |
| netstatus         | Metrics API              | unless-stopped |
| ros-core          | ROS 2 base               | unless-stopped |
| web-video-server  | Video server             | unless-stopped |
EOF
    log "Created new STATE.md"
  }
}

update_last_updated() {
  awk -v today="$NOW" '
    BEGIN{done=0}
    {
      if (!done && $0 ~ /^\*\*Last Updated:\*\*/) {
        print "**Last Updated:** " today "  "
        done=1
      } else {
        print
      }
    }
  ' "$STATE" > "${STATE}.tmp" && mv "${STATE}.tmp" "$STATE"
}

insert_completed_lines() {
  grep -q "^## ✅ Completed Since Last Update" "$STATE" || {
    printf "\n\n## ✅ Completed Since Last Update\n" >> "$STATE"
  }
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    if ! grep -Fq "$line" "$STATE"; then
      awk -v ins="$line" '
        BEGIN{added=0}
        {print}
        /^## ✅ Completed Since Last Update$/ && !added {print ins; added=1}
      ' "$STATE" > "${STATE}.tmp" && mv "${STATE}.tmp" "$STATE"
    fi
  done < "$COMPLETED_TMP"
}

create_symlinks() {
  ln -snf "$ROOT/docker" "${HOME}/robot-docker.new"
  ln -snf "$ROOT/site"   "${HOME}/robot-dashboard.new"
  add_completed_line "- ${NOW} – Added convenience links: \`${HOME}/robot-docker.new\` and \`${HOME}/robot-dashboard.new\`."
}

have_cmd() { command -v "$1" >/dev/null 2>&1; }

check_url() {
  # check_url <url> <desc>
  url="$1"; desc="$2"
  if have_cmd curl; then
    if curl -fsS --max-time 2 "$url" >/dev/null 2>&1; then
      add_completed_line "- ${NOW} – CHECK PASS: ${desc} reachable at ${url}."
    else
      add_completed_line "- ${NOW} – CHECK FAIL: ${desc} not reachable at ${url}."
    fi
  elif have_cmd wget; then
    if wget -q -T 2 -O - "$url" >/dev/null 2>&1; then
      add_completed_line "- ${NOW} – CHECK PASS: ${desc} reachable at ${url}."
    else
      add_completed_line "- ${NOW} – CHECK FAIL: ${desc} not reachable at ${url}."
    fi
  else
    add_completed_line "- ${NOW} – CHECK SKIP: No curl/wget to test ${desc} at ${url}."
  fi
}

run_checks() {
  [ "$RUN_CHECKS" = "1" ] || { log "Checks disabled (RUN_CHECKS=0)"; return 0; }
  log "Running quick endpoint checks (best-effort)…"
  check_url "http://localhost:8081/" "Dashboard root"
  check_url "http://localhost:8081/status" "Netstatus via Nginx"
  check_url "http://localhost:8080/streams" "Web Video Server streams"
}

summary() {
  log "Done. Next:"
  cat <<TXT

1) Inspect the new layout:
   tree -L 3 ${ROOT} 2>/dev/null || ls -la ${ROOT}

2) Bring the stack up:
   cd ${ROOT}
   make up && make ps

3) Quick checks (already attempted if RUN_CHECKS=1):
   curl -I http://localhost:8081/ || true
   curl -s http://localhost:8081/status | head -n 5 || true
   curl -s http://localhost:8080/streams | head -n 5 || true

Legacy convenience links:
  ${HOME}/robot-docker.new  -> ${ROOT}/docker
  ${HOME}/robot-dashboard.new -> ${ROOT}/site

Backup archive:
  ${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz
TXT
}

main() {
  log "Starting consolidation into ${ROOT}"
  ensure_layout
  backup_trees
  move_content
  create_scaffold_files_if_missing
  ensure_state_md
  add_completed_line "- ${NOW} – Consolidated repos into \`${ROOT}\` monorepo layout."
  create_symlinks
  run_checks
  update_last_updated
  insert_completed_lines
  summary
}

main "$@"


```

---

### File: scripts/consolidate_and_update_state.sh {#file-scripts--consolidate_and_update_state.sh}

```bash
#!/bin/bash
set -eu

# ==== Config ===============================================================
ROOT="${HOME}/robot-project"
BACKUP_DIR="/tmp/robot-backups"
NOW="$(date +%F)"
TIME="$(date +%H%M)"
STATE="${ROOT}/STATE.md"

# Set to "1" to run quick endpoint checks (dashboard/web-video)
RUN_CHECKS="${RUN_CHECKS:-1}"

# ==== Internals ============================================================
COMPLETED_TMP="$(mktemp)"
CLEANUPS=""

log() { printf "\n[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

cleanup() {
  [ -n "$COMPLETED_TMP" ] && [ -f "$COMPLETED_TMP" ] && rm -f "$COMPLETED_TMP" || true
}
CLEANUPS="cleanup $CLEANUPS"
trap 'for f in $CLEANUPS; do $f || true; done' EXIT INT TERM

add_completed_line() {
  # keep backticks literal
  printf "%s\n" "$1" >> "$COMPLETED_TMP"
}

ensure_layout() {
  mkdir -p \
    "$ROOT/docker/compose" \
    "$ROOT/site/nginx/conf.d" \
    "$ROOT/services" \
    "$ROOT/robot_ws/src" \
    "$ROOT/scripts" \
    "$ROOT/docs/wiring"
}

backup_trees() {
  log "Backing up existing project trees to ${BACKUP_DIR}..."
  mkdir -p "$BACKUP_DIR"
  tar -C / -czf "${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz" \
    robot-docker robot-project robot-dashboard 2>/dev/null || true
  log "Backup archive: ${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz"
}

copy_dir() {
  # copy_dir <src> <dst>
  src="$1"; dst="$2"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a "$src"/ "$dst"/
  else
    mkdir -p "$dst"
    cp -a "$src"/. "$dst"/
  fi
}

rsync_logged() {
  # rsync_logged <src_dir> <dst_dir> <desc>
  src="$1"; dst="$2"; desc="$3"
  if [ -d "$src" ]; then
    log "Syncing: $src -> $dst"
    copy_dir "$src" "$dst"
    add_completed_line "- ${NOW} – Migrated ${desc}: \`$src\` → \`$dst\`."
  else
    log "Skip (missing): $src"
  fi
}

move_content() {
  rsync_logged "${HOME}/robot-dashboard" "${ROOT}/site" "dashboard static files"
  rsync_logged "${HOME}/robot-docker/robot_ws" "${ROOT}/robot_ws" "ROS 2 workspace"
  rsync_logged "${HOME}/robot-docker/scripts" "${ROOT}/scripts" "utility scripts"

  if [ -d "${HOME}/robot-docker/site/nginx/conf.d" ]; then
    log "Syncing nginx snippets from robot-docker → site/nginx/conf.d"
    mkdir -p "${ROOT}/site/nginx/conf.d"
    copy_dir "${HOME}/robot-docker/site/nginx/conf.d" "${ROOT}/site/nginx/conf.d"
    add_completed_line "- ${NOW} – Migrated nginx snippets: \`${HOME}/robot-docker/site/nginx/conf.d\` → \`${ROOT}/site/nginx/conf.d\`."
  fi
}

create_scaffold_files_if_missing() {
  [ -f "${ROOT}/docker/compose/base.yml" ] || {
    cat > "${ROOT}/docker/compose/base.yml" <<'YAML'
version: "3.9"
name: robot
services: {}
networks:
  robot-net: {}
volumes:
  robot-data: {}
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/base.yml\`."
  }

  [ -f "${ROOT}/docker/compose/web.yml" ] || {
    cat > "${ROOT}/docker/compose/web.yml" <<'YAML'
version: "3.9"
services:
  video-dashboard:
    image: nginx:stable
    container_name: video-dashboard
    restart: unless-stopped
    ports: ["${DASHBOARD_PORT:-8081}:80"]
    networks: [robot-net]
    volumes:
      - ../site:/usr/share/nginx/html:ro
      - ../site/nginx/conf.d:/etc/nginx/conf.d:ro

  netstatus:
    build:
      context: ../services/netstatus
    container_name: netstatus
    restart: unless-stopped
    expose: ["5000"]
    networks: [robot-net]
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/web.yml\`."
  }

  [ -f "${ROOT}/docker/compose/ros.yml" ] || {
    cat > "${ROOT}/docker/compose/ros.yml" <<'YAML'
version: "3.9"
services:
  ros-core:
    image: ros:iron-ros-core
    container_name: ros-core
    restart: unless-stopped
    networks: [robot-net]
    command: ["bash","-lc","source /opt/ros/iron/setup.bash && sleep infinity"]

  web-video-server:
    image: ros:iron-ros-base
    container_name: web-video-server
    restart: unless-stopped
    networks: [robot-net]
    ports: ["${WVS_PORT:-8080}:8080"]
    command: >
      bash -lc "
      apt-get update &&
      apt-get install -y ros-iron-web-video-server &&
      source /opt/ros/iron/setup.bash &&
      ros2 run web_video_server web_video_server --port 8080 --address 0.0.0.0
      "
YAML
    add_completed_line "- ${NOW} – Created compose scaffold: \`docker/compose/ros.yml\`."
  }

  [ -f "${ROOT}/docker/.env" ] || {
    cat > "${ROOT}/docker/.env" <<'ENV'
DASHBOARD_PORT=8081
WVS_PORT=8080
ROBOT_HOSTNAME=RPi-Robot
ENV
    add_completed_line "- ${NOW} – Added \`docker/.env\` with default ports."
  }

  [ -f "${ROOT}/Makefile" ] || {
    cat > "${ROOT}/Makefile" <<'MAKE'
COMPOSE = docker compose -p robot -f docker/compose/base.yml -f docker/compose/web.yml -f docker/compose/ros.yml

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f --tail=200

rebuild:
	$(COMPOSE) build --no-cache

ps:
	$(COMPOSE) ps

restart:
	$(COMPOSE) down && $(COMPOSE) up -d
MAKE
    add_completed_line "- ${NOW} – Created \`Makefile\` (make up / logs / rebuild / ps / restart)."
  }
}

ensure_state_md() {
  [ -f "$STATE" ] || {
    cat > "$STATE" <<'EOF'
# 🛠 Robot Project – State Tracker

**Last Updated:** YYYY-MM-DD  
**Maintainer:** Drew  

---

## 📌 Current Phase
Dashboard & Metrics Integration + RoboClaw Motor Control Recovery

---

## ✅ Completed Since Last Update
- YYYY-MM-DD – Initial consolidation scaffold created (compose skeletons, Makefile, layout).

---

## 🚧 In Progress
- Directory consolidation and path updates across compose & mounts.
- Dashboard metrics for CPU %, memory %, disk.
- RoboClaw firmware recovery.

---

## 🗒 Next Actions
1. Review consolidated layout and mounts.
2. Bring stack up: `make up`.
3. Finish metrics and verify endpoints via dashboard.

---

## ⚠ Issues / Blockers
- RoboClaw device in bootloader; awaiting recovery path.
- Some services still referencing legacy paths.

---

## 📂 Project Structure Reference
# robot-project/
# docker/compose/ → Compose YAMLs
# site/ → Dashboard + nginx
# services/ → Small backends (e.g., netstatus)
# robot_ws/src/ → ROS 2 packages
# scripts/ → Helper scripts
# docs/ → Design docs & diagrams
# STATE.md → This file


---

## 🔌 System Reference
**Host:** RPi-Robot  
**Ports:** Dashboard :8081, Web Video :8080, Netstatus :5000 (in-network)

---

## 🧩 Active Containers
| Name              | Purpose                  | Restart |
|-------------------|--------------------------|---------|
| video-dashboard   | Nginx + UI               | unless-stopped |
| netstatus         | Metrics API              | unless-stopped |
| ros-core          | ROS 2 base               | unless-stopped |
| web-video-server  | Video server             | unless-stopped |
EOF
    log "Created new STATE.md"
  }
}

update_last_updated() {
  # Replace the "Last Updated" line portably
  awk -v today="$NOW" '
    BEGIN{done=0}
    {
      if (!done && $0 ~ /^\*\*Last Updated:\*\*/) {
        print "**Last Updated:** " today "  "
        done=1
      } else {
        print
      }
    }
  ' "$STATE" > "${STATE}.tmp" && mv "${STATE}.tmp" "$STATE"
}

insert_completed_lines() {
  # Ensure header exists
  grep -q "^## ✅ Completed Since Last Update" "$STATE" || {
    printf "\n\n## ✅ Completed Since Last Update\n" >> "$STATE"
  }

  # Insert each line after the header if not already present
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    if ! grep -Fq "$line" "$STATE"; then
      awk -v ins="$line" '
        BEGIN{added=0}
        {print}
        /^## ✅ Completed Since Last Update$/ && !added {print ins; added=1}
      ' "$STATE" > "${STATE}.tmp" && mv "${STATE}.tmp" "$STATE"
    fi
  done < "$COMPLETED_TMP"
}

create_symlinks() {
  ln -snf "$ROOT/docker" "${HOME}/robot-docker.new"
  ln -snf "$ROOT/site"   "${HOME}/robot-dashboard.new"
  add_completed_line "- ${NOW} – Added convenience links: \`${HOME}/robot-docker.new\` and \`${HOME}/robot-dashboard.new\`."
}

have_cmd() { command -v "$1" >/dev/null 2>&1; }

check_url() {
  # check_url <url> <desc>
  url="$1"; desc="$2"
  if have_cmd curl; then
    if curl -fsS --max-time 2 "$url" >/dev/null 2>&1; then
      add_completed_line "- ${NOW} – CHECK PASS: ${desc} reachable at ${url}."
    else
      add_completed_line "- ${NOW} – CHECK FAIL: ${desc} not reachable at ${url}."
    fi
  elif have_cmd wget; then
    if wget -q -T 2 -O - "$url" >/dev/null 2>&1; then
      add_completed_line("- ${NOW} – CHECK PASS: ${desc} reachable at ${url}.")
    else
      add_completed_line("- ${NOW} – CHECK FAIL: ${desc} not reachable at ${url}.")
    fi
  else
    add_completed_line "- ${NOW} – CHECK SKIP: No curl/wget to test ${desc} at ${url}."
  fi
}

run_checks() {
  [ "$RUN_CHECKS" = "1" ] || { log "Checks disabled (RUN_CHECKS=0)"; return 0; }
  log "Running quick endpoint checks (best-effort)…"
  check_url "http://localhost:8081/" "Dashboard root"
  check_url "http://localhost:8081/status" "Netstatus via Nginx"
  check_url "http://localhost:8080/streams" "Web Video Server streams"
}

summary() {
  log "Done. Next:"
  cat <<TXT

1) Inspect the new layout:
   tree -L 3 ${ROOT} 2>/dev/null || ls -la ${ROOT}

2) Bring the stack up:
   cd ${ROOT}
   make up && make ps

3) Quick checks (already attempted if RUN_CHECKS=1):
   curl -I http://localhost:8081/ || true
   curl -s http://localhost:8081/status | head -n 5 || true
   curl -s http://localhost:8080/streams | head -n 5 || true

Legacy convenience links:
  ${HOME}/robot-docker.new  -> ${ROOT}/docker
  ${HOME}/robot-dashboard.new -> ${ROOT}/site

Backup archive:
  ${BACKUP_DIR}/robot-pre-merge-${NOW}-${TIME}.tgz
TXT
}

main() {
  log "Starting consolidation into ${ROOT}"
  ensure_layout
  backup_trees
  move_content
  create_scaffold_files_if_missing
  ensure_state_md
  add_completed_line "- ${NOW} – Consolidated repos into \`${ROOT}\` monorepo layout."
  create_symlinks
  run_checks
  update_last_updated
  insert_completed_lines
  summary
}

main "$@"


```

---

### File: scripts/make_project_snapshot.sh {#file-scripts--make_project_snapshot.sh}

```bash
#!/usr/bin/env bash
# make_project_snapshot.sh
# Create a single-file Markdown snapshot of the robot project with:
#  - Directory tree (with sensible excludes)
#  - Index of included files (clickable within Markdown viewers)
#  - Concatenated file contents for easy review
# Usage:
#   ./make_project_snapshot.sh [PROJECT_DIR] [OUTPUT_DIR]
# Defaults:
#   PROJECT_DIR = ~/robot-project
#   OUTPUT_DIR  = $PROJECT_DIR/_snapshots

set -euo pipefail

# ---------- Config ----------
PROJECT_DIR="${1:-$HOME/robot-project}"
OUTPUT_DIR="${2:-$PROJECT_DIR/_snapshots}"
DATE_UTC="$(date -u '+%Y-%m-%d %H:%M:%S UTC')"
STAMP="$(date -u '+%Y%m%d-%H%M%S')"
OUTFILE="$OUTPUT_DIR/project-snapshot-$STAMP.md"

# Glob settings
shopt -s globstar nullglob extglob

# Exclusions for tree/find
TREE_IGNORE='node_modules|.git|build|install|log|__pycache__|.venv|dist|*.mp4|*.mov|*.mpg|*.avi|*.mkv|.DS_Store'

# File patterns to include in the snapshot
# (Add/remove here if you want more/less content)
INCLUDE_GLOBS=(
  "docker/**/*.yml"
  "docker/**/*.yaml"
  "docker/**/compose*.yml"
  "docker/**/Dockerfile"
  "docker/**/dockerfile"
  "site/**/*.html"
  "site/**/*.js"
  "site/**/*.css"
  "site/nginx/**/*.conf"
  "nginx/**/*.conf"
  "services/**/*.@(py|sh|yml|yaml)"
  "scripts/**/*.sh"
  "scripts/**/*.py"
  "ros*/**/*.py"
  "ros*/**/package.xml"
  "ros*/**/setup.cfg"
  "ros*/**/CMakeLists.txt"
  "**/requirements.txt"
  "**/.env"
  "STATE.md"
  "README.md"
  "index.html"
)

# ---------- Pre-flight checks ----------
if [[ ! -d "$PROJECT_DIR" ]]; then
  echo "ERROR: Project dir not found: $PROJECT_DIR" >&2
  exit 1
fi
mkdir -p "$OUTPUT_DIR"

# ---------- Collect matching files ----------
declare -A SEEN
FILES=()

pushd "$PROJECT_DIR" >/dev/null

for pattern in "${INCLUDE_GLOBS[@]}"; do
  for f in $pattern; do
    if [[ -f "$f" ]]; then
      # normalize to relative, de-dup
      rel="${f#./}"
      if [[ -z "${SEEN[$rel]+x}" ]]; then
        SEEN[$rel]=1
        FILES+=("$rel")
      fi
    fi
  done
done

# Sort file list
IFS=$'\n' FILES=($(printf '%s\n' "${FILES[@]}" | sort -u))
unset IFS

# ---------- Build directory tree ----------
TREE_BLOCK=""
if command -v tree >/dev/null 2>&1; then
  TREE_BLOCK="$(tree -a -I "$TREE_IGNORE" -F)"
else
  # Fallback to find + sed for a crude tree if 'tree' is unavailable
  # Prune common heavy dirs
  TREE_BLOCK="$(
    find . \
      -path './.git' -prune -o \
      -path './node_modules' -prune -o \
      -path './build' -prune -o \
      -path './install' -prune -o \
      -path './log' -prune -o \
      -path './__pycache__' -prune -o \
      -path './.venv' -prune -o \
      -type d -print -o -type f -print \
    | sed 's|^\./||' \
    | awk '{
        n=gsub(/[^\/]/,"");
        gsub(/[^\/]/,"");
        indent=length($0)-length(gensub(/[^\/]/,"","g"));
        gsub(/[^\/]/,"");
      }1' \
    | awk -F/ '{
        depth = NF-1;
        pad = "";
        for(i=0;i<depth;i++) pad=pad"  ";
        print pad $NF
      }'
  )"
fi

# ---------- Git context (optional) ----------
GIT_REMOTE=""
GIT_BRANCH=""
GIT_COMMIT=""
if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  GIT_REMOTE="$(git remote -v | awk 'NR==1{print $2}')"
  GIT_BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
  GIT_COMMIT="$(git rev-parse --short HEAD 2>/dev/null || true)"
fi

# ---------- Helper: make an anchor id from a path ----------
slugify() {
  # lowercase, replace spaces with '-', replace slashes with '--', strip invalids
  local s="${1,,}"
  s="${s// /-}"
  s="${s//\//--}"
  s="$(echo -n "$s" | sed 's/[^a-z0-9._-]/-/g')"
  printf "%s" "$s"
}

# ---------- Write header & index ----------
{
  echo "# Robot Project Snapshot"
  echo ""
  echo "- **Generated:** $DATE_UTC"
  echo "- **Host:** $(hostname 2>/dev/null || echo 'unknown')"
  if [[ -n "$GIT_COMMIT" ]]; then
    echo "- **Git:** \`$GIT_BRANCH@$GIT_COMMIT\`  ${GIT_REMOTE:+(remote: $GIT_REMOTE)}"
  fi
  echo ""
  echo "## Directory Tree"
  echo ""
  echo '```text'
  [[ -n "$TREE_BLOCK" ]] && echo "$TREE_BLOCK" || echo "(tree unavailable)"
  echo '```'
  echo ""
  echo "## Index"
  echo ""
  if ((${#FILES[@]}==0)); then
    echo "_No matching files found with current patterns._"
  else
    i=1
    for f in "${FILES[@]}"; do
      anchor="file-$(slugify "$f")"
      printf "%2d. [%s](#%s)\n" "$i" "$f" "$anchor"
      ((i++))
    done
  fi
  echo ""
  echo "---"
  echo ""
} > "$OUTFILE"

# ---------- Append file contents ----------
if ((${#FILES[@]})); then
  for f in "${FILES[@]}"; do
    anchor="file-$(slugify "$f")"
    echo "### File: $f {#$anchor}" >> "$OUTFILE"
    echo "" >> "$OUTFILE"

    # choose a fence language for nicer syntax highlighting
    ext="${f##*.}"
    case "${ext,,}" in
      yml|yaml) lang="yaml" ;;
      sh)       lang="bash" ;;
      py)       lang="python" ;;
      js)       lang="javascript" ;;
      html|htm) lang="html" ;;
      css)      lang="css" ;;
      conf)     lang="nginx" ;;
      xml)      lang="xml" ;;
      md)       lang="markdown" ;;
      txt|env)  lang="text" ;;
      *)        lang="" ;;
    esac

    if [[ -n "$lang" ]]; then
      echo "\`\`\`$lang" >> "$OUTFILE"
    else
      echo "\`\`\`" >> "$OUTFILE"
    fi
    cat -- "$f" >> "$OUTFILE" || true
    echo "" >> "$OUTFILE"
    echo "\`\`\`" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
    echo "---" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
  done
fi

popd >/dev/null

echo "Snapshot written to: $OUTFILE"

```

---

### File: scripts/prune_docker.sh {#file-scripts--prune_docker.sh}

```bash
# 0) See what's using space (images/containers/volumes/cache)
docker system df -v
# 1) Remove stopped containers, unused networks, dangling images, build cache
docker system prune -f
# 2) Remove images not used by any container (keeps images backing running containers)
# Keep very recent ones; adjust "until" if you like.
docker image prune -a -f --filter "until=168h"
# 3) Clear builder/cache artifacts (speeds up disk recovery; future builds may take longer)
docker builder prune -af
# 4) OPTIONAL: Remove unused volumes (never removes volumes in use)
# Skip if you're unsure, but generally safe. This does NOT touch bind mounts.
docker volume prune -f

```

---

### File: services/netstatus/app.py {#file-services--netstatus--app.py}

```python
from flask import Flask, jsonify
import psutil, time, os
app = Flask(__name__)
@app.get("/status")
def status():
    la = os.getloadavg() if hasattr(os, "getloadavg") else (0,0,0)
    vm = psutil.virtual_memory(); du = psutil.disk_usage('/')
    return jsonify({
        "cpu":{"percent": psutil.cpu_percent(interval=0.1), "load_avg": la},
        "memory":{"total": vm.total, "used": vm.used},
        "disk":{"total": du.total, "used": du.used},
        "uptime_seconds": time.time() - psutil.boot_time()
    })
@app.get("/status_temp")
def status_temp():
    temp = None
    try:
        temps = psutil.sensors_temperatures()
        for k in temps:
            for t in temps[k]:
                if hasattr(t,'current') and t.current:
                    temp = t.current; break
            if temp: break
    except Exception:
        pass
    return jsonify({"cpu_temp_c": temp})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

---

### File: services/netstatus/requirements.txt {#file-services--netstatus--requirements.txt}

```text
Flask==3.0.3
psutil==5.9.8

```

---

### File: site/index.html {#file-site--index.html}

```html
<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Robot Dashboard</title>
<style>
  :root{--bg:#111;--fg:#eaeaea;--muted:#9aa3b2;--card:#1b1b1b;--line:#2a2a2a;--pill:#2e3440}
  *{box-sizing:border-box}
  body{font-family:system-ui,Arial,sans-serif;background:var(--bg);color:var(--fg);margin:0;padding:16px}
  h1{margin:0 0 12px}
  .grid{display:grid;grid-template-columns:2fr 1fr;gap:16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px}
  label,select,button{font-size:14px;margin-right:8px}
  select,button{background:#0e1230;border:1px solid #2a3569;border-radius:8px;color:var(--fg);padding:6px 10px}
  button:hover,select:hover{border-color:#3b4a8e;cursor:pointer}
  img{max-width:100%;border-radius:8px;background:#000;display:block}
  code, .mono{font-family:ui-monospace,Menlo,Consolas,monospace}
  .kv{display:grid;grid-template-columns:160px 1fr;gap:6px;margin:6px 0}
  .muted{color:var(--muted)}
  .pill{display:inline-block;background:var(--pill);padding:2px 8px;border-radius:999px;font-size:12px}
  #cur{color:var(--muted);word-break:break-all;margin-top:6px}
  .section{margin-top:10px}
</style>

<h1>Robot Dashboard <span class="pill mono" id="iface">net: —</span></h1>

<div class="grid">
  <!-- VIDEO -->
  <div class="card">
    <h2>Video</h2>
    <div class="section">
      <label>Topic
        <select id="topic">
          <option value="/image_raw">/image_raw</option>
          <option value="/camera/image_raw">/camera/image_raw</option>
        </select>
      </label>
      <label>Quality
        <select id="quality">
          <option>80</option><option>70</option><option>60</option><option>90</option>
        </select>
      </label>
      <button id="apply">Apply</button>
      <div id="cur" class="mono"></div>
    </div>
    <img id="video" alt="video stream">
  </div>

  <!-- TELEMETRY -->
  <div class="card">
    <h2>Telemetry</h2>
    <div class="kv"><div class="muted">CPU Temp:</div>           <div id="cpuTemp">—</div></div>
    <div class="kv"><div class="muted">CPU Usage:</div>          <div id="cpuPct">—</div></div>
    <div class="kv"><div class="muted">Load Avg (1/5/15m):</div> <div id="loadAvg">—</div></div>
    <div class="kv"><div class="muted">Uptime:</div>             <div id="uptime">—</div></div>
    <div class="kv"><div class="muted">Memory used:</div>        <div id="memUsed">—</div></div>
    <div class="kv"><div class="muted">Memory total:</div>       <div id="memTotal">—</div></div>
    <div class="kv"><div class="muted">Memory %:</div>           <div id="memPct">—</div></div>
    <div class="kv"><div class="muted">Disk used:</div>          <div id="diskUsed">—</div></div>
    <div class="kv"><div class="muted">Disk total:</div>         <div id="diskTotal">—</div></div>
    <div class="kv"><div class="muted">Disk %:</div>             <div id="diskPct">—</div></div>
    <div class="section">
      <div class="muted">Status JSON (raw):</div>
      <div class="mono" id="statusMini" style="white-space:pre-wrap;word-break:break-all">—</div>
    </div>
  </div>
</div>

<script>
  // ---------- helpers ----------
  const $=id=>document.getElementById(id);
  function bytes(n){ if(n==null) return '—';
    const u=['B','KB','MB','GB','TB','PB']; let i=0, x=Number(n)||0;
    while(x>=1024 && i<u.length-1){ x/=1024; i++; }
    return (x>=10?x.toFixed(0):x.toFixed(1))+' '+u[i];
  }
  function pct(used,total){ if(!(Number.isFinite(+used)&&Number.isFinite(+total)&&total>0)) return '—';
    return (100*used/total).toFixed(1)+'%';
  }
  function fmtUptime(sec){
    sec=+sec; if(!Number.isFinite(sec)) return '—';
    const d=Math.floor(sec/86400); sec-=d*86400;
    const h=Math.floor(sec/3600); sec-=h*3600;
    const m=Math.floor(sec/60);   const s=Math.floor(sec-m*60);
    return `${d?d+'d ':''}${h}h ${m}m ${s}s`;
  }

  // ---------- video ----------
  const img=$('video'), topic=$('topic'), q=$('quality'), cur=$('cur');
  function setSrc(){
    const u=`/ros/stream?topic=${encodeURIComponent(topic.value)}&type=mjpeg&quality=${encodeURIComponent(q.value)}`;
    img.src = u + `&_=${Date.now()}`; // bust cache each Apply
    cur.textContent = u;
  }
  $('apply').onclick=setSrc; setSrc();

  // ---------- telemetry ----------
  async function j(u, asJson=true){
    const r = await fetch(u, {cache:'no-store'});
    if(!r.ok) throw new Error(`${u} -> ${r.status}`);
    return asJson ? r.json() : r.text();
  }

  async function tick(){
    try{
      const [st,tmp] = await Promise.allSettled([ j('/status'), j('/status_temp') ]);
      if(st.status==='fulfilled'){
        const js = st.value || {};
        // labeled fields
        const cpuPct = js.cpu?.percent ?? null;
        const la     = js.cpu?.load_avg ?? null;
        const memU   = js.memory?.used ?? null;
        const memT   = js.memory?.total ?? null;
        const diskU  = js.disk?.used ?? null;
        const diskT  = js.disk?.total ?? null;
        const upS    = js.uptime_seconds ?? js.uptime_sec ?? js.uptime ?? js?.system?.uptime;

        $('cpuPct').textContent  = (cpuPct==null?'—':cpuPct.toFixed?cpuPct.toFixed(1)+'%':cpuPct+'%');
        $('loadAvg').textContent = Array.isArray(la) ? la.join(', ') : (la??'—');
        $('uptime').textContent  = fmtUptime(upS);

        $('memUsed').textContent  = bytes(memU);
        $('memTotal').textContent = bytes(memT);
        $('memPct').textContent   = pct(memU, memT);

        $('diskUsed').textContent  = bytes(diskU);
        $('diskTotal').textContent = bytes(diskT);
        $('diskPct').textContent   = pct(diskU, diskT);

        // raw mini JSON for quick debugging
        $('statusMini').textContent = JSON.stringify({
          cpu_pct: cpuPct,
          load_avg: la,
          mem_used: memU,  mem_total: memT,  mem_pct: (memU!=null&&memT)? +(100*memU/memT).toFixed(1):null,
          disk_used: diskU, disk_total: diskT, disk_pct: (diskU!=null&&diskT)? +(100*diskU/diskT).toFixed(1):null,
          up_s: upS
        });
      }
      if(tmp.status==='fulfilled'){
        const t = tmp.value?.cpu_temp_c ?? tmp.value?.temp_c ?? null;
        $('cpuTemp').textContent = (t!=null) ? ((t.toFixed?t.toFixed(1):t)+' °C') : '—';
      }
    }catch(_){ /* keep last values */ }
  }

  // Detect which net iface we’re effectively using (best-effort)
  (async function(){
    try{ const s = await j('/status'); $('iface').textContent = 'net: '+(s.active_interface || s.iface || location.host || 'unknown'); }
    catch{ $('iface').textContent='net: unknown'; }
  })();

  tick(); setInterval(tick, 5000);
</script>

```

---

### File: site/nginx/conf.d/robot.conf {#file-site--nginx--conf.d--robot.conf}

```nginx
server {
  listen 80 default_server;
  server_name _;

  root /usr/share/nginx/html;
  index index.html;

  # Video proxy → web_video_server
  location /ros/ {
    proxy_pass http://web-video-server:8080/;
    proxy_buffering off;
    proxy_request_buffering off;
    proxy_read_timeout 3600s;
    proxy_send_timeout 3600s;
    sendfile off;
    tcp_nodelay on;
  }

  # Telemetry → netstatus
  location = /status      { proxy_pass http://netstatus:5000/status; }
  location = /status_temp { proxy_pass http://netstatus:5000/status_temp; }
}

```

---

### File: site/test_mjpeg.html {#file-site--test_mjpeg.html}

```html
<!doctype html><meta charset="utf-8">
<title>MJPEG Test</title>
<body style="margin:0;background:#000;color:#fff;font:14px/1.4 system-ui">
  <div style="padding:10px">Raw MJPEG via proxy: <code>/wvs/stream?topic=/image_raw</code></div>
  <img src="/wvs/stream?topic=/image_raw" style="display:block;width:100%;height:auto;border:0" alt="stream"/>
</body>

```

---

