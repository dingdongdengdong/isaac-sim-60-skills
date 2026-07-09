---
name: isaac-sim-motion-generation-control
description: Use when connecting AI-generated goals, task planners, MoveIt 2, cuMotion/cuRobo, motion generation, IK, trajectory planning, pose targets, grasp targets, or collision-aware robot manipulation to Isaac Sim 6.0.0 execution and verification.
---

# Isaac Sim Motion Generation Control

Use this skill when an AI system or task planner chooses goals and Isaac Sim must turn them into physically plausible robot motion. Keep goal generation, planning, controller execution, and verification separate.

## Workflow
1. Identify the command level: end-effector pose, grasp target, joint target, trajectory, navigation goal, or high-level task command.
2. Read `references/motion-generation-control.md` before editing planner configs, collision-world setup, IK targets, trajectory followers, or ROS 2 MoveIt bridges.
3. Validate the robot contract: articulation path, joint names/order, limits, end-effector frame, planning group, collision geometry, and controller type.
4. Validate the generated goal before planning: frame, units, reachability, object pose freshness, and safety bounds.
5. Run planning without execution first; save planner status, path length, joint limits, and collision result.
6. Execute one short bounded trajectory and compare commanded vs measured joint states.
7. Capture evidence: goal, planner config, trajectory summary, controller tracking, collision status, screenshot or viewport capture when useful.

## Read Order
- Read `references/motion-generation-control.md` for planner selection, goal validation, MoveIt/cuMotion/cuRobo checks, and execution evidence.
- Use `$isaac-sim-ai-policy-control` when a learned model generates goals or directly emits low-level actions.
- Use `$isaac-sim-60-ros2-sitl` when using MoveIt 2, ROS controllers, `/joint_states`, `/tf`, or ROS 2 bridge topics.
- Use `$isaac-sim-robot-setup-tuning` if planned trajectories fail because drives cannot track, colliders are wrong, or mass/inertia causes instability.
- Use `$isaac-sim-viewport-debugger` to verify end-effector frames, obstacle geometry, target poses, and before/after execution.

## Non-Negotiables
- Do not execute a planner result if status, collision checking, or joint-limit validation failed.
- Do not trust a planner-only success as simulated execution success.
- Do not mix frame conversions with planning logic; make world/base/tool frame conversion explicit.
- Do not let AI-generated poses bypass reachability, collision, workspace, or speed limits.
- Do not debug policy quality until the same target can be reached through a hand-authored goal.
