# Robot Setup Tuning Troubleshooting

## Robot collapses
Check zero/weak drive gains, missing articulation root, wrong drive mode, bad mass/inertia scale, gravity direction, missing physics scene, or backend-specific actuator differences.

## Robot explodes or jitters
Check overlapping colliders, bad mass ratios, invalid inertia, excessive stiffness, missing damping, solver settings, closed-loop constraints, and contact offsets.

## Joint moves wrong direction
Check joint axis, local joint frames, importer coordinate conversion, mimic ratio sign, command sign convention, and ROS/LeRobot joint order.

## Link detaches or jumps to origin
Check joint parent/child body paths, transform reset or missing xform op, payload/layer composition, articulation hierarchy, and whether the visual link and physics link are different prims.

## Backend mismatch
If behavior changes between PhysX and Newton, record backend, authored schemas, solver settings, actuator model, and whether the feature is documented as supported for that backend.

## Evidence before edits
Before changing values, capture current prim paths and properties. After changing values, rerun the smallest test that demonstrated the failure.

## Gripper cannot hold object
Check finger collider shape, contact offsets, solver iterations, drive force limits, mimic ratios, Surface Gripper migration, and whether the object has mass/collider/material properties suitable for contact.

## Acceptance evidence
A tuning change is accepted only after rerunning the smallest failing scenario and recording before/after values. Prefer one-joint, one-contact, or one-gripper tests before a full task demo.
