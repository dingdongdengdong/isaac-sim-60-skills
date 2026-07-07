# Rendering and Capture Troubleshooting

## Classify the capture surface
- Active viewport screenshot: human GUI evidence; use `$isaac-sim-viewport-debugger`.
- Camera/render-product capture: sensor/dataset evidence; use `$isaac-sim-60-sensors-sdg`.
- Replicator writer output: SDG evidence; check writer, annotators, orchestrator, and flush.
- Livestream/WebRTC: remote GUI transport; check runtime/ports before sensor code.

## Blank screenshots
Check launch mode, viewport existence, camera orientation, clipping range, renderer initialization, stage load, and wait-for-frame behavior.

## Replicator writes nothing
Check output permissions, render product, annotators, writer initialization, `orchestrator.step()`, frame count, and flush/close.

## Sensor data missing
After verifying runtime/rendering, inspect sensor prim, profile/config, tick rate, render product, annotator/GenericModelOutput, and output path.

## Known-issue handling
Record known-issue link or release-note context when choosing to ignore a warning. Do not bury actionable errors under warning noise.

## Verification
A capture fix is verified by a fresh file/buffer with changed timestamp, nonzero size, expected dimensions, and associated JSON/log evidence.
