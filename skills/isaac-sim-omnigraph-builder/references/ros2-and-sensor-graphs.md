# ROS 2 and Sensor Graphs

## Official docs
- ROS 2 reference architecture: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_reference_architecture.html
- ROS2 joint control scripting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_manipulation.html
- ROS 2 cameras: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_camera.html
- RTX Lidar sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_rtx_lidar.html

## ROS 2 graph checks

Before editing:
1. Confirm ROS 2 bridge extension and environment.
2. Confirm `ROS_DOMAIN_ID` and middleware variables.
3. Identify publisher/subscriber node types, topic names, namespaces, QoS, and frame IDs.
4. Confirm simulation is playing when nodes require active simulation time.

## Sensor graph checks

For camera, Lidar, radar, IMU, contact, or joint-state graphs:
- verify sensor prim path
- verify render product or sensor output path
- verify tick rate and timing source
- verify topic name and message type
- verify downstream subscriber or file output

Hand off API-level sensor problems to `$isaac-sim-60-sensors-sdg`.
