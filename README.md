# Isaac Sim 6.0 Skills

Custom Codex/Agent Skills for NVIDIA Isaac Sim 6.0 robotics simulation workflows.

## Included skills

- `isaac-sim-60-runtime` — Isaac Sim 6.0 container/runtime setup, host checks, headless screenshot workflow.
- `isaac-sim-60-ros2-sitl` — ROS 2 bridge, LeRobot/Foxglove/phone teleop, 13D joint command/state contract.
- `isaac-sim-60-robot-assets` — SimReady USD loading, URDF/MJCF import, articulation mapping, AmazingHand notes.
- `isaac-sim-60-sensors-sdg` — cameras, RTX Lidar/Radar, multitick rendering, Replicator and dataset workflows.
- `isaac-sim-60-troubleshooting` — log-driven triage for Docker, headless rendering, ROS 2, assets, sensors, and contact physics.
- `isaac-sim-viewport-debugger` — active viewport framing, camera switching, screenshot capture, and before/after visual evidence reports.
- `isaac-sim-python-scripting` — standalone and interactive Python scripting, SimulationApp lifecycle, extension enabling, and scene automation.
- `isaac-sim-omnigraph-builder` — scripted Action Graph creation, ROS 2/sensor graph wiring, custom node triage, and graph execution debugging.
- `isaac-sim-robot-setup-tuning` — robot drive gains, colliders, mass/inertia, closed-loop structures, grippers, and asset tuning evidence.
- `isaac-sim-ai-policy-control` — AI/RL policy deployment, observation/action mapping, bounded control loops, ROS 2 policy nodes, and rollout evidence.
- `isaac-sim-motion-generation-control` — AI-generated goals, MoveIt 2, cuMotion/cuRobo, IK, trajectory execution, and collision-aware motion evidence.
- `isaac-sim-ai-navigation-control` — AI navigation goals, ROS 2 Nav2, localization, maps, path following, and final-pose evidence.
- `isaac-sim-teleop-policy-data-loop` — teleoperation recording, replay validation, dataset schema stability, and policy-data conversion evidence.

## Install into Codex

From this repository root:

```bash
bash scripts/install_to_codex.sh
```

By default this copies skills to `${CODEX_HOME:-$HOME/.codex}/skills`.
Set `CODEX_SKILLS_DIR=/custom/path` to override the destination.
Restart Codex after installing.

## Use as a Git submodule

From a parent repo:

```bash
git submodule add <repo-url> .agents/skill-packs/isaac-sim-60-skills
git submodule update --init --recursive
```

Then install or sync the contained skills:

```bash
bash .agents/skill-packs/isaac-sim-60-skills/scripts/install_to_codex.sh
```

## NVIDIA upstream skills

This repo keeps NVIDIA's public skills repository as an isolated submodule at `vendor/nvidia-skills`.
Use that tree for upstream reference material, and keep this repo's custom Isaac Sim 6.0 skills under `skills/` to avoid namespace and validation conflicts.

## Validate

```bash
python3 scripts/validate.py
```

The validator checks each skill with Codex's `quick_validate.py` when available and falls back to frontmatter/file checks otherwise.
