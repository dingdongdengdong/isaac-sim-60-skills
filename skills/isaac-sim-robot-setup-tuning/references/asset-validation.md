# Asset Validation

## Official docs
- Robot setup: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/index.html
- Asset validation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_validation.html
- Asset Transformer tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_transformer_tutorials.html
- Asset Structure: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_structure.html
- OpenUSD tuning tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/openusd_tuning_tutorials/index.html
- Newton physics backend: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/physics/newton_physics.html

## Validation checklist
Record:
- source asset path and edited output layer/path
- articulation root path
- intended physics backend: PhysX, Newton, or both
- link and joint count
- collider presence and approximation
- mass/inertia presence
- drive gain presence and force limits
- mimic/closed-loop/gripper relationships
- validation, inspector, or script output

## Layer policy
Use a separate output layer or diagnostics copy for tuning. Do not overwrite imported, CAD, vendor, or SimReady source files without explicit user approval.

## Asset Structure and backend notes
For Isaac Sim 6.0 robot assets, prefer a structure that separates geometry, materials, collision meshes, metadata, and physics-specific layers. This makes PhysX/Newton/MuJoCo variants easier to inspect and tune.

## 5.1-to-6.0 migration notes
- Replace removed `omni.isaac.*` compatibility names before tuning scripts.
- Check for deprecated Robot Wizard workflows and prefer current Robot Inspector/Poser/Asset Transformer tooling.
- If an imported asset gained Newton schemas in 6.0, record whether the validation was run against PhysX or Newton.
