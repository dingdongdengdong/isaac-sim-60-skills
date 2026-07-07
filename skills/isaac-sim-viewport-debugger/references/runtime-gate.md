# Runtime Gate

## Decide the capture path first
Use active viewport capture only when Isaac Sim or Kit has a GUI viewport, livestream/WebRTC GUI surface, or an explicitly created viewport API. Headless Isaac Sim often has no active GUI viewport, even if rendering is available.

## Runtime modes
- GUI Isaac Sim: active viewport workflows are valid.
- Livestream/WebRTC GUI: active viewport may be valid inside the running app; browser connectivity is a runtime issue.
- Standalone Isaac Sim with `headless=False`: active viewport workflows are usually valid after app and viewport extensions finish loading.
- Standalone Isaac Sim with `headless=True`: prefer camera render products, Replicator, or camera/sensor APIs.
- Kit/Omniverse apps: active viewport workflows are valid only when `omni.kit.viewport.utility` can return a viewport.

## Gate checks
1. Confirm launch command and whether `headless=True`, `--no-window`, container livestream, or local GUI was used.
2. Try `get_active_viewport()` only after app loaded the stage and rendered at least one frame.
3. If no viewport is returned, do not keep retrying blindly; switch to camera/render-product capture.
4. If a screenshot is required in headless mode, create a camera/render product workflow and record that the result is not an active GUI viewport capture.

## Diagnostics directory
Use a new directory such as:

```text
outputs/viewport_debug/YYYYMMDD-HHMMSS/
```

Include screenshot or buffer output, JSON report with runtime mode/camera path/resolution/target prims/errors, and the command used to run the capture script.
