# Closed Loops and Grippers

## Official docs
- Rig closed-loop structures: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/rig_closed_loop_structures.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html
- Grasp Editor: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_simulation/index.html
- Surface Gripper: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_simulation/ext_isaacsim_robot_surface_gripper.html
- Surface Gripper extension: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_simulation/ext_isaacsim_robot_surface_gripper.html

## Closed-loop policy
Closed-loop kinematic structures require extra care. Inspect:
- which chain is broken for articulation compatibility
- constraints used to represent the loop
- mimic joints and ratios
- drive settings on all loop joints
- solver settings and convergence symptoms

If the loop is unstable, consider separate articulations with constraints rather than one complex closed-loop articulation.

## Gripper checks
For grippers and dexterous hands:
1. Capture open and closed baseline poses.
2. Test without contact first.
3. Test contact against one simple object.
4. Confirm mimic joints, axes, limits, drive gains, and force limits.
5. Inspect collider shapes separate from visuals.
6. If using Surface Gripper code from 5.1, apply the 6.0 binding migration before tuning physics.

For this user's SuperArm/AmazingHand context, coordinate with `$isaac-sim-60-robot-assets` before changing the established hand asset policy.
