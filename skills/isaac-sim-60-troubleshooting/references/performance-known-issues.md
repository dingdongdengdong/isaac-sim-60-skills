# Performance and Known Issues

## Startup and shader warmup
Slow first launch can be cache/shader warmup. Record elapsed time, log progress, CPU/GPU use, cache paths, and whether a second run improves.

## Persistent settings and cache state
Do not delete caches/settings as a first step. If cache reset is necessary, record old paths and why the reset is safe.

## Runtime performance triage
Record scene complexity, asset load state, renderer mode, sensor/render product count, Replicator writers, ROS publish rates, CPU/GPU utilization, and FPS/RTF if available.

## Known issues
Use official known-issues pages to decide ignore versus fix. If a warning is known noise, record why it is not the cause of the missing artifact.

## Verification
A performance fix needs before/after evidence using the same scene, launch mode, sensors, and measurement method.
