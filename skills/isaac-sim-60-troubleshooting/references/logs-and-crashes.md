# Logs, Hangs, and Crashes

## Log locations
- Linux workstation/container: check the configured Isaac Sim/Kit log directory and mounted workspace artifacts.
- Windows: `%userprofile%\.nvidia-omniverse\logs\Kit\Isaac-Sim`.
- Workspace headless log: `isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log`.

## Summarizer workflow
Run:

```bash
python3 skills/isaac-sim-60-troubleshooting/scripts/summarize_isaacsim60_logs.py <log>
```

Then inspect the first actionable error, not only the last line.

## Known-issue noise
Compare warnings against the official known-issues page before changing code. Record whether a warning is ignorable noise or blocks the requested artifact.

## Hangs
Preserve command, elapsed time, CPU/GPU activity, current log tail, cache state, and whether shader compilation or asset download is still progressing.

## Crashes
Record signal/exception, stack trace if available, extension names recently enabled, asset path opened, GPU/driver info, and whether the crash reproduces on a minimal scene.

## Import and extension failures
For migrated 5.1 projects, check removed `omni.isaac.*` compatibility shims and renamed `isaacsim.*` extensions before changing Python paths.

## Verification
A crash fix needs the original command rerun through the point where the failing artifact is produced or the prior exception is absent.
