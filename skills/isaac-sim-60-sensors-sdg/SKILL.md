---
name: isaac-sim-60-sensors-sdg
description: Use when designing or debugging Isaac Sim 6.0.0 sensors, timing, or synthetic data capture, including RtxCamera, CameraSensor, TiledCameraSensor, LidarSensor, RadarSensor, RTX Acoustic, physics/PhysX/proximity sensors, GenericModelOutput, Replicator writers or annotators, Action/Event SDG, MobilityGen, teleoperation SDG, orchestrator.step(), tick_rate, scan accumulation, or migration from deprecated 5.x sensor APIs.
---

# Isaac Sim 6.0 Sensors and SDG

## Overview
Use this skill to choose the sensor API, timing policy, and capture path before writing camera, RTX sensor, ROS stream, Replicator, MobilityGen, teleoperation, or Action/Event dataset code.

## Workflow
1. Choose the output first: camera frames, depth, segmentation, RTX Lidar point cloud, RTX Radar/acoustic data, physics/PhysX sensor signal, ROS stream, Replicator dataset, MobilityGen recording, or teleoperation episode.
2. For new Isaac Sim 6.0 camera/Lidar/Radar work, prefer the documented 6.0 experimental sensor APIs; treat `isaacsim.sensors.camera` and `isaacsim.sensors.rtx` as deprecated or migration-only.
3. State the timing policy explicitly: autotrigger, `tick_rate`, Lidar scan rate, Replicator `orchestrator.step()`, episode recorder cadence, or ROS publish rate.
4. Read the smallest matching reference file from the matrix below before editing code.
5. Preserve this workspace's LeRobot 13D state/action contract when sensor data intersects teleoperation datasets.

## Read Order
- Start with `references/sensors-sdg.md` for official source links and the output-to-reference matrix.
- Read `references/camera-workflows.md` for `RtxCamera`, `CameraSensor`, `TiledCameraSensor`, depth, segmentation, lens distortion, and image capture checks.
- Read `references/rtx-lidar-radar.md` for Lidar/Radar/Acoustic/GenericModelOutput, non-visual materials, point-cloud annotators, debug draw, and Radar Motion BVH.
- Read `references/replicator-sdg.md` for Replicator Functional API, writers, annotators, randomization, manual stepping, and dataset flushing.
- Read `references/action-event-teleop-sdg.md` for Action/Event SDG, behavior-tree generation, MobilityGen, teleoperation SDG, and episode recording.
- Read `references/timing-and-migration.md` for `tick_rate`, multitick rendering, deprecated `frameSkipCount`, scan accumulation, and 5.x-to-6.0 API migration.
- Read `references/troubleshooting.md` when captures are blank, missing, partial, stale, skipped, or misaligned with ROS/teleop episodes.

## Handoffs
- Use `$isaac-sim-60-runtime` when Isaac Sim startup, GPU, container, livestream, or headless runtime readiness is the issue.
- Use `$isaac-sim-60-ros2-sitl` when the output is a ROS topic, ROS clock/publish rate, or LeRobot bridge contract.
- Use `$isaac-sim-omnigraph-builder` when graph nodes, execution pins, or ROS/sensor OmniGraph wiring are the issue.
- Use `$isaac-sim-viewport-debugger` when visual framing or viewport screenshots are needed instead of sensor render-product data.
- Use `$isaac-sim-60-troubleshooting` when logs, crashes, blank renders, or broad runtime symptoms dominate the diagnosis.
