# Capture Patterns

## Screenshot to file

Use `capture_viewport_to_file(viewport, file_path=...)` for the normal evidence path. Await or wait on the returned helper before reading the file.

```python
capture = capture_viewport_to_file(viewport, file_path="/tmp/viewport.png")
result = capture.wait_for_result(completion_frames=30)
if inspect.isawaitable(result):
    await result
```

## Buffer capture

Use `capture_viewport_to_buffer` only when an agent needs to inspect pixels in memory or pipe data into a custom analyzer. For most diagnostics, file capture is easier to preserve and review.

## JSON report fields

Write a JSON report next to the screenshot:

```json
{
  "runtime_mode": "gui",
  "camera_path": "/OmniverseKit_Persp",
  "resolution": [1280, 720],
  "target_prims": ["/World/Robot/right_wrist_link"],
  "screenshot": "outputs/viewport_debug/right_wrist_link.png",
  "script": "frame_prim_and_capture.py"
}
```

## Before/after evidence

For visual regression or attachment debugging, save:

- Before image and report.
- After image and report.
- Comparison report with file hashes, file sizes, and optional pixel difference.

Do not claim "fixed" from visual comparison alone; pair the images with USD schema, joint, collider, or articulation evidence.
