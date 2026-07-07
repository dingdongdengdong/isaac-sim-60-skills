# Drive Gains

## Official docs
- Tutorial 11: Tuning Joint Drive Gains: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/joint_tuning.html
- Gain Tuner Extension: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/ext_isaacsim_robot_setup_gain_tuner.html
- OpenUSD joint drive tuning: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/openusd_tuning_tutorials/tutorial_05_joint_drive_tuning.html
- OpenUSD joint gains tuning: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/openusd_tuning_tutorials/tutorial_06_joint_gains_tuning.html
- Newton actuators: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/newton_actuators_tutorials/index.html

## Tuning loop
1. Capture baseline gains for every actuated joint.
2. Confirm backend, mode, stiffness, damping, force limit, and target units.
3. Test one joint or one coupled group first.
4. Use snap-to-limits, step response, sine response, or gravity hold depending on the issue.
5. Increase stiffness to reach target authority.
6. Increase damping to reduce overshoot and oscillation.
7. Record pass/fail, settling time, overshoot, steady-state error, and changed properties.

## Symptoms
- Collapses under gravity: gains may be zero or too weak, or mass/inertia is wrong.
- Oscillates: damping too low, timestep/solver settings poor, backend mismatch, or mass distribution unstable.
- Slow response: stiffness too low, damping too high, force limit too low, or controller target wrong.
- Cannot reach limits: collider interference, wrong joint limits, wrong axis, or blocked motion.

## Report fields
Include joint name, joint path, backend, mode, stiffness, damping, force limit, target, response result, and any property changed.
