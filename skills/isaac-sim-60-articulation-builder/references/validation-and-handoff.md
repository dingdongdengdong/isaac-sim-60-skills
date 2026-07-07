# Validation and Handoff

## Inspection evidence
Keep these artifacts:
- source inspection JSON
- articulation mapping JSON
- scaffold output USD path
- scaffold report JSON
- output inspection JSON
- screenshot paths when visual review matters

## Acceptance gates
Before handoff, verify:
- `valid_physics_joints` count is greater than zero
- `invalid_joint_relationships` count is zero
- articulation root count is greater than zero
- intended actuated joints have drive APIs on movable joint prims or a documented no-drive policy
- `stray_drives` are explained or removed
- source USD was not modified in place
- skipped disabled mapping entries are explained, and `failed_enabled_joints` is empty

## Handoff to tuning
Hand off to `$isaac-sim-robot-setup-tuning` when the scaffold exists and the next problem is drive gains, damping, force limits, colliders, mass, inertia, contact stability, closed loops, or gripper behavior.

## Handoff to ROS/LeRobot
Hand off to `$isaac-sim-60-ros2-sitl` only after the final joint names and order are real. Include the output inspection JSON and the joint list expected by the control contract.

## Handoff to viewport evidence
Use `$isaac-sim-viewport-debugger` to capture the source asset, candidate links, scaffolded robot root, and before/after views. Treat screenshots as visual evidence only, not proof of physics control.
