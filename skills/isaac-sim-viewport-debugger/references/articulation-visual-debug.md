# Articulation Visual Debug

## Useful capture sequence

For robot assets, capture both full context and focused links:

1. Full robot.
2. Base or articulation root.
3. Shoulder/elbow/wrist chain.
4. End effector or hand attachment.
5. Any link that jumps to the world origin, separates, or has suspicious scale.

## Report these fields

- Robot root prim path.
- Target link or joint prim paths.
- Camera path and resolution.
- Before/after timestep or command.
- Whether the stage was paused, playing, or stepped.
- Screenshot paths.

## Visual symptoms and next checks

- Link visually detached: inspect joint parent/child body paths and local transforms.
- Link at world origin: inspect missing parent relationship, broken xform ops, or reset transform.
- Hand/wrist offset: inspect attachment transform and frame conventions.
- Axis looks wrong: inspect joint axis, local frame, and imported coordinate conversion.
- Mesh appears correct but physics fails: inspect collider approximation, mass/inertia, articulation root, and drive gains.

Use `$isaac-sim-60-robot-assets` for USD/importer/articulation mapping and `$isaac-sim-60-troubleshooting` for runtime failures.
