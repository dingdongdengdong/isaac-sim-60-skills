# Isaac Sim 6.0 Skills

Custom Codex/Agent Skills for NVIDIA Isaac Sim 6.0 robotics simulation workflows.

This pack is a **curated practical layer** over NVIDIA's official docs, not a mirror of the docs. Use it to choose the right Isaac Sim workflow, preserve local workspace contracts, collect evidence, and know when to hand off between runtime, ROS 2, assets, sensors/SDG, scripting, OmniGraph, viewport, and robot tuning skills.

## Version strategy

- Primary target: Isaac Sim 6.0-family workflows, with this workspace runtime default pinned to `nvcr.io/nvidia/isaac-sim:6.0.0` unless a workspace explicitly changes it.
- Migration context: Isaac Sim 5.1/5.1+ is covered where it affects 5.1-to-6.0 migration decisions, extension names, APIs, or importer behavior.
- Source quality: official NVIDIA Isaac Sim docs and release notes are the baseline. Third-party summaries are not used as normative guidance.

## Included skills

- `isaac-sim-60-runtime` — install/runtime surfaces, container/pip/workstation/cloud/livestream readiness, host checks, caches, logs, and headless screenshot workflows.
- `isaac-sim-60-ros2-sitl` — ROS 2 bridge, Simulation Control, Linux/Windows platform notes, LeRobot/Foxglove/phone teleop, and the 13D joint command/state contract.
- `isaac-sim-60-robot-assets` — SimReady/OpenUSD assets, URDF/MJCF import/export, Asset Structure, source prim mapping, binding-gap classification, Newton schema awareness, Surface Gripper migration, and AmazingHand notes.
- `isaac-sim-60-articulation-builder` — post-SimReady controllability scaffolding: inspect visual/rigid-body USDs, generate explicit joint maps, author articulation roots/joints/drives into separate output layers, and produce validation reports.
- `isaac-sim-60-sensors-sdg` — cameras, RTX/physics/PhysX sensors, acoustic/proximity/raycast coverage, Replicator, Action/Event SDG, MobilityGen, teleoperation SDG, and dataset timing.
- `isaac-sim-60-troubleshooting` — evidence-first triage for startup, Docker, cache/logs, headless rendering, ROS 2, assets, sensors, SDG, performance, and robot/contact physics.
- `isaac-sim-viewport-debugger` — active viewport framing, camera switching, screenshot capture, and before/after visual evidence reports.
- `isaac-sim-python-scripting` — standalone and interactive Python scripting, SimulationApp lifecycle, extension enabling, remote Python/Jupyter/VS Code/MCP surfaces, and scene automation.
- `isaac-sim-omnigraph-builder` — scripted Action Graph creation, ROS 2/sensor graph wiring, simulation triggers, custom nodes, and graph execution debugging.
- `isaac-sim-robot-setup-tuning` — robot drive gains, colliders, mass/inertia, closed-loop structures, grippers, Newton/PhysX backend notes, Asset Transformer, and asset tuning evidence.

## Official doc coverage map

Start with `skills/isaac-sim-60-runtime/references/official-doc-map.md` when deciding whether a task belongs in this pack or needs a direct official-doc lookup. Each skill then contains smaller practical references with official links, migration notes, evidence checklists, and handoffs.

## NVIDIA upstream skills

This repo stays focused on Isaac Sim 6.0-family workflows. NVIDIA's broader skills repo (`https://github.com/nvidia/skills`) has useful Omniverse skills for CAD-to-SimReady conversion, USD performance tuning, and realtime viewer apps. See `skills/isaac-sim-60-runtime/references/nvidia-skills-interop.md` for when to hand off to those upstream skills.

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

The validator checks each skill with Codex's `quick_validate.py` when available and falls back to frontmatter/file checks otherwise. It also syntax-checks bundled shell/Python helper scripts.
