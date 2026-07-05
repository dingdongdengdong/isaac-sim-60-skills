# Isaac Sim 6.0 Runtime Reference

## Official docs checked
- Release notes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html
- Container installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_container.html
- Setup tips: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_faq.html
- Performance handbook: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/reference_material/sim_performance_optimization_handbook.html

## 6.0.0 facts to remember
- Isaac Sim 6.0.0 uses Kit 110.1.1.
- 6.0 adds multitick rendering: cameras and RTX Lidars can be scheduled by simulation time.
- RT2 is the default rendering mode in 6.0 and is relevant for performance/fidelity tradeoffs.
- The official container tag for this skill is `nvcr.io/nvidia/isaac-sim:6.0.0`.

## Read-only host checks
```bash
nvidia-smi
docker --version
docker info >/tmp/docker-info.txt
docker image inspect nvcr.io/nvidia/isaac-sim:6.0.0 >/tmp/isaacsim60-image.json
```

## Workspace commands
```bash
cd /home/dong/robot/superarm_ws
cp isaacsim_test/.env.example isaacsim_test/.env  # only if .env is absent
cd isaacsim_test
docker compose config >/tmp/isaacsim60-compose.yml
bash run_isaacsim60_headless_screenshot.sh
```

## Local evidence paths
- Startup script: `isaacsim_test/run_isaacsim60_headless_screenshot.sh`
- Compose service: `isaacsim_test/docker-compose.yml`, service `isaac-sim-60`
- Runtime log: `isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log`
- Runtime status: `isaacsim_test/artifacts/isaacsim60_headless_status.json`
- Screenshot target: `isaacsim_test/artifacts/echo_full_simready_startup_isaacsim60.png`

## Cautions
- Stop other Isaac Sim instances before container startup to avoid GPU memory pressure.
- If `docker pull` stalls, record the layer and byte count; do not assume the image is installed.
- In headed mode, `xhost +local:docker` may be needed, but headless evidence is preferred.
