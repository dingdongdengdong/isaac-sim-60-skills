# Isaac Sim 6.0 Sensors and SDG Reference

## Official docs checked
- Release notes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html
- Sensors overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/index.html
- Camera sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_camera.html
- RTX Lidar ROS tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_rtx_lidar.html
- RTX sensor migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_rtx_to_experimental_rtx.html
- RTX sensor annotators: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_rtx_annotators.html
- Replicator troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/troubleshooting.html

## 6.0 sensor notes
- Cameras are USD `Camera` prims rendered by the RTX renderer.
- RTX Lidar/Radar APIs moved toward `isaacsim.sensors.experimental.rtx`; avoid stale `isaacsim.sensors.rtx` assumptions when writing 6.0 code.
- RTX Lidar needs its own viewport to simulate properly.
- Release notes highlight multitick rendering: cameras and RTX Lidars can be scheduled by simulation time.
- In 6.0 GA, RTX Radar has a known tick-rate caveat: verify behavior empirically when exact Radar cadence matters.

## Capture triage
- No data captured: check capture-on-play, render product attachment, writer initialization, output directory permissions, and whether simulation actually advanced.
- Rendering artifacts: increase subframes where appropriate, wait for materials/assets to load, and verify lighting.
- ROS sensor output missing: confirm ROS 2 bridge extension, domain ID, graph node migration, and topic names.

## Workspace dataset context
- LeRobot episode recording should preserve the 13D state/action metadata unless the user asks for a new dataset schema.
- When adding cameras or sensors to the SimReady `echo_full` scene, store evidence under `isaacsim_test/artifacts/` and avoid committing generated datasets unless requested.
