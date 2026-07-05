# Isaac Sim 6.0 Robot Asset Reference

## Official docs checked
- URDF importer: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/importer_exporter/ext_isaacsim_asset_importer_urdf.html
- MJCF importer: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/importer_exporter/ext_isaacsim_asset_importer_mjcf.html
- Manipulator setup/import: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html
- Newton physics backend: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/physics/newton_physics.html

## 6.0 robot notes
- Release notes say URDF and MJCF importers can import multi-physics assets and include robot/base type selection options.
- MJCF import is relevant for MuJoCo-format robots, but closed-loop/equality-constraint hands can still need custom decomposition.
- Newton support is available as an experimental physics backend; default workspace SITL should not switch physics backend without explicit intent and new validation.

## Workspace source of truth
- Local guide: `isaacsim_test/README.md`.
- Sim loop plan: `integration_guide/09_isaacsim_sim_loop_plan.md`.
- AmazingHand memory: `omx_wiki/amazinghand-isaacsim.md`.
- Final SimReady USD: `isaacsim_test/outputs/simready/echo_full/pipeline/04_conform/repair-loop-02-fet005/fet005-grasp/echo_full_robot_arm_hand.usd`.
- SimReady validation: `isaacsim_test/outputs/simready/echo_full/pipeline/06_validation_final/simready-profile.json`.
- Mapping evidence: `isaacsim_test/artifacts/simready_prim_mapping.json`.

## AmazingHand policy
- Do not use the original AmazingHand MJCF as the runtime physics articulation without new validation.
- Stable current model: simplified two-link-per-finger tree articulation for physics, primitive collision proxies, and static MJCF visual shell.
- Actuated hand joints are `finger1_motor1` through `finger4_motor2`.
- If animated STL finger visuals are requested, plan a visual follower or tree-compatible decomposition; do not partition closed-loop visuals casually.

## Robot setup triage
- Meshes penetrate: inspect source transforms and imported USD transforms.
- Joints do not move: check limits, nonzero gains, mimic ratios/directions, and isolate one joint at a time.
- Wrong direction: compare source joint axes against USD joint axes and command sign conventions.
