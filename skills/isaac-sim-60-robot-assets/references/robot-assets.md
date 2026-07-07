# Isaac Sim 6.0 Robot Asset Reference

## Official docs checked
- URDF importer: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/importer_exporter/ext_isaacsim_asset_importer_urdf.html
- MJCF importer: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/importer_exporter/ext_isaacsim_asset_importer_mjcf.html
- Importer/exporter tutorials: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/importer_exporter/importer_exporter_tutorials.html
- Asset Structure: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_structure.html
- Robot assets: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/assets/usd_assets_robots.html
- Robot setup: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/index.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html
- Newton physics backend: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/physics/newton_physics.html
- Surface Gripper extension: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_simulation/ext_isaacsim_robot_surface_gripper.html

## Asset intake workflow
1. Classify the source: SimReady/OpenUSD, imported URDF, imported MJCF, CAD-converted USD, third-party USD, or generated diagnostics copy.
2. Record source path, target prim path, output layer, units, up axis, articulation root, link/joint counts, and whether payloads are loaded.
3. For importers, save importer settings and generated USD path. Do not edit vendor/import source assets destructively.
4. Confirm link visuals, colliders, joints, drives, limits, mimic joints, and actuator/control names before binding ROS or LeRobot topics.
5. If the asset loads but physics fails, stop asset work and hand off to `$isaac-sim-robot-setup-tuning` with the collected prim paths.

## 6.0 robot notes
- Newton support is available as an experimental physics backend; default workspace SITL should not switch physics backend without explicit intent and new validation.
- URDF and MJCF importers may author backend-specific schemas; record whether an asset is intended for PhysX, Newton, or both.
- SimReady content and Asset Structure guidance matter for reusable assets: separate geometry, materials, collisions, metadata, and physics/tuning layers.
- Robot Wizard is deprecated in current 6.0 docs; prefer Robot Inspector, Robot Poser, Asset Transformer, and explicit setup/tutorial workflows.

## 5.1-to-6.0 migration notes
- 5.1 warned deprecated extensions would be removed in 6.0; check old assets/scripts for `omni.isaac.*` extension names.
- If a 5.1 project used Surface Gripper Python bindings, follow the 6.0 Surface Gripper migration before editing grasp logic.
- If a 5.1 asset used older sensor, robot, or motion-generation extension names, migrate the extension/API name first, then retest import.

## Non-articulated conversion result
If inspection reports meshes and rigid bodies but `0` physics joints and `0` articulation roots, the converted USD is only a visual/rigid-body asset. Record it as `binding_pending` and read `articulation-binding-gap.md` before attempting controllers, ROS joint state, or LeRobot binding.

## Workspace source of truth
- Primary SimReady asset: `isaacsim_test/outputs/simready/echo_full/pipeline/04_conform/repair-loop-02-fet005/fet005-grasp/echo_full_robot_arm_hand.usd`.
- Mapping artifact: `isaacsim_test/artifacts/simready_prim_mapping.json`.
- Do not silently replace the real asset with a hidden stand-in articulation. If binding is not complete, report `binding_pending`.

## AmazingHand policy
- Stable default: static MJCF visual shell plus a simplified Isaac-oriented collision/physics tree.
- Before changing hand physics, capture hand root prim, wrist attachment, finger links/joints, mimic relationships, collider approximation, drive gains, and one visual screenshot.
- Coordinate with `$isaac-sim-60-ros2-sitl` before changing joint order or the 13D LeRobot feature contract.

## Robot setup triage
- Visual import issue: stay here and inspect USD composition, payloads, prim paths, scales, and materials.
- Articulation/control issue: collect joint/link paths and hand off to `$isaac-sim-robot-setup-tuning` or `$isaac-sim-omnigraph-builder`.
- ROS topic issue: hand off to `$isaac-sim-60-ros2-sitl`.
- Runtime, missing asset server, or cache issue: hand off to `$isaac-sim-60-runtime` or `$isaac-sim-60-troubleshooting`.
