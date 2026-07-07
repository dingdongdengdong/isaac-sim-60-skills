# Isaac Sim 6.0 Sensors and SDG Index

## Official sources
- 6.0 release notes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html
- Camera sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_camera.html
- RTX sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx.html
- RTX Lidar sensor: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_lidar.html
- RTX Radar sensor: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_radar.html
- RTX Acoustic sensor: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_acoustic.html
- RTX sensor annotators: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_annotators.html
- RTX non-visual materials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_materials.html
- Physics-based sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_physics.html
- PhysX SDK sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_physx.html
- RTX sensor migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html
- Replicator overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/index.html
- Action and Event Data Generation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/action_and_event_data_generation/index.html
- MobilityGen: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/synthetic_data_generation/tutorial_replicator_mobility_gen.html
- Teleoperation SDG: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/synthetic_data_generation/tutorial_replicator_teleop_sdg.html
- Replicator troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/troubleshooting.html

## Read-order matrix
- RGB/depth/segmentation camera frames: `camera-workflows.md`, then `timing-and-migration.md`.
- RTX Lidar/Radar/Acoustic, point clouds, GenericModelOutput, non-visual materials: `rtx-lidar-radar.md`, then `timing-and-migration.md`.
- Contact, IMU, effort, joint state, raycast, PhysX generic/Lidar/lightbeam/proximity sensors: `rtx-lidar-radar.md` for routing, then official physics/PhysX sensor docs for exact API shape.
- Replicator image/annotation dataset: `replicator-sdg.md`, then `troubleshooting.md`.
- Actor/Object/Event SDG, behavior trees, MobilityGen, teleop dataset episodes: `action-event-teleop-sdg.md`, then `timing-and-migration.md`.
- ROS sensor stream: `$isaac-sim-60-ros2-sitl` plus `$isaac-sim-omnigraph-builder` after this skill chooses the sensor source.

## Scope boundaries
- Viewport screenshots are human visual evidence, not sensor data. Use `$isaac-sim-viewport-debugger`.
- ROS messages are transport/bridge behavior. Use `$isaac-sim-60-ros2-sitl` after the sensor source is known.
- Asset-mounted sensors require valid robot prim paths. Use `$isaac-sim-60-robot-assets` if paths or attachments are uncertain.
- Exact API signatures can change across 6.0.0; when coding against a new sensor family, inspect the installed docs or extension metadata.

## Workspace dataset context
- Preserve LeRobot 13D state/action order when sensor streams become teleoperation or imitation-learning episodes.
- Save camera calibration and sensor frame metadata with episodes when replay fidelity matters.
- Record timing source: simulation step, render frame, ROS clock, or recorder episode index.
