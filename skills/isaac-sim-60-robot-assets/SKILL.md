---
name: isaac-sim-60-robot-assets
description: Use when importing, loading, converting, or binding robot assets in Isaac Sim 6.0.0, including SimReady USD, OpenUSD prim mapping, URDF or MJCF importers, articulations, joint limits, mimic joints, Surface Gripper migration, AmazingHand, or this workspace's `echo_full_robot_arm_hand.usd`.
---

# Isaac Sim 6.0 Robot Assets

## Overview
Use this skill to move robot asset work from “loads visually” to “has explicit evidence for articulation, control mapping, and contact behavior.”

## Workflow
1. Prefer the validated SimReady USD when working in this workspace; use legacy URDF only as a control-reference baseline.
2. Read `references/robot-assets.md` before changing USD loading, importer settings, joint names, or AmazingHand physics.
3. Write mapping evidence to `isaacsim_test/artifacts/simready_prim_mapping.json` when inspecting or binding prims.
4. If a command cannot yet drive a real articulation, record `binding_pending` instead of substituting a hidden stand-in.
5. Use installed `$omniverse-cad-to-simready` for CAD-to-SimReady conversion and `$omniverse-usd-performance-tuning` for heavy USD performance work.

## Workspace Priorities
- Primary asset: `isaacsim_test/outputs/simready/echo_full/pipeline/04_conform/repair-loop-02-fet005/fet005-grasp/echo_full_robot_arm_hand.usd`.
- Keep the 13D LeRobot joint contract coordinated with `$isaac-sim-60-ros2-sitl`.
- For AmazingHand, the stable default is a static MJCF visual shell plus a simplified Isaac-oriented collision/physics tree.

## References
- Read `references/robot-assets.md` for official importer links, local asset paths, and known hand constraints.
