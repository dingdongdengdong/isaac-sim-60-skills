# Camera Sensor Versus Viewport

## Use viewport capture for human-facing visual debugging

Viewport capture is best for:

- What the current Isaac Sim UI sees.
- Framing a prim, joint, link, or robot section for review.
- Capturing before/after evidence during manual or scripted debugging.
- Recording camera path and resolution used by the viewport.

## Use camera/render-product capture for sensor or headless workflows

Camera sensor and render-product capture is best for:

- Headless Isaac Sim.
- Dataset generation.
- RGB/depth/semantic/instance annotators.
- Reproducible fixed-camera regression images.
- Synthetic data pipelines.

## Do not mix the meanings

The viewport is a visual inspection surface. A camera sensor is part of the simulation/data pipeline. A viewport screenshot can show that a hand looks detached; it cannot prove that joints, colliders, drives, or mimic constraints are physically valid.
