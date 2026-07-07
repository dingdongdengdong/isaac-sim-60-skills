# RTX, Physics, and PhysX Sensors

## Official docs checked
- RTX Lidar: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_lidar.html
- RTX Radar: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_radar.html
- RTX Acoustic: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_acoustic.html
- RTX annotators: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_annotators.html
- RTX non-visual materials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_materials.html
- Multi-tick rendering: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_multitick_rendering.html
- Physics-based sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_physics.html
- PhysX SDK sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_physx.html
- RTX migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html

## API choice
- New RTX authoring/runtime work: prefer `isaacsim.sensors.experimental.rtx` and record sensor class, profile/config, prim path, and tick/render policy.
- Existing `isaacsim.sensors.rtx` or `isaacsim.sensors.camera` code: treat as migration work and preserve before/after output shape.
- ROS point clouds/images: separate sensor output validation from ROS transport validation.
- Physics/PhysX sensors: confirm whether the task needs high-level physics sensors, PhysX SDK sensors, or a ROS/OmniGraph bridge.

## Lidar workflow
Record sensor prim path, parent frame, profile/config path, tick rate, scan rate, horizontal/vertical resolution, accumulation policy, annotator or GenericModelOutput path, point-cloud coordinate frame/units, and output artifact or ROS topic.

## Radar and acoustic workflow
Record sensor prim path/orientation, material or non-visual material assumptions, Motion BVH or Doppler/motion settings when applicable, GenericModelOutput/annotator output, and debug draw or tiny sample output.

## Physics and PhysX sensor routing
- Articulation joint/contact/effort/IMU/joint-state sensors usually belong with robot validation and may hand off to `$isaac-sim-robot-setup-tuning`.
- Raycast, PhysX generic, PhysX lidar, lightbeam, and proximity sensors need exact official API lookup before implementation because profiles and bindings are more specialized.
- Preserve backend assumption: PhysX versus Newton can affect what physics data is available or validated.

## Annotators and debug draw
Do not declare a sensor missing until you check sensor prim initialization, render/simulation steps, annotator attachment, debug draw, and output after at least one valid sensor tick.

## Migration notes
- 5.1 added RTX non-visual material support and changed some RTX point-cloud extraction behavior; 6.0 continues migration toward experimental RTX APIs.
- Record old import path, new import path, old output fields, and new output fields when migrating 5.1 scripts.
- Re-run a tiny scene with one object before trusting a migrated full-scene sensor dataset.
