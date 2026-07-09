# Teleop Policy Data Loop Reference

## Official Docs Checked
- Isaac Sim sensors and synthetic data documentation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/index.html
- Replicator synthetic data generation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/index.html
- ROS 2 bridge tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/ros2_landing_page.html
- ROS 2 manipulation and joint control: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_manipulation.html
- Isaac Lab policy deployment: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/isaac_lab_tutorials/tutorial_policy_deployment.html

## Dataset Contract

Record these for every data collection run:

- Robot asset, articulation path, and joint order.
- Control source and command topic/API.
- Action units and bounds.
- Observation fields and sensor names.
- Camera intrinsics/extrinsics when visual policy data is recorded.
- Physics timestep, control frequency, and sensor frequency.
- Episode reset state and success/failure labels.
- Dataset schema version.

For this workspace, keep the 13D LeRobot command/state order stable unless the user explicitly requests a new schema.

## Capture Sequence

1. Start Isaac Sim and verify stable robot state.
2. Verify ROS 2 bridge or direct control path.
3. Send zero/home command and confirm measured state.
4. Record a 5-10 second smoke episode.
5. Replay the raw episode in the same scene.
6. Check command/observation alignment and final state.
7. Record longer episodes only after replay passes.

## Replay Quality Gates

A usable teleop episode should pass:

- Action length and joint order match the declared schema.
- Timestamps are monotonic and close to expected rate.
- Sensor frames line up with action/observation timestamps.
- Actions are inside limits.
- Measured state changes in the expected direction.
- Reset returns to a known state.
- Replay reaches a comparable final state or the divergence is explained.

If replay fails, fix capture timing, topic mapping, action scaling, or robot stability before collecting more data.

## Conversion to Policy Data

Before exporting to a policy-training format:

- Keep raw episodes immutable.
- Write conversion outputs to a new directory with schema version.
- Include calibration, camera, and joint metadata.
- Preserve both commanded action and measured observation.
- Document filtering rules for failed or partial episodes.
- Run one policy-loader or dataset-loader smoke test.

## Evidence to Save

- Dataset root path and schema version.
- Episode count and total duration.
- Topic/API contract.
- Sensor list and rates.
- Replay pass/fail summary.
- One visual artifact from recording and replay.
- Known gaps, such as missing tactile/contact labels or uncalibrated cameras.
