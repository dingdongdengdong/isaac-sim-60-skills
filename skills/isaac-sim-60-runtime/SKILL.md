---
name: isaac-sim-60-runtime
description: Use when starting, installing, validating, or scripting NVIDIA Isaac Sim 6.0.0 runtime environments, especially Docker/NGC containers, pip/workstation installs, livestream/WebRTC, cloud deployment, GPU/driver checks, cache mounts, EULA variables, or this workspace's `isaacsim_test` compose service.
---

# Isaac Sim 6.0 Runtime

## Overview
Use this skill to make Isaac Sim 6.0 runtime work reproducible before debugging scene, ROS, sensor, or physics logic. Prefer read-only checks first, then run the smallest startup command that produces evidence.

## Workflow
1. Identify the launch surface: workstation install, pip install, container, cloud/remote workstation, livestream client, or this repo's `isaacsim_test/docker-compose.yml`.
2. Read `references/official-doc-map.md` if the task might belong to a different Isaac Sim skill or a direct official-doc lookup.
3. Read `references/runtime.md` before changing image tags, install modality, cache/log mounts, livestream, or cloud startup assumptions.
4. Run `scripts/check_isaacsim60_host.sh` from this skill when host/container readiness is unclear.
5. For this workspace, treat `isaacsim_test/README.md` and `isaacsim_test/docker-compose.yml` as the local source of truth.
6. For headless validation, prefer `bash isaacsim_test/run_isaacsim60_headless_screenshot.sh`; it sets `HEADLESS=1`, `SCREENSHOT_ON_STARTUP=1`, and writes artifacts under `isaacsim_test/artifacts/`.
7. If startup fails, preserve the log path and switch to `$isaac-sim-60-troubleshooting`.

## Runtime Defaults
- Default image remains `nvcr.io/nvidia/isaac-sim:6.0.0` unless the workspace explicitly pins a a different image.
- Required env for containers: `ACCEPT_EULA=Y`, `NVIDIA_VISIBLE_DEVICES=all`, `NVIDIA_DRIVER_CAPABILITIES=all`.
- This workspace's compose service: `isaac-sim-60`.
- This workspace uses ROS 2 Humble in the container and `ROS_DOMAIN_ID=42` unless overridden.
- Keep Isaac Sim caches in Docker volumes or host cache mounts; do not delete caches unless the user asks.

## References
- Read `references/official-doc-map.md` for the official-doc coverage/routing map and 5.1-to-6.0 migration anchors.
- Read `references/nvidia-skills-interop.md` when deciding whether to use upstream NVIDIA Omniverse skills for SimReady conversion, USD optimization, or viewer workflows.
- Read `references/runtime.md` for official 6.0 install/runtime links, compatibility notes, and workspace commands.
- Use installed `$omniverse-usd-performance-tuning` for USD load/FPS/memory optimization after the runtime starts.
