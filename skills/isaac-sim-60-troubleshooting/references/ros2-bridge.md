# ROS 2 Bridge Troubleshooting

## First checks
Record Isaac Sim launch mode, bridge extension state, `ROS_DOMAIN_ID`, `RMW_IMPLEMENTATION`, ROS distro/platform, container network, and whether simulation is playing.

## Workspace contract
Default local contract:
- `ROS_DOMAIN_ID=42`
- `/leader/joint_commands`: 13-float command
- `/follower/joint_commands`: follower command bridge
- `/follower/joint_states`: same semantic 13-feature order

## Missing topics
Check bridge extension, domain mismatch, graph execution trigger, simulation play state, container network, and whether source nodes are valid after 6.0 graph migration.

## Stale or wrong data
Check simulation clock, publish rate, QoS, stale graph node input, joint binding, and asset articulation paths.

## Simulation Control
If world services/actions are missing, verify the Simulation Control extension/startup flag and installed simulation_interfaces version before changing ROS application code.

## Boundaries
- Topic transport and domain issues stay here.
- Graph wiring issues hand off to `$isaac-sim-omnigraph-builder`.
- Joint order/binding issues hand off to `$isaac-sim-60-robot-assets` or `$isaac-sim-robot-setup-tuning`.

## Verification
Use `ros2 topic list`, `ros2 topic echo --once`, `ros2 topic hz`, and service/action listing for Simulation Control.
