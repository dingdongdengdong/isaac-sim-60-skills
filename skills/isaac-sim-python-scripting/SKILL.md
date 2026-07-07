---
name: isaac-sim-python-scripting
description: Use when writing, reviewing, or debugging Isaac Sim 6.0.0 Python scripts, standalone SimulationApp workflows, interactive Script Editor snippets, headless automation, extension enabling, app lifecycle, stage setup snippets, robot simulation snippets, Python server/Jupyter/VS Code/MCP surfaces, or Isaac Sim Python environment issues.
---

# Isaac Sim Python Scripting

Use this skill to choose the right Isaac Sim Python entrypoint and avoid common lifecycle errors. The main rule: create `SimulationApp` before importing Omniverse or Isaac Sim runtime modules in standalone scripts.

## Workflow
1. Identify the script surface: standalone command, interactive Script Editor, Jupyter, extension code, remote Python server, MCP-driven session, or generated extension template.
2. If Isaac Sim is not already running, coordinate launch/runtime checks with `$isaac-sim-60-runtime`.
3. Read `references/python-entrypoints.md` before choosing `python.sh`, pip package execution, Script Editor, remote server, MCP, or notebook.
4. For standalone scripts, instantiate `SimulationApp` first, then import `omni.*`, `pxr.*`, or `isaacsim.*` runtime modules.
5. Enable required extensions before using their APIs.
6. Load or create the stage, wait for app updates when assets or extensions need initialization, then run the smallest reproducible operation.
7. Save diagnostics under a new output directory and close `SimulationApp` when the script owns the app lifecycle.

## Read Order
- Read `references/python-entrypoints.md` for standalone, interactive, notebook, Python server, MCP, and container choices.
- Read `references/simulation-app-patterns.md` for import order, headless mode, update loops, version/migration notes, and shutdown.
- Read `references/extensions-and-environment.md` for extension enabling, Python paths, VS Code settings, packages, and `omni.isaac.*` to `isaacsim.*` migration risk.
- Read `references/scene-and-robot-scripting.md` for stage setup, asset loading, robot simulation snippets, and handoff to other skills.

## Handoffs
- Use `$isaac-sim-viewport-debugger` when the script must save visual evidence.
- Use `$isaac-sim-omnigraph-builder` when the script creates or edits Action Graphs.
- Use `$isaac-sim-robot-setup-tuning` when the script changes joints, drives, colliders, or robot physics.
- Use `$isaac-sim-60-sensors-sdg` when the script creates cameras, sensors, Replicator datasets, MobilityGen runs, or teleop episodes.
- Use `$isaac-sim-60-troubleshooting` when startup, import, extension, or artifact generation fails.

## Non-Negotiables
- Do not import Omniverse runtime modules before `SimulationApp` in standalone scripts.
- Do not use GUI-only APIs in headless mode without a documented rendering or viewport path.
- Do not write generated diagnostics into the source asset directory.
- Do not leave a script-owned `SimulationApp` running after automation completes.
