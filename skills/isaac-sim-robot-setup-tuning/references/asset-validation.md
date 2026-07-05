# Asset Validation

## Official docs
- Robot setup: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/index.html
- Asset validation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_validation.html
- Asset Transformer tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_transformer_tutorials.html
- OpenUSD tuning tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/openusd_tuning_tutorials/index.html

## Validation checklist

Record:
- source asset path
- edited output layer/path
- articulation root path
- physics backend target
- link and joint count
- collider presence
- mass/inertia presence
- drive gain presence
- validation tool output

## Layer policy

Use a separate output layer or diagnostics copy for tuning. Do not overwrite imported, CAD, vendor, or SimReady source files without explicit user approval.

## Asset Structure 3.0

For Isaac Sim 6.0 robot assets, prefer a structure that separates geometry, materials, collision meshes, metadata, and physics-specific layers. This makes PhysX/Newton/MuJoCo variants easier to inspect and tune.
