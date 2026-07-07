---
name: isaac-sim-viewport-debugger
description: Use when an agent needs to inspect, frame, capture, or visually debug Isaac Sim or Omniverse Kit viewports, USD stages, robot links, joints, articulation setup, camera views, livestream GUI sessions, screenshots, before/after simulation visuals, or headless-vs-GUI viewport capture decisions.
---

# Isaac Sim Viewport Debugger

Use this skill for human-facing visual evidence from an active viewport or a GUI-equivalent runtime. Keep it separate from sensor/render-product datasets.

## Workflow
1. Decide whether the runtime has an active GUI viewport, livestream/WebRTC GUI surface, or only headless rendering.
2. Read `references/runtime-gate.md` before trying active viewport APIs.
3. Choose capture target: active viewport, existing camera prim, framed prims, or before/after comparison.
4. Use the bundled script that matches the target when possible.
5. Write screenshots and JSON reports to a fresh diagnostics directory.
6. If capture fails because the run is headless, hand off to `$isaac-sim-60-sensors-sdg` for camera/render-product capture.

## Read Order
- Read `references/runtime-gate.md` for GUI/headless/livestream routing.
- Read `references/viewport-api-patterns.md` for active viewport, camera path, resolution, prim framing, and frame waits.
- Read `references/capture-patterns.md` for screenshot, buffer, and reporting patterns.
- Read `references/camera-vs-viewport.md` when deciding between viewport evidence and sensor/dataset capture.
- Read `references/articulation-visual-debug.md` for robot link, joint, wrist, hand, and before/after visual checks.
- Read `references/troubleshooting.md` when capture fails, returns blank images, or no active viewport exists.

## Scripts
- `scripts/capture_active_viewport.py`: capture the current active viewport to `active_viewport.png` plus `active_viewport_report.json`.
- `scripts/frame_prim_and_capture.py`: frame one or more prim paths, wait for viewport frames, then capture an image and report.
- `scripts/switch_camera_capture.py`: switch the active viewport to a camera prim/path, set resolution, then capture.
- `scripts/compare_before_after.py`: compare two saved images by hash, size, and optional Pillow pixel difference, then write a JSON report.

## Non-Negotiables
- Do not use active GUI viewport capture in headless mode unless a viewport/render surface has explicitly been created.
- Do not treat a screenshot as validation of joints, colliders, drives, or articulation correctness.
- Do not edit the user's USD just to add a debug camera; create a separate layer or ask first if a persistent camera is required.
- Always write diagnostics to a fresh or explicit output directory.
- Always preserve the exact failing command, runtime mode, and artifact paths when capture fails.
