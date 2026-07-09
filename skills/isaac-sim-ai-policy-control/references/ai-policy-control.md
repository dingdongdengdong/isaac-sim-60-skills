# AI Policy Control Reference

## Official Docs Checked
- Isaac Lab policy deployment: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/isaac_lab_tutorials/tutorial_policy_deployment.html
- ROS 2 RL controller: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_rl_controller.html
- ROS 2 manipulation and joint control: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_manipulation.html
- ROS 2 bridge Python workflows: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_python.html
- Motion generation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/motion_generation/index.html
- MoveIt 2 integration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_moveit.html
- cuRobo/cuMotion manipulation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/manipulators/manipulators_curobo.html

## Control Surface Choices

Choose one primary path before coding:

| Path | Use when | Main checks |
| --- | --- | --- |
| Isaac Lab policy deployment | A trained RL policy and Isaac Lab env/config already exist | env config, policy checkpoint/export, obs/action terms, device, reset |
| Direct Python control | A custom model should run inside an Isaac Sim script | `SimulationApp`, physics stepping, articulation handles, bounded actions |
| ROS 2 policy node | Policy runs outside Isaac Sim or inside a ROS container | topic names, QoS, ROS_DOMAIN_ID, message type, control rate |
| OmniGraph/Action Graph | Existing scene uses graph-based controllers or ROS bridge nodes | graph execution, tick source, node attributes, ROS node migration |
| Motion planner control | AI selects goals and planner computes motion | collision world, IK/trajectory status, joint limits, controller tracking |
| Teleop/imitation loop | Human demonstrations feed policy evaluation or training | episode format, action timestamps, observation sync, replay fidelity |

## Minimum Contract

Record these before changing behavior:

- Robot USD or stage path and articulation prim path.
- Joint names and command order.
- Command type: position, velocity, effort, target pose, twist, gripper command, or navigation goal.
- Units and scales: radians vs degrees, meters, normalized `[-1, 1]`, raw joint targets, delta actions.
- Observation fields: joint position/velocity, base pose, camera tensors, contact state, task state, previous action.
- Policy frequency and physics timestep.
- Reset behavior and randomization state.
- Action bounds and emergency stop behavior.

For this workspace, do not break the existing 13D ROS/LeRobot command contract unless the user explicitly requests a new interface.

## Safe Rollout Sequence

1. Load and stabilize the robot with no policy.
2. Apply zero, hold, or home command for 100-300 simulation frames.
3. Apply one bounded nonzero command to one joint or one goal.
4. Connect the policy adapter but run one inference step only.
5. Run a short rollout with action logging and visual capture.
6. Reset and replay the same seed or command trace.
7. Increase rollout length only after the short rollout is stable.

Stop and hand off to `$isaac-sim-robot-setup-tuning` if the robot collapses, jitters, explodes, ignores limits, detaches, or cannot hold zero command.

## Policy Adapter Pattern

Keep adapters thin and testable:

```python
obs = read_sim_observation()
model_input = encode_observation(obs, config)
raw_action = policy(model_input)
action = decode_and_clip_action(raw_action, config)
apply_action(action)
log_step(obs, raw_action, action)
```

Do not hide unit conversion inside the model call. Keep normalization, clipping, joint-order mapping, and topic serialization as named steps.

## ROS 2 Loop Checks

For policy nodes that command through ROS 2:

```bash
export ROS_DOMAIN_ID=42
source /opt/ros/humble/setup.bash
ros2 topic list
ros2 topic hz /follower/joint_states
ros2 topic echo /follower/joint_states --once
ros2 topic pub /leader/joint_commands std_msgs/msg/Float64MultiArray \
  "data: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]" --once
```

Then run the policy with a low action scale first. Confirm that published actions match the expected length, joint order, units, and rate.

## Isaac Lab Deployment Checks

For Isaac Lab policy deployment:

- Identify the task/env name, checkpoint/export path, and config files.
- Confirm the deployed robot and training robot use compatible joint names, limits, and observation terms.
- Confirm observations are in the order and units expected by the policy.
- Run deterministic reset and short rollout before task evaluation.
- Log reward/task metrics separately from physical stability metrics.

If a policy worked in Isaac Lab but fails in a custom Isaac Sim scene, first compare robot asset, articulation root, joint naming, drive properties, timestep, and action scale.

## Motion Planning and AI Goals

When an AI model chooses object poses, grasp targets, navigation goals, or manipulation goals, separate goal generation from motion execution:

1. Validate the generated goal in task coordinates.
2. Run IK or trajectory planning with collision world enabled.
3. Check planner status before applying any trajectory.
4. Execute with a bounded controller.
5. Compare commanded vs measured joint states.

Planner success is not execution success. Save both planner status and simulated robot evidence.

## Evidence to Save

Minimum useful evidence:

- Policy/model path and checksum when practical.
- Config files or key parameters.
- Command topics or direct-control API used.
- Joint order and action bounds.
- One zero/hold test result.
- One short rollout result with elapsed sim time and frame count.
- Screenshot or camera/viewport capture when behavior is spatial, visual, or contact-based.
- Failure symptoms with the first bad timestamp/frame.
