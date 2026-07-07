# Colliders, Mass, and Inertia

## Official docs
- OpenUSD collider pairs tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/openusd_tuning_tutorials/tutorial_04_collider_pairs.html
- Physics fundamentals: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/physics/index.html
- Physics Inspector: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/physics/index.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html

## Collider checks
Record:
- collider prim paths
- approximation type
- contact offsets and rest offsets when relevant
- self-collision pairs and disabled collision pairs
- visual/collider alignment screenshots when useful
- backend assumption and solver settings when relevant

## Mass and inertia checks
Record:
- mass per dynamic link
- center of mass
- inertia tensor or principal axes
- suspicious scale/unit conversions
- extremely light/heavy links

## Symptoms
- Jitter at rest: collider penetration, bad mass ratio, solver settings, unstable contacts, or over-strong drive gains.
- Exploding robot: overlapping colliders, invalid inertia, excessive gains, or bad joint constraints.
- Falls through floor: missing collider, disabled collision, wrong collision layer, or bad physics scene.
- Link separates visually: joint parent/child path or transform is wrong before tuning gains.
