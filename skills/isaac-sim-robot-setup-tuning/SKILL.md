---
name: isaac-sim-robot-setup-tuning
description: Use when tuning Isaac Sim robot setup, drive gains, stiffness, damping, articulation stability, colliders, mass/inertia, closed-loop structures, mimic joints, grippers, Gain Tuner results, asset optimization, OpenUSD tuning best practices, or robot setup troubleshooting.
---

# Isaac Sim Robot Setup Tuning

Use this skill to move a robot asset from "imports and appears" to "simulates with stable, explainable physics." Treat tuning as evidence-driven: inspect structure, isolate one subsystem, run a small test, record results, then change one thing.

## Workflow
1. Identify the asset source and structure: SimReady USD, imported URDF, imported MJCF, CAD-converted USD, or manually assembled USD.
2. Read `references/asset-validation.md` before editing layers, physics schemas, or asset structure.
3. Inspect articulation root, links, joints, drives, colliders, mass, inertia, and payload/layer organization.
4. Choose one tuning target: drive gains, collider/contact behavior, mass/inertia, closed-loop/mimic behavior, gripper behavior, or asset optimization.
5. Run a minimal test: snap-to-limits, step response, sine response, gravity hold, collision pair check, gripper closure, or one-joint command.
6. Save before/after evidence: USD path, prim paths, changed properties, test command, screenshots when useful, and numeric outcomes.
7. Re-run validation after edits and hand off runtime failures to `$isaac-sim-60-troubleshooting`.

## Read Order
- Read `references/asset-validation.md` for validation, layers, Asset Structure 3.0, and source-of-truth rules.
- Read `references/drive-gains.md` for stiffness/damping, Gain Tuner, step/sine tests, and stability interpretation.
- Read `references/colliders-mass-inertia.md` for collider approximation, contact stability, mass, inertia, and solver symptoms.
- Read `references/closed-loop-and-grippers.md` for closed-loop structures, mimic joints, dexterous hands, and gripper testing.
- Read `references/troubleshooting.md` when the robot collapses, explodes, detaches, jitters, or cannot reach limits.

## Handoffs
- Use `$isaac-sim-60-robot-assets` for import, mapping, SimReady source paths, URDF/MJCF conversion, and AmazingHand asset policy.
- Use `$isaac-sim-viewport-debugger` to frame links, joints, and before/after visual evidence.
- Use `$isaac-sim-60-ros2-sitl` when tuning changes the ROS/LeRobot joint contract.
- Use `$isaac-sim-60-sensors-sdg` when tuning affects sensor placement or output.

## Non-Negotiables
- Do not tune multiple independent properties at once unless recording a deliberate batch.
- Do not edit a source USD destructively; use a dedicated output layer or diagnostics copy unless explicitly requested.
- Do not treat visual attachment as proof of physics correctness.
- Do not ignore zero gains, missing colliders, bad mass/inertia, or broken parent/child joint paths just because the model loads.
