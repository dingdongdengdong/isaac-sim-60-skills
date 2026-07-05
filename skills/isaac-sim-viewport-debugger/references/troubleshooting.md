# Troubleshooting

## No active viewport

Likely causes:

- Isaac Sim was launched headless.
- The viewport extension is not loaded.
- The script ran before the app opened a viewport or rendered a frame.

Actions:

1. Confirm the launch mode.
2. Wait a few app updates after stage load.
3. If still missing, switch to camera/render-product capture.

## Blank or stale screenshot

Likely causes:

- Captured before the next rendered frame.
- Camera is inside geometry or points away from the target.
- Stage is still loading.
- Viewport resolution changed but no frame was rendered afterward.

Actions:

1. Set resolution first.
2. Frame target prims or switch to a known camera.
3. Wait 5-10 viewport frames.
4. Capture and wait for completion frames.

## Prim does not frame

Likely causes:

- Prim path does not exist.
- Prim has no visible bounds.
- Target is hidden, unloaded, or inside an inactive payload.

Actions:

1. Check the prim path in the stage.
2. Capture a full-scene view.
3. Record missing or invalid prim paths in the JSON report.

## Capture helper never completes

Likely causes:

- Render loop is not advancing.
- App is blocked by modal UI, startup failure, or extension error.
- Output path is not writable.

Actions:

1. Confirm the app is still updating.
2. Confirm the output directory exists and is writable.
3. Preserve the log and exact command.
4. Fall back to a simpler active viewport capture or camera render product.
