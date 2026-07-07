# Isaac Sim 6.0 Runtime Reference

## Official docs checked
- Release notes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html
- Quick install: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/quick-install.html
- Requirements: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/requirements.html
- Workstation installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_workstation.html
- Container installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_container.html
- Python environment installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_python.html
- Livestream clients: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/manual_livestream_clients.html
- Setup tips and cache/log locations: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_faq.html
- Cloud deployment index: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_cloud.html
- Performance handbook: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/reference_material/sim_performance_optimization_handbook.html

## 6.0 runtime facts to remember
- Isaac Sim 6.0.0 uses Kit 110.1.1; 5.1 used Kit 107.3.3.
- The official container tag for this workspace remains `nvcr.io/nvidia/isaac-sim:6.0.0` until the local compose/runtime files are explicitly changed.
- 5.1 release notes call out rootless container behavior and multi-arch Docker support; re-check ownership and permissions before blaming Isaac Sim code.
- 6.0 docs include workstation, container, pip, cloud, and livestream surfaces. Do not assume a user is on the local container path.
- 6.0 adds a browser-based streaming/livestream path useful for remote GUI inspection; keep it separate from headless render-product validation.

## Runtime decision table
- Local GUI debugging: workstation install or container with livestream/WebRTC, then hand off viewport tasks to `$isaac-sim-viewport-debugger`.
- CI/headless artifact: container or pip environment with `headless=True`, explicit output directory, and preserved logs.
- ROS 2 SITL: container or workstation launch plus `$isaac-sim-60-ros2-sitl` for domain/RMW/QoS details.
- Cloud/remote workstation: verify GPU class, driver/runtime compatibility, EULA, ports, cache volume, and streaming endpoint before debugging scene code.
- API-only automation: use `$isaac-sim-python-scripting` for `SimulationApp`, extension enabling, and shutdown rules.

## Read-only host checks
From this repo root:

```bash
bash skills/isaac-sim-60-runtime/scripts/check_isaacsim60_host.sh
```

Manual equivalent:

```bash
nvidia-smi
docker info >/tmp/docker-info.txt
docker image inspect nvcr.io/nvidia/isaac-sim:6.0.0 >/tmp/isaacsim60-image.json
```

## Workspace commands
Prefer workspace scripts when present:

```bash
bash isaacsim_test/run_isaacsim60_headless_screenshot.sh
```

Expected outputs:
- `isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log`
- `isaacsim_test/artifacts/isaacsim60_headless_status.json`
- screenshot artifacts under the configured output directory

## Cautions
- Do not delete shader, asset, or download caches just because startup is slow; first classify warmup versus failure.
- Do not switch image tags or install modality without recording the old tag, new tag, and reason.
- Do not conflate active GUI viewport screenshots with headless camera/render-product output.
- If an extension import fails after migrating a 5.1 project, check for removed `omni.isaac.*` shims before changing Python paths.
