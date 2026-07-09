# AI Navigation Control Reference

## Official Docs Checked
- ROS 2 navigation tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_navigation.html
- ROS 2 bridge tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_landing_page.html
- ROS 2 transform tree tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_tf.html
- ROS 2 bridge Python workflows: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_python.html

## Required Contract

Record these before connecting an AI goal generator:

- Robot asset and base/articulation prim path.
- Frames: `map`, `odom`, robot base frame, sensor frames, and Isaac Sim world frame.
- TF publisher source and rate.
- Odometry source and covariance assumptions.
- Map source, resolution, origin, and update policy.
- Sensor topics used by localization or obstacle layers.
- Command topic, usually velocity command or Nav2 action goal.
- Goal format and frame.

## Bring-Up Sequence

1. Start Isaac Sim and ROS 2 bridge.
2. Confirm ROS_DOMAIN_ID and topic visibility.
3. Verify `/tf`, odometry, sensor topics, and map availability.
4. Confirm localization is stable while the robot is stationary.
5. Send one small manual goal in an open area.
6. Check global plan, local plan, controller status, and final pose.
7. Only then connect AI-generated goals.

## Useful ROS 2 Checks

```bash
export ROS_DOMAIN_ID=42
source /opt/ros/humble/setup.bash
ros2 topic list
ros2 topic hz /tf
ros2 topic echo /odom --once
ros2 run tf2_ros tf2_echo map base_link
```

Adapt frame and topic names to the actual robot. If TF or odometry is missing, fix bridge/graph configuration before changing Nav2 or AI code.

## AI Goal Validation

For every AI-generated navigation target:

- Convert into the expected frame explicitly.
- Clamp to the allowed workspace.
- Reject goals inside obstacles, outside the map, or too close to restricted zones.
- Limit goal update rate to avoid thrashing the planner.
- Log raw AI output, validated goal, and rejection reason if rejected.

For multi-robot cases, include robot ID, namespace, TF prefix, and collision/traffic assumptions.

## Evidence to Save

- Map and robot initial pose.
- Raw AI target and validated Nav2 goal.
- TF/odometry status.
- Global path and local controller status when available.
- Final pose and final pose error.
- Timeout, collision, recovery, or stuck status.
- Screenshot or viewport capture showing robot, goal, and relevant obstacles.
