---
name: isaac-sim-60-runtime
description: Use when starting, installing, validating, or scripting NVIDIA Isaac Sim 6.0.0 runtime environments, especially Docker/NGC containers, headless screenshots, GPU/driver checks, cache mounts, EULA variables, or this workspace's `isaacsim_test` compose service.
---

# Isaac Sim 6.0 Runtime

## Overview
Use this skill to make Isaac Sim 6.0 runtime work reproducible before debugging scene, ROS, or physics logic. Prefer read-only checks first, then run the smallest startup command that produces evidence.

## Workflow
1. Identify the launch surface: local install, pip, container, or this repo's `isaacsim_test/docker-compose.yml`.
2. Run `scripts/check_isaacsim60_host.sh` from this skill when host/container readiness is unclear.
3. For this workspace, treat `isaacsim_test/README.md` and `isaacsim_test/docker-compose.yml` as the local source of truth.
4. For headless validation, prefer `bash isaacsim_test/run_isaacsim60_headless_screenshot.sh`; it sets `HEADLESS=1`, `SCREENSHOT_ON_STARTUP=1`, and writes artifacts under `isaacsim_test/artifacts/`.
5. If startup fails, preserve the log path and switch to `$isaac-sim-60-troubleshooting`.

## Runtime Defaults
- Image: `nvcr.io/nvidia/isaac-sim:6.0.0`.
- Required env for containers: `ACCEPT_EULA=Y`, `NVIDIA_VISIBLE_DEVICES=all`, `NVIDIA_DRIVER_CAPABILITIES=all`.
- This workspace's compose service: `isaac-sim-60`.
- This workspace uses ROS 2 Humble in the container and `ROS_DOMAIN_ID=42` unless overridden.
- Keep Isaac Sim caches in Docker volumes or host cache mounts; do not delete caches unless the user asks.

## References
- Read `references/runtime.md` for official 6.0 links, compatibility notes, and workspace commands.
- Use installed `$omniverse-usd-performance-tuning` for USD load/FPS/memory optimization after the runtime starts.
