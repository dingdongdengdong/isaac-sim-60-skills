---
name: isaac-sim-omnigraph-builder
description: Use when creating, scripting, inspecting, or debugging Isaac Sim 6.0.0 OmniGraph or Action Graph workflows, including robot controllers, ROS 2 bridge graphs, sensor publishing graphs, simulation tick graphs, custom Python/C++ OmniGraph nodes, graph connections, node attributes, 5.1-to-6.0 ROS/sensor node migration, or graph execution failures.
---

# Isaac Sim OmniGraph Builder

Use this skill to build graph behavior reproducibly with Python or GUI-equivalent steps. Prefer scripted graph creation for repeatability, and always verify node paths, connections, execution triggers, and runtime state.

## Workflow
1. Identify the graph purpose: robot control, ROS 2 publishing/subscribing, sensor readout, simulation control, custom node, or UI-authored graph inspection.
2. Choose graph type: Action Graph for explicit execution flow, Push Graph for automatic frame evaluation.
3. Read `references/graph-scripting.md` before using Python APIs to create nodes or connections.
4. Read `references/ros2-and-sensor-graphs.md` before migrating 5.1 ROS/sensor graphs or wiring source-node inputs in 6.0.
5. Enable required extensions before creating extension-specific nodes.
6. Create or locate the graph under a stable path such as `/World/ActionGraph`.
7. Add nodes, set attributes, connect execution and data pins, then save a graph report with node paths and attributes.
8. Run the simulation or graph trigger and verify the downstream artifact: robot motion, ROS topic, sensor output, or log message.

## Read Order
- Read `references/graph-scripting.md` for Python graph construction, inspection, execution triggers, and report fields.
- Read `references/ros2-and-sensor-graphs.md` for ROS 2 bridge, camera, Lidar/Radar, TF, odometry, QoS, and 6.0 migration warnings.
- Read `references/custom-nodes.md` for Python/C++ OmniGraph nodes and `.ogn` constraints.
- Read `references/troubleshooting.md` when nodes do not execute, attributes do not update, or ROS/sensor outputs are missing.

## Handoffs
- Use `$isaac-sim-python-scripting` for standalone app lifecycle and extension enabling.
- Use `$isaac-sim-60-ros2-sitl` for ROS 2 topic contracts and bridge/container diagnostics.
- Use `$isaac-sim-60-sensors-sdg` for sensor API and render-product behavior.
- Use `$isaac-sim-robot-setup-tuning` for drive, joint, collider, or robot physics problems discovered through graph control.

## Non-Negotiables
- Do not confuse OmniGraph nodes with ROS 2 nodes; they are different systems.
- Do not assume a graph runs until its execution trigger is connected and simulation state is active.
- Do not leave generated graphs undocumented; report graph path, nodes, attributes, connections, required extensions, and verification artifact.
- Do not rewrite a user's graph wholesale when a focused node/connection fix is enough.
