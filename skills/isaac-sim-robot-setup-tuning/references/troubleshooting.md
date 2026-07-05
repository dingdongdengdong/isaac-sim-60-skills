# Robot Setup Tuning Troubleshooting

## Robot collapses

Check:
- zero or weak drive gains
- missing articulation root
- missing or wrong joint drive mode
- mass/inertia scale
- gravity direction and physics scene

## Robot explodes or jitters

Check:
- overlapping colliders
- bad mass ratios
- invalid inertia
- excessive stiffness
- missing damping
- solver settings
- closed-loop constraints

## Joint moves wrong direction

Check:
- joint axis
- local joint frames
- importer coordinate conversion
- mimic ratio sign
- command sign convention

## Link detaches or jumps to origin

Check:
- joint parent/child body paths
- transform reset or missing xform op
- payload/layer composition
- articulation hierarchy
- whether the visual link and physics link are different prims

## Evidence before edits

Before changing values, capture current prim paths and properties. After changing values, rerun the smallest test that demonstrated the failure.
