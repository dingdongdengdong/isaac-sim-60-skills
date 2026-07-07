# Isaac Sim 6.0 Official Doc Map

## Official sources checked
- 6.0.0 release notes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html
- 6.0.0 migration guide index: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/index.html
- 5.1.0 release notes: https://docs.isaacsim.omniverse.nvidia.com/5.1.0/overview/release_notes.html
- 6.0 docs table of contents / task groupings: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/

## Pack strategy
This repo is a practical routing layer for 6.0-family Isaac Sim workflows. Do not copy NVIDIA docs wholesale. For each task, preserve official links, the smallest actionable workflow, migration gotchas, evidence to collect, and handoff to the neighboring skill when the issue crosses boundaries.

## Skill routing from official task groups
- Installation, requirements, containers, cloud deployment, livestream clients, caches, logs: `$isaac-sim-60-runtime` and `$isaac-sim-60-troubleshooting`.
- ROS 2 installation, tutorials, Simulation Control, QoS, bridge in standalone workflow, MoveIt/navigation: `$isaac-sim-60-ros2-sitl`; use `$isaac-sim-omnigraph-builder` for graph wiring.
- Importers/exporters, SimReady/OpenUSD assets, URDF/MJCF, Asset Structure, source prim mapping: `$isaac-sim-60-robot-assets`; use `$isaac-sim-60-articulation-builder` for post-SimReady articulation scaffolds; use `$isaac-sim-robot-setup-tuning` after joints/root/drives exist but physics is unstable.
- Cameras, RTX Lidar/Radar/Acoustic, physics sensors, PhysX SDK sensors, non-visual materials, multi-tick rendering: `$isaac-sim-60-sensors-sdg`.
- Replicator, Action/Event SDG, behavior-tree generation, MobilityGen, teleoperation SDG, dataset writers: `$isaac-sim-60-sensors-sdg`.
- Python scripting, Core API, standalone examples, Jupyter, Python server, MCP server, VS Code: `$isaac-sim-python-scripting`.
- OmniGraph interface, Python graph scripting, ROS/sensor Action Graphs, custom nodes: `$isaac-sim-omnigraph-builder`.
- Robot setup tutorials for adding joints/articulation roots/drives from explicit maps: `$isaac-sim-60-articulation-builder`; Gain Tuner, Asset Transformer, Robot Inspector/Poser, colliders, tuned drives, grippers, Newton actuators: `$isaac-sim-robot-setup-tuning`.
- Human visual evidence, active viewport, camera switching, before/after screenshots: `$isaac-sim-viewport-debugger`.

## 5.1-to-6.0 anchors
- Isaac Sim 5.1 docs warn that deprecated extensions would be removed in the next major 6.0 release; treat `omni.isaac.*` compatibility shims as gone in 6.0.
- 6.0 release notes require migration from `omni.isaac.*` to `isaacsim.*` extension names and push many APIs toward `isaacsim.core.experimental.*` and `isaacsim.core.simulation_manager`.
- 6.0 migration guide topics include camera sensors, RTX sensors, physics sensors, PhysX Lidar/generic/lightbeam, ROS 2 OmniGraph nodes, Replicator Agent, MobilityGen recordings, and Surface Gripper bindings.
- 5.1 is unsupported for new fixes/features; use it only to understand old projects and migration risk.

## When direct docs lookup is still required
Use official docs directly when the task requires exact API signatures, current package versions, cloud provider commands, or generated schema fields. Keep the skill output focused on routing, safety, evidence, and migration risk.

## Review cadence
When NVIDIA publishes a later patch, update official links and migration notes first, then decide whether local runtime image tags should change. Do not update the local image default as a documentation-only side effect.

## Upstream NVIDIA skills interop
For CAD-to-SimReady conversion, generic USD performance tuning, or standalone Omniverse viewer work, read `nvidia-skills-interop.md`. Keep Isaac Sim robot articulation/control ownership in this repo.
