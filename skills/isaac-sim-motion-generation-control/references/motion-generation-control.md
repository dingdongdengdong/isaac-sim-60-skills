# Motion Generation Control Reference

## Official Docs Checked
- Motion generation overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/motion_generation/index.html
- cuRobo/cuMotion manipulation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/manipulators/manipulators_curobo.html
- ROS 2 MoveIt tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_moveit.html
- ROS 2 manipulation tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_manipulation.html
- ROS 2 bridge Python workflows: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_python.html

## Planner Choice

| Planner path | Use when | Watch for |
| --- | --- | --- |
| Isaac Sim Motion Generation API | Direct Isaac Sim script controls the manipulator | robot descriptor, collision world, frame names |
| cuMotion/cuRobo | GPU-accelerated collision-aware manipulation is needed | device config, obstacle sync, warmup, trajectory retiming |
| MoveIt 2 | ROS 2 stack owns planning and execution | planning group, controllers, `/joint_states`, `/tf`, bridge timing |
| Custom IK/trajectory | Task is simple or highly constrained | joint limits, singularities, controller tracking |
| Learned goal generator plus planner | AI emits goals, planner emits motion | goal validity, frame conversion, safety envelope |

## Required Contract

Capture these before connecting AI-generated goals:

- Robot asset and articulation prim path.
- Planning group and active joint order.
- End-effector frame and base/world frame.
- Joint position, velocity, acceleration, and effort limits.
- Collision geometry source and obstacle update path.
- Controller interface: direct articulation command, ROS trajectory controller, position targets, or velocity commands.
- Planning timestep, execution timestep, and any retiming/smoothing.

## Goal Validation

Before calling the planner, check:

- The target pose is in the expected frame.
- Position units are meters and orientation convention is explicit.
- Target is inside a known workspace envelope.
- Object/obstacle pose is current enough for the task.
- The goal does not require self-collision, environment collision, or joint-limit violation.
- Speed, acceleration, and gripper/contact assumptions are bounded.

For AI-generated targets, log the raw model output and the validated goal passed to the planner. Never pass raw model output directly to a planner or controller.

## Plan-Then-Execute Sequence

1. Build or refresh the planning scene and collision world.
2. Run IK or planning with execution disabled.
3. Inspect planner status, final pose error, collision result, and joint-limit margins.
4. If planning passes, execute slowly or with reduced action scale first.
5. Compare commanded trajectory points with measured joint states.
6. Save a viewport or camera capture for spatial tasks, grasping, or obstacle avoidance.

If plan succeeds but execution fails, investigate drives, controller gains, timestep, mass/inertia, and command interface before changing the AI goal generator.

## MoveIt 2 Checks

For ROS 2 MoveIt workflows:

```bash
export ROS_DOMAIN_ID=42
source /opt/ros/humble/setup.bash
ros2 topic list
ros2 topic echo /joint_states --once
ros2 run tf2_ros tf2_echo world <end_effector_frame>
```

Confirm the Isaac Sim ROS 2 bridge publishes joint states and transforms at a stable rate before planning. If MoveIt cannot see the robot state, debug ROS 2 bridge and TF first.

## cuMotion/cuRobo Checks

For cuMotion/cuRobo-style workflows:

- Verify the robot configuration matches the simulated articulation joint names and limits.
- Warm up the planner where required before measuring behavior.
- Refresh obstacles after scene changes.
- Confirm planned trajectories are retimed or sampled for the simulated controller.
- Save planner status and collision result separately from execution result.

## Evidence to Save

- Raw AI goal and validated planner goal.
- Frame conversion used.
- Planner config and selected planning group.
- Planning status, solve time, path length, and final pose error.
- Collision-world source and obstacle count when available.
- Executed trajectory duration and measured final joint/pose error.
- Screenshot or viewport capture for target reach, grasp, or obstacle-clearance tasks.
