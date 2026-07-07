---
name: isaac-sim-60-troubleshooting
description: Use when Isaac Sim 6.0.0 fails, hangs, crashes, renders blank images, cannot pull Docker images, has GPU/container/cache/log problems, misses ROS 2 topics, has stale bridge data, broken robot joints, unstable contacts, failed Replicator/SDG/teleop outputs, headless screenshots, or needs log-based evidence from this workspace's `isaacsim_test` artifacts.
---

# Isaac Sim 6.0 Troubleshooting

## Overview
Use this skill to turn Isaac Sim failures into an evidence bundle, classify the failing subsystem, and choose one focused fix plus one verification command.

## Workflow
1. Capture the failing command, runtime mode, expected artifact, observed artifact, log path, Isaac Sim version, and whether the failure is startup/runtime, logs/crash, ROS 2 bridge, rendering/capture, robot physics, performance, sensor/SDG, or migration.
2. Run `scripts/summarize_isaacsim60_logs.py <log>` on available logs.
3. Start with `references/troubleshooting.md`, then read the smallest symptom playbook below.
4. Separate ignorable known-issue noise from actionable errors before proposing changes.
5. Prefer one focused fix plus one verification command. Do not rewrite scene/control architecture during triage.

## Evidence First
For this workspace, check:
- `isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log`
- `isaacsim_test/artifacts/isaacsim60_headless_status.json`
- `isaacsim_test/artifacts/simready_prim_mapping.json`
- `isaacsim_test/artifacts/hand_focus/`

## Read Order
- Read `references/troubleshooting.md` for official source links, the symptom matrix, version notes, and the minimal evidence bundle.
- Read `references/startup-runtime.md` for Docker pulls, GPU visibility, EULA/env vars, cache/log mounts, WebRTC/livestream, and headless/windowed startup.
- Read `references/logs-and-crashes.md` for log locations, summarizer use, known-issue noise, hangs, crashes, extension/import failures, and `omni.isaac.*` migration failures.
- Read `references/ros2-bridge.md` for missing topics, stale ROS data, `ROS_DOMAIN_ID`, RMW/QoS, Simulation Control, Foxglove, and LeRobot bridge failures.
- Read `references/rendering-capture.md` for blank screenshots, viewport/headless mismatch, Replicator writer failures, sensor capture artifacts, and livestream confusion.
- Read `references/robot-physics.md` for broken joints, unstable contacts, exploding robots, gripper failures, articulation/root/collider/drive issues, and backend mismatch.
- Read `references/performance-known-issues.md` for slow startup, shader warmup, CPU/GPU bottlenecks, cache state, known noisy warnings, and ignore-versus-fix decisions.

## Handoffs
- Use `$isaac-sim-60-runtime` after startup evidence points to host/container/GPU/install setup rather than application logic.
- Use `$isaac-sim-60-ros2-sitl` after the failure is narrowed to ROS topics, bridge contracts, Simulation Control, or LeRobot/Foxglove behavior.
- Use `$isaac-sim-60-robot-assets` for importer, USD composition, SimReady mapping, Surface Gripper migration, or AmazingHand asset-policy problems.
- Use `$isaac-sim-robot-setup-tuning` after robot physics symptoms require drive/collider/mass/inertia/backend tuning.
- Use `$isaac-sim-60-sensors-sdg` for sensor APIs, Replicator timing, annotators, render products, MobilityGen, teleop episodes, or SDG datasets.
