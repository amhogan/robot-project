# Robot Project Snapshot

- **Generated:** 2025-08-14 14:55:07 UTC
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

209 directories, 688 files
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

