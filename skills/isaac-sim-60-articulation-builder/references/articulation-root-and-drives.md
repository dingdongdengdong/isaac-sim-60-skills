# Articulation Root and Drives

## Official docs checked
- Articulation Controller: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_simulation/articulation_controller.html
- OmniGraph Articulation Controller tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_tutorial.html
- Joint drive tuning: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup_tutorials/joint_tuning.html
- Gain Tuner: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/ext_isaacsim_robot_setup_gain_tuner.html

## Root placement
Apply the articulation root above the jointed hierarchy, usually the robot root or stable assembly root. Do not add a root to a random mesh prim and call the robot controllable.

## Drive policy
A scaffold may author basic drive APIs, but drive values are placeholders until tuning. Record every authored stiffness, damping, and max force value so `$isaac-sim-robot-setup-tuning` can replace them with evidence-backed values.

## Controller readiness
The asset is not ready for Articulation Controller until:
- an articulation root exists
- physics joints exist under the root
- intended actuated joints have drives or a clear actuator policy
- joint names are stable and inspectable
- a one-joint command or equivalent smoke test can be run

## 5.1-to-6.0 migration notes
Older projects may contain `omni.isaac.*` imports or extension names. For 6.0-focused work, treat those as migration context and prefer current `isaacsim.*` surfaces where applicable. Migrate API/extension names before debugging the articulation scaffold.
