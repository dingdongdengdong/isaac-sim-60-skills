---
name: isaac-sim-teleop-policy-data-loop
description: Use when recording, replaying, validating, or converting Isaac Sim 6.0.0 teleoperation episodes for imitation learning, LeRobot, policy training, policy evaluation, phone/keyboard/joystick control, demonstration datasets, or sim-to-policy data capture.
---

# Isaac Sim Teleop Policy Data Loop

Use this skill when human or scripted teleoperation should become reliable policy data. Treat recording, replay, dataset conversion, and policy evaluation as separate stages with explicit schemas.

## Workflow
1. Identify the teleop source: phone UI, keyboard, joystick, ROS 2 topic, scripted controller, or LeRobot leader/follower path.
2. Read `references/teleop-policy-data-loop.md` before changing episode schema, action order, observation fields, timestamps, or replay logic.
3. Freeze the command/observation contract: joint order, action units, topic names, camera names, sensor rates, and reset state.
4. Record a short smoke episode and immediately replay it in the same scene.
5. Validate timing, dropped frames, action bounds, observation completeness, and final task state.
6. Convert or export only after replay proves the raw episode is coherent.
7. Save evidence: source controls, schema, episode count, replay result, visual artifact, and known limitations.

## Read Order
- Read `references/teleop-policy-data-loop.md` for recording, replay, schema, and quality gates.
- Use `$isaac-sim-60-ros2-sitl` for LeRobot, phone teleop, `/leader/joint_commands`, `/follower/joint_states`, and ROS bridge stability.
- Use `$isaac-sim-ai-policy-control` when replayed episodes become policy inputs, imitation baselines, or policy evaluation rollouts.
- Use `$isaac-sim-60-sensors-sdg` when dataset quality depends on cameras, lidar, annotators, randomization, or Replicator outputs.
- Use `$isaac-sim-viewport-debugger` to capture demonstrations and replay evidence.

## Non-Negotiables
- Do not change episode action order or units without versioning the dataset schema.
- Do not train or evaluate a policy on episodes that cannot replay.
- Do not merge episodes from different robot contracts without an explicit conversion step.
- Do not treat recorded commands as ground truth if simulated measured state diverged; log both command and observation.
