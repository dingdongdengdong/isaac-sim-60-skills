# Isaac Sim 6.0 Skills

Custom Codex/Agent Skills for NVIDIA Isaac Sim 6.0 robotics simulation workflows.

## Included skills

- `isaac-sim-60-runtime` — Isaac Sim 6.0 container/runtime setup, host checks, headless screenshot workflow.
- `isaac-sim-60-ros2-sitl` — ROS 2 bridge, LeRobot/Foxglove/phone teleop, 13D joint command/state contract.
- `isaac-sim-60-robot-assets` — SimReady USD loading, URDF/MJCF import, articulation mapping, AmazingHand notes.
- `isaac-sim-60-sensors-sdg` — cameras, RTX Lidar/Radar, multitick rendering, Replicator and dataset workflows.
- `isaac-sim-60-troubleshooting` — log-driven triage for Docker, headless rendering, ROS 2, assets, sensors, and contact physics.
- `isaac-sim-viewport-debugger` — active viewport framing, camera switching, screenshot capture, and before/after visual evidence reports.

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

## Validate

```bash
python3 scripts/validate.py
```

The validator checks each skill with Codex's `quick_validate.py` when available and falls back to frontmatter/file checks otherwise.
