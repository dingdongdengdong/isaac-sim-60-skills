# Viewport API Patterns

## Core imports

```python
from omni.kit.viewport.utility import (
    get_active_viewport,
    get_active_viewport_camera_path,
    capture_viewport_to_file,
    frame_viewport_prims,
    next_viewport_frame_async,
    post_viewport_message,
)
```

## Active viewport

```python
viewport = get_active_viewport()
if viewport is None:
    raise RuntimeError("No active viewport. Use camera/render-product capture in headless mode.")
```

## Camera path and resolution
`viewport.camera_path` and `viewport.resolution` are the most useful direct controls. Treat both as report fields.

```python
viewport.resolution = (1280, 720)
camera_path = str(get_active_viewport_camera_path() or viewport.camera_path)
```

When switching cameras, prefer an existing camera prim and do not create/persist a new camera in the user's USD unless explicitly requested.

## Frame prims
Frame target prims before capture:

```python
frame_viewport_prims(viewport, prims=["/World/Robot/right_wrist_link"])
```

Validate prim paths against the current stage when possible, but include missing paths in the report so the user can see what was requested.

## Wait for frames
After changing camera, resolution, stage selection, or framed prims, wait several viewport frames before capture.

If the installed Kit version exposes `next_viewport_frame_async()` without a viewport argument, call it without arguments.
