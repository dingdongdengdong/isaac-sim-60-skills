# Camera Sensor Versus Viewport

## Use viewport capture for human-facing visual debugging
Viewport capture is best for:
- what the current Isaac Sim UI sees
- framing a prim, joint, link, or robot section for review
- capturing before/after visual evidence during manual or scripted debugging
- documenting a livestream/remote GUI session after runtime is known good

## Use camera/render-product capture for sensor or headless workflows
Camera sensor and render-product capture is best for:
- headless Isaac Sim
- dataset generation
- RGB/depth/semantic/instance annotators
- reproducible fixed-camera regression images
- synthetic data pipelines and teleoperation episodes

## Do not mix the meanings
The viewport is a visual inspection surface. A camera sensor is part of the simulation/data pipeline. A viewport screenshot can show that a hand looks detached; it cannot prove that joints, colliders, drives, or mimic constraints are physically valid.
