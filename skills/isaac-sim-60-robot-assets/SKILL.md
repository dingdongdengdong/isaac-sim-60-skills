---
name: isaac-sim-60-robot-assets
description: Use when importing, loading, converting, classifying, or source-mapping robot assets in Isaac Sim 6.0-family workflows, including SimReady USD, OpenUSD prim mapping, Asset Structure, URDF/MJCF importers, articulations, joint limits, mimic joints, Surface Gripper migration, Newton schema awareness, AmazingHand, or this workspace's `echo_full_robot_arm_hand.usd`.
---

# Isaac Sim 6.0 Robot Assets

## Overview
Use this skill to classify and map robot assets before controllability work. It owns source identity, SimReady/OpenUSD import context, prim mapping, and detection of the visual/rigid-body-but-not-articulated gap.

## Workflow
1. Prefer the validated SimReady USD when working in this workspace; use legacy URDF/MJCF only as importer or control-reference baselines.
2. Read `references/robot-assets.md` before changing USD loading, importer settings, joint names, Surface Gripper bindings, Newton/PhysX schemas, or AmazingHand physics.
3. Read `references/articulation-binding-gap.md` when a converted USD has meshes/rigid bodies but zero physics joints or articulation roots.
4. Write mapping evidence to `isaacsim_test/artifacts/simready_prim_mapping.json` when inspecting or binding prims.
5. If a command cannot yet drive a real articulation, record `binding_pending` instead of substituting a hidden stand-in.
6. Hand off to `$isaac-sim-60-articulation-builder` when the next step is adding articulation root, physics joints, limits, drives, and scaffold validation.
7. Hand off to `$isaac-sim-robot-setup-tuning` only after joints/root/drives exist and the problem is gains, colliders, mass, inertia, closed loops, grippers, or backend-specific physics behavior.
8. Use NVIDIA upstream CAD-to-SimReady or USD performance skills for broad Omniverse conversion/optimization work when installed; then return here to classify Isaac Sim articulation/control readiness.

## Workspace Priorities
- Primary asset: `isaacsim_test/outputs/simready/echo_full/pipeline/04_conform/repair-loop-02-fet005/fet005-grasp/echo_full_robot_arm_hand.usd`.
- Keep the 13D LeRobot joint contract coordinated with `$isaac-sim-60-ros2-sitl`.
- For AmazingHand, the stable default is a static MJCF visual shell plus a simplified Isaac-oriented collision/physics tree unless the user explicitly asks for full hand physics.

## References
- Read `references/robot-assets.md` for official importer/setup links, local asset paths, 5.1-to-6.0 migration notes, and known hand constraints.
- Read `references/articulation-binding-gap.md` for the visual/rigid-body-but-not-controllable-articulation case, then hand off to `$isaac-sim-60-articulation-builder` for scaffold authoring.
