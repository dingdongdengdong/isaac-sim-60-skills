# Isaac Sim 6.0 Troubleshooting Index

## Official sources
- Troubleshooting hub: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/troubleshooting.html
- Known issues: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/known_issues.html
- Setup tips and logs/cache locations: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_faq.html
- Container installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_container.html
- ROS 2 troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/troubleshooting.html
- Replicator troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/troubleshooting.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html
- Digital Twin troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/digital_twin/troubleshooting.html
- Performance handbook: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/reference_material/sim_performance_optimization_handbook.html
- 6.0 release notes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html
- 5.1 release notes: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/overview/release_notes.html

## Symptom matrix
- Cannot start, pull image, open GUI, or stream: `startup-runtime.md`.
- Crash, hang, import error, extension error, suspicious log noise: `logs-and-crashes.md`.
- Missing/stale ROS topics or Simulation Control services: `ros2-bridge.md`.
- Blank screenshots, no files, stale images, livestream confusion: `rendering-capture.md`.
- Robot collapses, explodes, detaches, cannot grasp, wrong joint motion: `robot-physics.md`.
- Slow startup, poor FPS, shader warmup, cache state, noisy known issues: `performance-known-issues.md`.
- Sensor/SDG output wrong after basic runtime works: hand off to `$isaac-sim-60-sensors-sdg`.

## Minimal evidence bundle
Always preserve:
- exact command and working directory
- Isaac Sim version and install surface
- runtime mode: GUI, headless, container, workstation, pip, cloud, livestream
- expected artifact and observed artifact
- log path and first actionable error
- relevant env vars: `ROS_DOMAIN_ID`, `RMW_IMPLEMENTATION`, `ACCEPT_EULA`, GPU visibility
- recent changes: image tag, extension name migration, asset path, graph, sensor, or ROS contract

## Workspace evidence paths
- `isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log`
- `isaacsim_test/artifacts/isaacsim60_headless_status.json`
- `isaacsim_test/artifacts/simready_prim_mapping.json`
- `isaacsim_test/artifacts/hand_focus/`

## Version note
- 5.1 is unsupported for new fixes/features and warned that deprecated extensions would be removed in 6.0.
- If a migrated project fails with missing modules/extensions, check `omni.isaac.*` to `isaacsim.*` migration before changing Docker, Python paths, or ROS settings.
- Treat 6.0.0 docs as the pinned 6.0.0 guidance, while preserving local 6.0.0 image pins unless changed deliberately.

## Ignore versus fix rule
Do not treat every warning as actionable. First decide whether the warning explains the missing artifact. If not, record it as known/noisy and continue to the first error that blocks startup, rendering, ROS, asset load, sensor output, or dataset generation.

## Handoff rule
After evidence narrows the subsystem, stop broad troubleshooting and hand off to the focused skill. Include the command, log, artifact path, version/install surface, and the one symptom that must be verified after the fix.
