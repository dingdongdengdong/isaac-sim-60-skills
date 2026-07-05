# Scene and Robot Scripting

## Official docs
- Scene setup snippets: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/index.html
- Core API tutorial series: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/core_api_tutorials/index.html
- Robot simulation snippets: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/index.html

## Stage work

Prefer explicit paths:
- source USD path
- target prim path
- output layer or diagnostics path

When opening large stages, wait for loading and capture the exact stage identifier. Do not modify a source USD unless the user requested persistent edits.

## Robot work

Before controlling a robot:
1. Confirm the articulation root.
2. Confirm joint names and count.
3. Confirm controller API or graph path.
4. Capture initial state.
5. Apply one command and verify the resulting state.

Use `$isaac-sim-60-robot-assets` for import/mapping and `$isaac-sim-robot-setup-tuning` for drive/collider/physics edits.
