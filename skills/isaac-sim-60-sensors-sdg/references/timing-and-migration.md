# Timing and Migration

## Official docs checked
- Multi-tick rendering: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_multitick_rendering.html
- Camera migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_camera_to_experimental_rtx.html
- RTX migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html
- Physics sensor migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_physics_to_experimental_physics.html
- PhysX Lidar migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_physx_lidar_to_physics_raycast.html
- Replicator Agent migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/ext_isaacsim_replicator_agent_migration_guide.html

## Timing terms
Keep these separate in reports: simulation timestep, render frame, sensor tick rate, Lidar/radar scan accumulation window, Replicator orchestrator step, ROS publish rate/clock, and teleoperation episode index.

## Camera timing
After camera creation or movement, wait for render initialization and at least one new rendered frame before reading buffers or files.

## Lidar/Radar timing
Record tick rate, scan rate, accumulation policy, and whether output is per tick, per completed scan, or per render frame.

## Replicator timing
A saved frame requires scene update, randomization trigger, render product, annotator, writer, and flush/close path to all run. Preserve the explicit step count used for evidence.

## Migration rules
- Replace removed `omni.isaac.*` shims before debugging sensor logic.
- Treat `isaacsim.sensors.camera`, `isaacsim.sensors.rtx`, `isaacsim.sensors.physics`, and `isaacsim.sensors.physx` as old/import-migration paths when 6.0 docs point to experimental replacements.
- Replace deprecated `frameSkipCount` style assumptions with explicit tick/render/orchestrator policy.
- For each migrated script, save a minimal before/after output comparison: one frame, one scan, or one sensor sample.
