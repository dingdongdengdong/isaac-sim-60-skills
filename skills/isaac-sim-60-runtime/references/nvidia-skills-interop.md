# NVIDIA Skills Interop for Isaac Sim 6.0

## Upstream repo checked
- Repository: https://github.com/nvidia/skills
- Local inspection clone used during authoring: `/tmp/nvidia-skills`
- Relevant upstream skill paths inspected:
  - `plugins/nvidia-skills/skills/omniverse-cad-to-simready`
  - `plugins/nvidia-skills/skills/omniverse-usd-performance-tuning`
  - `plugins/nvidia-skills/skills/omniverse-realtime-viewer`

## What exists upstream
The NVIDIA skills repo does not currently provide a dedicated Isaac Sim 6.0 robot articulation/binding skill. It provides broader Omniverse and Physical AI skills that are useful around Isaac Sim workflows:

- `omniverse-cad-to-simready`: end-to-end CAD/source-asset to SimReady USD workflow, including conversion, material/physics assignment, validation, conformance, rendering, and packaging.
- `omniverse-usd-performance-tuning`: USD scene performance diagnosis and optimization for slow loading, memory, FPS, validation, and Scene Optimizer workflows.
- `omniverse-realtime-viewer`: Omniverse USD viewer app routing, realtime rendering/streaming, viewport interaction, and validation guidance.

## How this repo should use them
Use this Isaac Sim skill pack as the owner for Isaac Sim 6.0-family runtime, ROS 2, robot articulation, sensors, SDG, and control contracts. Hand off to NVIDIA upstream skills only for their broader Omniverse scope:

- Source CAD or generic source asset needs SimReady conversion: use upstream `omniverse-cad-to-simready` first, then return to `$isaac-sim-60-robot-assets` to inspect whether the resulting USD is a controllable articulation.
- Converted USD loads slowly, has high memory use, low FPS, or needs generic USD optimization: use upstream `omniverse-usd-performance-tuning`, then return to Isaac Sim skills for robot/control validation.
- User needs a standalone Omniverse viewer or realtime viewer app: use upstream `omniverse-realtime-viewer`; use `$isaac-sim-viewport-debugger` for Isaac Sim in-app viewport evidence.

## Important boundary
A successful CAD-to-SimReady or USD validation pass does not prove Isaac Sim controllability. If inspection shows:

```text
meshes > 0
rigid bodies > 0
physics joints = 0
articulation roots = 0
```

then the USD is still a visual/rigid-body asset. Keep it in `$isaac-sim-60-robot-assets`, mark `binding_pending`, then use `$isaac-sim-60-articulation-builder` before any ROS, LeRobot, Articulation Controller, or joint sensor work.

## Do not vendor upstream by default
Do not copy the whole `NVIDIA/skills` repo into this repo. If upstream skills are needed locally, install or clone them as a separate skill pack/plugin so this Isaac Sim 6.0-focused pack stays focused.
