---
name: isaac-sim-viewport-debugger
description: Use when an agent needs to inspect, frame, capture, or visually debug Isaac Sim or Omniverse Kit viewports, USD stages, robot links, joints, articulation setup, camera views, screenshots, before/after simulation visuals, or headless-vs-GUI viewport capture decisions.
---

# Isaac Sim Viewport Debugger

Use this skill to create visual evidence from Isaac Sim viewports without confusing viewport screenshots with physics validation. Prefer small, repeatable captures plus a JSON report that records camera path, resolution, target prims, runtime mode, and output paths.

## Workflow
1. Identify the runtime first: Isaac Sim GUI, standalone `headless=False`, standalone `headless=True`, or another Omniverse Kit app.
2. Read `references/runtime-gate.md` before choosing viewport capture versus camera render-product capture.
3. If a GUI viewport exists, use `omni.kit.viewport.utility` to get the active viewport, set resolution, frame target prims, wait several frames, and capture.
4. Always save outputs under a new diagnostics directory; never overwrite the user's USD or create permanent debug cameras in the source stage without explicit approval.
5. Report the camera path, resolution, target prim paths, screenshot path, and JSON report path.
6. For robot attachment, joint, or articulation visual issues, combine screenshots with USD/articulation inspection; screenshots alone are not proof of valid physics.

## Read Order
- Read `references/runtime-gate.md` for GUI/headless routing.
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
- Do not use active GUI viewport capture in headless mode unless a viewport/render product has explicitly been created.
- Do not treat a screenshot as validation of joints, colliders, drives, or articulation correctness.
- Do not edit the user's USD just to add a debug camera; create a separate layer or ask first if a persistent camera is required.
- Always write diagnostics to a fresh or explicit output directory.
- Always preserve the exact failing command, runtime mode, and artifact paths when capture fails.
