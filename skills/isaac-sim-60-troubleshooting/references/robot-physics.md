# Robot Physics Troubleshooting

## First split
Decide whether the symptom is visual composition, articulation/control binding, physics tuning, backend mismatch, ROS command contract, or sensor attachment.

## Joints do not move
Check articulation root, joint names, drive mode, gains, force limits, controller target units, graph/control execution, and ROS command order.

## Robot collapses, explodes, or jitters
Check missing/weak gains, collider overlap, invalid mass/inertia, bad joint parent/child paths, closed-loop constraints, solver settings, and backend-specific actuator behavior.

## Link detaches or jumps
Check USD composition, payloads, xform ops, joint body paths, visual-vs-physics prim mismatch, and imported coordinate conversion.

## Gripper or hand drops objects
Check contact colliders, finger mimic joints, gain/force limits, contact offsets, Surface Gripper migration, and whether testing starts with one simple object.

## Verification
Run the smallest reproduction: one-joint command, gravity hold, step response, open/close gripper test, or collision pair check. Save before/after properties and visual evidence when useful.
