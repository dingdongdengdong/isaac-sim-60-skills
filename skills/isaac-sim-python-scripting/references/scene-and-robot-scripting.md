# Scene and Robot Scripting

## Official docs
- Scene setup snippets: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/index.html
- Core API tutorial series: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/core_api_tutorials/index.html
- Robot simulation snippets: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/index.html
- Application Template: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/app_template/index.html

## Stage work
Prefer explicit paths:
- source USD path
- target prim path
- output layer or diagnostics path
- loaded payloads or asset dependencies
- units/up-axis assumptions

When opening large stages, wait for loading and capture the exact stage identifier. Do not modify a source USD unless the user requested persistent edits.

## Robot work
Before controlling a robot:
1. Confirm the articulation root.
2. Confirm joint names and count.
3. Confirm controller API or graph path.
4. Capture initial state.
5. Apply one command and verify the resulting state.

Use `$isaac-sim-60-robot-assets` for import/mapping and `$isaac-sim-robot-setup-tuning` for drive/collider/physics edits.

## Sensor or SDG work
When scripts create sensors, Replicator writers, MobilityGen runs, or teleop episodes, hand off to `$isaac-sim-60-sensors-sdg` for timing, output metadata, and writer/recorder verification.
