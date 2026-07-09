---
name: isaac-sim-ai-navigation-control
description: Use when connecting AI-generated navigation goals, ROS 2 Nav2, autonomous mobile robots, maps, localization, path planning, obstacle avoidance, multi-robot navigation, or simulated base control to Isaac Sim 6.0.0 verification.
---

# Isaac Sim AI Navigation Control

Use this skill when an AI system chooses where a simulated robot should move and Isaac Sim/ROS 2 must prove the robot can localize, plan, avoid obstacles, and reach the goal.

## Workflow
1. Identify the navigation stack: ROS 2 Nav2, direct base controller, OmniGraph ROS 2 bridge, custom planner, or AI goal generator.
2. Read `references/ai-navigation-control.md` before changing maps, frames, localization, goals, costmaps, or controller parameters.
3. Validate the navigation contract: robot base frame, odometry source, TF tree, map frame, sensor topics, velocity command topic, and goal message type.
4. Run localization and odometry without AI-generated goals.
5. Send one hand-authored safe goal and verify planning plus execution.
6. Add the AI goal generator behind a validator that bounds workspace, frame, speed, and obstacle assumptions.
7. Save evidence: goal, map/localization state, path, controller status, final pose error, collision/near-miss notes, and viewport or camera capture.

## Read Order
- Read `references/ai-navigation-control.md` for Nav2, TF, maps, goal validation, and evidence patterns.
- Use `$isaac-sim-60-ros2-sitl` for ROS_DOMAIN_ID, ROS 2 bridge health, topic visibility, and ROS 2 graph issues.
- Use `$isaac-sim-ai-policy-control` when a learned policy directly emits base commands or waypoint actions.
- Use `$isaac-sim-60-sensors-sdg` when navigation depends on camera, lidar, radar, or synthetic sensor streams.
- Use `$isaac-sim-viewport-debugger` to capture robot pose, path context, obstacles, and final goal state.

## Non-Negotiables
- Do not send AI-generated navigation goals until TF, odometry, localization, and a hand-authored goal work.
- Do not mix map-frame, odom-frame, and world-frame coordinates without explicit conversion.
- Do not call a navigation rollout successful from `/cmd_vel` activity alone; verify final pose and obstacle clearance.
- Do not debug AI planning quality until the same goal is reachable with a manual command.
