# Post-SimReady Controllability Pipeline

## Official docs checked
- Robot setup: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/index.html
- Rig a mobile robot: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/rig_mobile_robot.html
- Import and assemble a manipulator: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html
- Basic robot quickstart: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/introduction/quickstart_isaacsim_robot.html
- Asset validation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_validation.html

## Status meanings
- `visual_only`: meshes exist, but no rigid bodies, physics joints, or articulation root are detected.
- `rigid_body_not_articulated`: rigid bodies exist, but physics joints and articulation root are missing.
- `invalid_articulation_relationships`: one or more joints have missing or non-rigid body targets; this is not controllable.
- `partial_articulation_missing_root`: valid physics joints exist, but no articulation root is detected.
- `partial_articulation_missing_joints`: an articulation root exists, but no valid physics joints are detected.
- `articulated_no_drives`: valid joints and root exist, but no drive APIs are detected on valid movable joint prims.
- `controllable_candidate`: valid joints, articulation root, and at least one drive on a valid movable joint are detected; ready for tuning/verification.

## Pipeline
1. Inspect the source USD and record counts.
2. If status is not `controllable_candidate`, create an articulation mapping template.
3. Confirm the mapping manually or from a trusted robot spec. CAD geometry alone is not enough to infer joint semantics.
4. Author a scaffold into a separate output USD/layer.
5. Re-inspect output and preserve both inspection JSON files.
6. Move to tuning only after the root exists, joint body targets resolve to rigid bodies, and intended drives are attached to movable joints.

## Mapping source options
- Mechanical design spec, CAD assembly metadata, or existing URDF/MJCF.
- A known robot joint contract such as this workspace's 13D LeRobot order.
- Manual link inspection with screenshots and prim paths.

## Failure policy
If there is no explicit parent/child joint mapping, stop after template generation. Do not invent revolute/prismatic joints from mesh positions.
