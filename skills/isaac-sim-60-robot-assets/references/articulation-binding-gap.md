# Visual/Rigid USD Without Articulation

## Official docs checked
- Robot setup: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/index.html
- Rig a mobile robot: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/rig_mobile_robot.html
- Basic robot tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/introduction/quickstart_isaacsim_robot.html
- OmniGraph articulation controller: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_tutorial.html
- Asset validation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_validation.html

## Classification
If USD inspection shows meshes and rigid bodies but no physics joints and no articulation roots, classify it as:

```text
visual/rigid-body USD, not a controllable articulation
```

This is a valid asset state, but it is not ready for Articulation Controller, joint-state sensors, ROS joint publishing, or LeRobot command binding.

## Evidence fields
Record:
- source USD path and conversion path
- mesh count
- rigid body count
- physics joint count
- articulation root count
- candidate logical links
- expected control joints or 13D contract fields
- whether the result is `binding_pending`

## What is missing
A controllable robot needs:
1. link hierarchy or logical rigid bodies
2. physics joints between parent/child bodies
3. limits and axes on each joint
4. drive APIs or actuator setup where control is needed
5. one articulation root above the jointed hierarchy
6. stable joint names for controller, ROS, and LeRobot binding

## Do not do
- Do not tune gains before joints exist.
- Do not wire ROS or LeRobot commands to a stand-in if the real USD has no articulation.
- Do not treat visual validation as proof of controllability.
- Do not add an articulation root alone and call the asset bound; joints and drives are still required.

## Handoff
- Stay in `$isaac-sim-60-robot-assets` to classify the converted USD and map source/candidate links.
- Move to `$isaac-sim-60-articulation-builder` to generate an explicit joint map and author a non-destructive articulation scaffold.
- Move to `$isaac-sim-robot-setup-tuning` after joints/articulation root exist and the problem becomes stability, gains, colliders, mass, or gripper behavior.
- Move to `$isaac-sim-60-ros2-sitl` only after joint names and command order are real.
