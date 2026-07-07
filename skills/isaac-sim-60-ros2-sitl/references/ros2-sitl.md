# Isaac Sim 6.0 ROS 2 SITL Reference

## Official docs checked
- ROS 2 landing page: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_landing_page.html
- ROS 2 installation default: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_ros.html
- ROS 2 installation other platforms: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_ros_other_platforms.html
- ROS 2 reference architecture: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_reference_architecture.html
- ROS 2 Simulation Control: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_simulation_control.html
- ROS 2 QoS: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_qos.html
- ROS 2 OmniGraph migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/ros2_omnigraph_migration.html
- ROS 2 troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/troubleshooting.html

## 6.0 ROS notes
- In Isaac Sim 6.0, some ROS 2 OmniGraph publisher nodes moved away from direct prim path inputs toward pre-computed source-node inputs. Be careful with `ROS2 Publish Transform Tree`, `ROS2 Publish Joint State`, odometry, and sensor graphs migrated from 5.1 or earlier.
- ROS 2 tutorials cover both Linux and Windows workflows; do not assume WSL for a Windows user without checking the selected install path.
- Simulation Control exposes world-management services/actions; verify service names against the installed Isaac Sim/Simulation Interfaces version before scripting external control.
- 5.1 release notes updated internal Humble/Jazzy libraries and set bridge library loading toward `system_default`; preserve explicit environment variables in existing Docker workflows unless intentionally changing platform behavior.

## Workspace services
- Isaac Sim compose service: `isaac-sim-60`.
- LeRobot phone teleop service: `lerobot`, phone UI port `8766`.
- Foxglove service: `foxglove`, web port `8080`.
- Default ROS domain: `42`.

## 13D LeRobot joint order
Preserve this semantic order unless the user explicitly requests a breaking dataset/control migration:

```text
shoulder_pan
shoulder_lift
elbow_flex
wrist_roll
wrist_pitch
wrist_yaw
thumb_0
thumb_1
index_0
index_1
middle_0
middle_1
gripper
```

If the real asset does not expose a matching articulation yet, report missing bindings instead of reshaping the contract silently.

## Verification commands
Run inside the ROS-aware container or shell:

```bash
export ROS_DOMAIN_ID=42
ros2 topic list
ros2 topic hz /follower/joint_states
ros2 topic echo --once /follower/joint_states
ros2 topic pub --once /leader/joint_commands std_msgs/msg/Float64MultiArray '{data: [0,0,0,0,0,0,0,0,0,0,0,0,0]}'
```

For Simulation Control tasks, also list services/actions:

```bash
ros2 service list | grep -i world || true
ros2 action list | grep -i sim || true
```

## Triage rules
- Missing all topics: runtime/bridge extension/domain issue.
- Topics exist but stale: simulation not playing, graph not executing, QoS/RMW mismatch, or publisher blocked.
- Wrong joint count/order: asset binding or LeRobot contract issue; coordinate with `$isaac-sim-60-robot-assets`.
- Sensor topics wrong: coordinate with `$isaac-sim-60-sensors-sdg` and `$isaac-sim-omnigraph-builder`.
- External tools cannot connect: record domain, middleware, container network, ports, and firewall before changing graph logic.

## Do not silently change
- `ROS_DOMAIN_ID`
- RMW implementation
- topic names
- message types
- 13D joint order
- bridge container/service names
