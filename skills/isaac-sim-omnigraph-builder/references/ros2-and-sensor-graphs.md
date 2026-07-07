# ROS 2 and Sensor Graphs

## Official docs
- ROS 2 reference architecture: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_reference_architecture.html
- ROS2 joint control scripting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_manipulation.html
- ROS 2 cameras: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_camera.html
- RTX Lidar sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_rtx_lidar.html
- ROS 2 QoS: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_qos.html
- ROS 2 OmniGraph migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/ros2_omnigraph_migration.html

## ROS 2 graph checks
Record:
- graph path
- node type names
- topic, namespace, frame ID, QoS, and domain assumptions
- execution trigger path
- source nodes used for prim, articulation, transform, or sensor data
- downstream verification command (`ros2 topic echo`, `hz`, service/action list)

## 6.0 migration warning
Do not migrate old 5.1 graphs by copying prim path strings into deprecated node inputs. In 6.0, publisher nodes may require pre-computed source-node inputs. Rebuild the minimal dataflow and verify one topic before expanding the graph.

## Sensor graph checks
Record:
- sensor prim and render product paths
- annotator or GenericModelOutput nodes
- graph execution trigger
- frame/tick rate policy
- whether output is consumed by ROS, Replicator, file writer, or debug draw

## Handoff rule
If graph wiring is correct but the sensor produces no data, hand off to `$isaac-sim-60-sensors-sdg`. If the ROS topic does not appear despite graph output, hand off to `$isaac-sim-60-ros2-sitl`.
