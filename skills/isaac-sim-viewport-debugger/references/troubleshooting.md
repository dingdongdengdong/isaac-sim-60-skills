# Troubleshooting

## No active viewport
Likely causes: Isaac Sim launched headless, viewport extension missing, script ran before viewport/render frame, or the task is actually a livestream/runtime issue.

Actions:
1. Confirm launch mode.
2. Wait a few app updates after stage load.
3. If still missing, switch to camera/render-product capture.

## Blank or stale screenshot
Likely causes: captured before the next rendered frame, camera inside geometry or pointed away, stage still loading, or resolution changed without a new frame.

Actions:
1. Set resolution first.
2. Frame target prims or switch to a known camera.
3. Wait 5-10 viewport frames.
4. Capture and wait for completion frames.

## Prim does not frame
Check prim path exists, has visible bounds, is loaded/active, and is not hidden. Capture a full-scene view if needed.

## Capture helper never completes
Check render loop, modal UI/startup failure, extension errors, and output path permissions. Preserve the log and exact command.

## Livestream confusion
A browser livestream can fail even when Isaac Sim has an active viewport. Split the issue:
- Isaac Sim app started and viewport exists: viewport scripts may still work.
- Browser cannot connect: preserve ports, container logs, and runtime command; hand off to `$isaac-sim-60-runtime`.
- Browser shows a stale frame: wait for app frames and confirm simulation/render loop is advancing.

## Report fields
Always include launch command, headless/windowed/livestream mode, viewport availability, camera path, resolution, target prims, output path, and log path. For robot visuals, include the relevant articulation/link/joint prim paths.
