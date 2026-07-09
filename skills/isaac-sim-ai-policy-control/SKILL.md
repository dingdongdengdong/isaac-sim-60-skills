---
name: isaac-sim-ai-policy-control
description: Use when wiring AI, RL, imitation-learning, Isaac Lab, PyTorch/ONNX, policy inference, learned controllers, or planner outputs into Isaac Sim 6.0.0 robot control loops; includes observation/action mapping, ROS 2 or direct Python control paths, timing, safety limits, and verification for simulated robot behavior.
---

# Isaac Sim AI Policy Control

Use this skill to turn a trained or scripted AI policy into a repeatable Isaac Sim control loop. Keep the control surface explicit: what observes the robot, what computes actions, what publishes or applies commands, and what evidence proves the robot actually followed the policy.

## Workflow
1. Identify the control path: direct Isaac Sim Python stepping, ROS 2 bridge topic loop, OmniGraph Action Graph, Isaac Lab policy deployment, MoveIt/cuMotion planner output, or LeRobot/imitation policy.
2. Read `references/ai-policy-control.md` before changing policy inputs, action scaling, timing, command topics, or safety limits.
3. Freeze the robot contract: articulation path, joint names/order, command units, action bounds, observation fields, control rate, and reset behavior.
4. Run a baseline without the policy: load the robot, step physics, publish or apply a zero/hold command, and confirm stable joint states.
5. Add the policy behind a thin adapter that converts sim observations to model inputs and model outputs to bounded robot commands.
6. Verify incrementally: one step, short rollout, reset/replay, then longer rollout with screenshots or logs.
7. Save evidence: model path, config files, topic names, joint order, action scale, policy frequency, seed, rollout length, success/failure symptoms, and artifacts.

## Read Order
- Read `references/ai-policy-control.md` for policy deployment surfaces, timing, ROS 2 integration, safety checks, and verification patterns.
- Use `$isaac-sim-python-scripting` for standalone `SimulationApp` setup, extension enabling, and direct scene stepping.
- Use `$isaac-sim-60-ros2-sitl` when the AI controller talks through `/leader/joint_commands`, `/follower/joint_states`, ROS_DOMAIN_ID, LeRobot, Foxglove, or phone teleop.
- Use `$isaac-sim-omnigraph-builder` when the policy loop depends on Action Graph nodes, ROS 2 nodes, simulation ticks, or custom OmniGraph nodes.
- Use `$isaac-sim-robot-setup-tuning` when the policy is unstable because of gains, masses, colliders, joint limits, or articulation setup.
- Use `$isaac-sim-viewport-debugger` when visual evidence is needed to confirm motion, contact, grasping, navigation, or failures.

## Non-Negotiables
- Do not connect an unbounded model output directly to articulation drives or ROS command topics.
- Do not change joint order, units, or topic names silently.
- Do not evaluate policy quality until a zero/hold command keeps the robot stable.
- Do not mix training, deployment, asset tuning, and bridge debugging in one change; isolate the failing layer.
- Do not call a rollout successful using logs alone when the task is visual or contact-dependent; capture viewport or camera evidence.
