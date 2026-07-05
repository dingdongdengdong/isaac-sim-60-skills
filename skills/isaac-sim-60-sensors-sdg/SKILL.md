---
name: isaac-sim-60-sensors-sdg
description: Use when designing or debugging Isaac Sim 6.0.0 sensor and synthetic data workflows, including cameras, RTX Lidar/Radar, tick rates, multitick rendering, Replicator, data capture, annotators, randomization, or teleoperation-generated datasets.
---

# Isaac Sim 6.0 Sensors and SDG

## Overview
Use this skill to choose the right 6.0 sensor APIs and capture path before writing scene code or Replicator workflows.

## Workflow
1. Identify outputs: RGB/depth/segmentation, Lidar/Radar point clouds, ROS 2 topics, Replicator dataset, or teleoperation episodes.
2. Read `references/sensors-sdg.md` before using 5.x sensor APIs or migrating old Replicator/ROS graphs.
3. For runtime sensor timing, account for Isaac Sim 6.0 multitick rendering and sensor tick-rate behavior.
4. For data capture failures, verify render products, writers, output permissions, materials, and lighting before changing logic.
5. Coordinate ROS-published sensor streams with `$isaac-sim-60-ros2-sitl`.

## References
- Read `references/sensors-sdg.md` for official 6.0 sensor and SDG links, migration notes, and local dataset context.
- Use `$physical-ai-neural-reconstruction` for NuRec/NRE sensor-sim workflows, not ordinary camera/Lidar capture.
