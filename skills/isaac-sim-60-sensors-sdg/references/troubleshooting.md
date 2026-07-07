# Sensor and SDG Troubleshooting

## No camera data
Check camera prim, render product, annotator/writer attachment, stage load, frame stepping, output directory, and writer flush.

## Blank or bad frames
Check camera orientation, clipping range, lighting/materials, renderer initialization, headless support, and whether the capture path is viewport versus render product.

## No Lidar/Radar/Acoustic or partial scans
Check sensor prim/profile, tick rate, scan accumulation, non-visual materials, GenericModelOutput/annotator attachment, debug draw, and whether enough simulation/render ticks have elapsed.

## Physics/PhysX sensor missing
Check physics scene, backend assumption, sensor attachment target, articulation/contact availability, and whether the sensor family requires exact official API lookup.

## Replicator files missing or skipped
Check orchestrator stepping, writer initialization, randomization trigger, output permissions, file count, and flush/close calls.

## Teleop or MobilityGen episodes misaligned
Check recorder start/stop timing, state/action mapping, camera stream cadence, dropped frames, and whether the LeRobot 13D contract was preserved.

## ROS topics stale or missing
After confirming the sensor itself produces data, hand off to `$isaac-sim-60-ros2-sitl` and `$isaac-sim-omnigraph-builder`.

## Evidence to preserve
Save exact script/command, Isaac Sim version and launch mode, sensor prim paths, render products or graph paths, output directory and file count, one tiny sample output or screenshot, log path, and first actionable error.

## Migration failure pattern
If a migrated 5.1 script imports old sensor modules or emits missing extension errors, migrate extension/API names first. Then rerun a one-frame or one-scan minimal scene before testing the full dataset workflow.

## Acceptance evidence
A sensor/SDG fix needs a fresh artifact: image dimensions, point count, file count, sample sensor payload, ROS topic sample, or episode metadata showing synchronized state/action/video timing.
