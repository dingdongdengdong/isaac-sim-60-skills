# Startup and Runtime Failures

## Docker and image checks
1. Confirm Docker and NVIDIA runtime:
   ```bash
   nvidia-smi
   docker info >/tmp/docker-info.txt
   docker image inspect nvcr.io/nvidia/isaac-sim:6.0.0 >/tmp/isaacsim60-image.json
   ```
2. If the image is missing, pull/login/network issues are runtime issues, not scene issues.
3. For container launch, require `ACCEPT_EULA=Y`, `--gpus all`, and expected NVIDIA runtime/device visibility.

## Container environment
Record image tag, user/rootless behavior, mounted cache/log/output directories, ports, and whether the command uses GUI, livestream, or headless mode.

## Headless versus windowed
- Headless artifact generation should use camera/render-product or scripted screenshot paths.
- GUI viewport tasks need a real viewport or livestream/WebRTC surface.
- Do not diagnose blank active-viewport screenshots in a purely headless run as a camera sensor failure.

## Livestream/WebRTC
For remote GUI sessions, record exposed ports, browser/client, container logs, and whether Isaac Sim itself started before debugging network streaming.

## Cache, logs, and warmup
Slow first startup often includes shader/cache warmup. Preserve logs and cache paths before deleting anything.

## Verification
The official image tag for this workspace remains `nvcr.io/nvidia/isaac-sim:6.0.0`; if changing to another 6.0.0 tag, record both tags and the reason.
