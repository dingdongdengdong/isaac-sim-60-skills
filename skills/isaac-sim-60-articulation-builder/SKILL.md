---
name: isaac-sim-60-articulation-builder
description: "Use after SimReady/CAD conversion when a USD loads visually or has rigid bodies but is not yet a controllable Isaac Sim robot articulation. Builds explicit articulation scaffolds from mapping files: articulation root, physics joints, limits, drives, validation reports, and handoff to tuning or ROS/LeRobot."
---

# Isaac Sim Articulation Builder

Use this skill for the post-SimReady step: convert a visual or rigid-body USD into a controllable Isaac Sim robot articulation. This skill is 6.0-focused and open across the 6.0 family; use 5.1/5.1+ notes only as migration context for older projects.

## Workflow
1. Start from a USD produced by SimReady, CAD conversion, URDF/MJCF import, or manual assembly.
2. Read `references/controllability-pipeline.md` to classify the asset and choose the next step.
3. Run `scripts/inspect_usd_articulation.py SOURCE.usd --out inspection.json` to collect counts and status.
4. If the asset has no physics joints or no articulation root, run `scripts/generate_articulation_map_template.py inspection.json --out articulation_map.json`.
5. Fill or review the mapping explicitly: link prims, parent/child joint pairs, joint type, axis, limits, drive parameters, and articulation root path.
6. Read `references/joint-authoring.md` and `references/articulation-root-and-drives.md` before authoring a scaffold.
7. Run `scripts/author_articulation_scaffold.py SOURCE.usd articulation_map.json --out OUTPUT.usd --report scaffold_report.json` to write a separate output layer/stage.
8. Re-run inspection on the output, then read `references/validation-and-handoff.md` before handing off to tuning, ROS, or LeRobot.

## Boundaries
- Do not infer correct robot kinematics automatically from CAD geometry.
- Do not edit the source USD in place; always write an output USD/layer and a report.
- Do not tune drive gains before valid joint body targets and articulation root exist.
- Do not wire ROS/LeRobot commands until real joint names and command order are verified.

## Read Order
- `references/controllability-pipeline.md`: end-to-end post-SimReady flow and status meanings.
- `references/joint-authoring.md`: mapping requirements, joint types, axes, limits, and parent/child relationships.
- `references/articulation-root-and-drives.md`: root placement, drives, controller readiness, and 5.1-to-6.0 migration notes.
- `references/validation-and-handoff.md`: inspection evidence, smoke tests, and handoff criteria.

## Handoffs
- Use `$isaac-sim-60-robot-assets` before this skill when source asset identity, conversion, SimReady path, or prim mapping is unclear.
- Use `$isaac-sim-robot-setup-tuning` after valid joints/root/drives exist and the issue is stability, gains, colliders, mass, inertia, closed loops, or grippers.
- Use `$isaac-sim-60-ros2-sitl` after a real joint list exists and the task is ROS/LeRobot topic binding.
- Use `$isaac-sim-viewport-debugger` for before/after visual evidence, not for proving physics controllability.
