---
name: isaac-sim-60-troubleshooting
description: Use when Isaac Sim 6.0.0 fails, hangs, crashes, renders blank images, cannot pull Docker images, misses ROS 2 topics, has broken robot joints, unstable contacts, failed headless screenshots, or needs log-based evidence from this workspace's `isaacsim_test` artifacts.
---

# Isaac Sim 6.0 Troubleshooting

## Overview
Use this skill to diagnose from evidence instead of guessing. Always collect the command, log path, runtime mode, and expected artifact before proposing fixes.

## Workflow
1. Capture the failing command and whether it is container, local app, ROS bridge, robot asset, sensor, or physics/contact related.
2. Run `scripts/summarize_isaacsim60_logs.py <log>` on available logs.
3. Read `references/troubleshooting.md` for symptom-specific checks.
4. Prefer one focused fix plus one verification command. Do not rewrite scene/control architecture during triage.
5. Escalate to `$isaac-sim-60-runtime`, `$isaac-sim-60-ros2-sitl`, `$isaac-sim-60-robot-assets`, or `$isaac-sim-60-sensors-sdg` once the failing subsystem is clear.

## Evidence First
For this workspace, check:
- `isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log`
- `isaacsim_test/artifacts/isaacsim60_headless_status.json`
- `isaacsim_test/artifacts/simready_prim_mapping.json`
- `isaacsim_test/artifacts/hand_focus/`

## References
- Read `references/troubleshooting.md` for official troubleshooting links and local symptoms.
