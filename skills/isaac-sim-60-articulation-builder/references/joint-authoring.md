# Joint Authoring

## Official docs checked
- Rig a mobile robot: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/rig_mobile_robot.html
- Rig closed-loop structures: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/rig_closed_loop_structures.html
- Physics fundamentals: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/physics/index.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html

## Mapping fields
Each authored joint must have:
- stable joint name or explicit joint prim path
- joint type: `revolute`, `prismatic`, `fixed`, or `spherical`
- parent/body0 prim path that exists on the composed stage and has `RigidBodyAPI`
- child/body1 prim path that exists on the composed stage and has `RigidBodyAPI`
- axis for revolute/prismatic joints: `X`, `Y`, or `Z`
- optional lower/upper limits in the units expected by the target joint type
- optional drive block with drive type, stiffness, damping, and max force; drives are accepted only for revolute (`angular`) and prismatic (`linear`) scaffold joints

## Rules
- Use fixed joints for rigid attachments that should move as one body.
- Use revolute joints for hinge-like rotational degrees of freedom.
- Use prismatic joints for linear slides.
- Use spherical joints only when the downstream controller and tuning plan can handle multi-axis motion; this scaffold does not attach drives to spherical joints.
- Keep joint names stable because ROS, LeRobot, logs, and tests will depend on them.

## Closed-loop caution
Closed-loop mechanisms require deliberate break/constraint strategy. Do not convert every visible CAD assembly relationship into an articulation joint without checking Isaac Sim closed-loop guidance.
