# Action/Event, MobilityGen, and Teleoperation SDG

## Official docs checked
- Action and Event Data Generation index: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/action_and_event_data_generation/index.html
- Actor Simulation and SDG: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/action_and_event_data_generation/tutorial_replicator_agent.html
- Behavior Tree Generation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/action_and_event_data_generation/tutorial_behavior_tree_gen.html
- Object Simulation and SDG: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/action_and_event_data_generation/tutorial_replicator_object.html
- MobilityGen: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/synthetic_data_generation/tutorial_replicator_mobility_gen.html
- MobilityGen migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/mobility_gen_recordings_migration.html
- Teleoperation SDG: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/synthetic_data_generation/tutorial_replicator_teleop_sdg.html

## Choose the SDG family
- Perception Replicator dataset: use `replicator-sdg.md`.
- Actor/object/event scenario: use Action/Event SDG and record config files, behavior tree JSON, writer, trigger, and scenario seed.
- Mobile-robot data collection: use MobilityGen and record robot config, route/map/world, sensors, and episode metadata.
- Demonstration collection: use Teleoperation SDG and record teleop device/source, action/state mapping, camera streams, and episode boundaries.

## Practical workflow
1. Define the dataset product: frames/labels, event timeline, mobile robot trajectory, or teleoperation episode.
2. Record the controlling extension/API, config file path, world/stage path, robot prim, sensor prims, writer/output directory, and random seed.
3. Decide whether the run is scripted, GUI-driven, ROS-driven, or teleop-driven.
4. Keep simulation time, render time, and episode index distinct in metadata.
5. Flush or close writers/recorders before inspecting output files.
6. Save one minimal replay or verification command when the workflow supports replay.

## 6.0 feature notes
- 6.0 release notes add behavior-tree based actor control, AI-assisted behavior tree generation, object/event workflows, MobilityGen, and teleoperation data collection surfaces.
- MobilityGen moved toward `isaacsim.replicator.experimental.mobility_gen`; treat older `isaacsim.replicator.mobility_gen` imports as migration-only.
- Teleoperation episodes must not silently alter this workspace's 13D LeRobot state/action contract.

## Failure checks
- Empty output: recorder/writer not flushed, no render/sim steps, wrong output path, or trigger never fired.
- Misaligned state/action/video: inconsistent clock source, dropped frames, or recorder started after teleop commands.
- Scenario repeats unexpectedly: seed/config not recorded or randomization not triggered.
- Behavior tree does nothing: behavior tree JSON invalid, actor controller not attached, or simulation not playing.
