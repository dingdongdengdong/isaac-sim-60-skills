---
name: isaac-sim-60-ros2-sitl
description: Use when connecting Isaac Sim 6.0.0 to ROS 2, LeRobot, Foxglove, smartphone teleoperation, Simulation Control, ROS_DOMAIN_ID/RMW/QoS, ROS 2 bridge extensions, `/leader/joint_commands`, `/follower/joint_states`, or this workspace's Sim-in-the-loop control contract.
---

# Isaac Sim 6.0 ROS 2 SITL

## Overview
Use this skill to keep the Isaac Sim ↔ ROS 2 ↔ LeRobot contract stable while changing runtime, scene assets, graph wiring, or control bindings.

## Workflow
1. Confirm runtime readiness with `$isaac-sim-60-runtime` if Isaac Sim has not started.
2. Read `references/ros2-sitl.md` before changing topics, message shapes, ROS 2 install platform, Simulation Control, or bridge containers.
3. Preserve this workspace's 13D command/state contract unless the user explicitly requests a breaking interface change.
4. Verify bridge health by checking container logs, `ros2 topic list`, `ros2 topic hz /follower/joint_states`, and a one-shot `/leader/joint_commands` publish.
5. If ROS 2 OmniGraph nodes are involved, read the 6.0 migration notes before editing graphs or scripts.
6. Hand off to `$isaac-sim-omnigraph-builder` for node/pin/graph construction and to `$isaac-sim-60-troubleshooting` for missing/stale topics.

## Local Contract
- `/leader/joint_commands`: command input, `std_msgs/msg/Float64MultiArray`, 13 floats.
- `/follower/joint_commands`: follower-side command bridge, same semantic order.
- `/follower/joint_states`: observation output, expected joint names in the same 13-feature order.
- Default `ROS_DOMAIN_ID=42`, `RMW_IMPLEMENTATION=rmw_fastrtps_cpp`, `FASTDDS_BUILTIN_TRANSPORTS=UDPv4`.

## References
- Read `references/ros2-sitl.md` for official ROS 2 bridge links, Simulation Control notes, platform notes, migration warnings, and exact local commands.
- Use `$isaac-sim-60-troubleshooting` for missing topics, stale domains, QoS/RMW mismatches, or bridge startup failures.
