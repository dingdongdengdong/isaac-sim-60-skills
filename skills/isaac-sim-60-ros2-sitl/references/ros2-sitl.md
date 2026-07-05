# Isaac Sim 6.0 ROS 2 SITL Reference

## Official docs checked
- ROS 2 landing page: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_landing_page.html
- ROS 2 installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_ros.html
- ROS 2 OmniGraph migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/ros2_omnigraph_migration.html

## 6.0 ROS notes
- Isaac Sim connects to ROS through the ROS 2 bridge extension.
- NVIDIA recommends/targets ROS 2 Jazzy and Humble for Isaac Sim 6.0; this workspace currently uses Humble containers.
- In Isaac Sim 6.0, some ROS 2 OmniGraph publisher nodes moved toward pre-computed source-node inputs. Be careful with `ROS2 Publish Transform Tree` and `ROS2 Publish Joint State` graphs migrated from 5.1 or earlier.

## Workspace services
- Isaac Sim service: `isaac-sim-60`.
- LeRobot phone teleop service: `lerobot`, phone UI port `8766`.
- Foxglove bridge service: `foxglove`, WebSocket port `8765`.

## 13D LeRobot joint order
```text
right_arm_pitch_joint.pos
right_arm_roll_joint.pos
right_arm_yaw_joint.pos
right_elbow_pitch_joint.pos
right_elbow_yaw_joint.pos
finger1_motor1.pos
finger1_motor2.pos
finger2_motor1.pos
finger2_motor2.pos
finger3_motor1.pos
finger3_motor2.pos
finger4_motor1.pos
finger4_motor2.pos
```

## Verification commands
```bash
cd /home/dong/robot/superarm_ws/isaacsim_test
docker compose up isaac-sim-60
# new terminal
docker compose up lerobot foxglove
```

Host/container ROS checks:
```bash
export ROS_DOMAIN_ID=42
source /opt/ros/humble/setup.bash
ros2 topic list
ros2 topic hz /follower/joint_states
ros2 topic pub /leader/joint_commands std_msgs/msg/Float64MultiArray \
  "data: [0.1, 0.0, 0.0, 0.0, 0.0, 0.05, 0.02, 0.2, 0.25, 0.35, 0.4, 0.5, 0.6]" --once
ros2 topic echo /follower/joint_states --once
```

## Do not silently change
- Topic names.
- Message type for the 13D command path.
- Joint order.
- `ROS_DOMAIN_ID` defaults in compose and docs.
