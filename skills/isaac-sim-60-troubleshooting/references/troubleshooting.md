# Isaac Sim 6.0 Troubleshooting Reference

## Official docs checked
- Troubleshooting hub: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/troubleshooting.html
- Setup tips: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_faq.html
- Robot setup troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/troubleshooting.html
- Replicator troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/troubleshooting.html
- RTX Lidar tutorial warnings: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_rtx_lidar.html

## Common symptom map
- Docker image missing or pull stalled: verify `docker image inspect nvcr.io/nvidia/isaac-sim:6.0.0`; re-run pull outside long composed workflows; record stalled layer.
- Container starts but no GUI: prefer headless screenshot first; for headed mode check `DISPLAY`, `/tmp/.X11-unix`, and `xhost`.
- Cannot connect to services: use `network_mode: host` for this workspace; check ports 8765 and 8766.
- No ROS topics: verify `ROS_DOMAIN_ID`, RMW variables, ROS 2 bridge extension, and matching Humble/Jazzy environment.
- Robot joints do not move: check joint limits, drive gains, mimic settings, and one-joint isolation.
- Bad imported geometry: inspect source mesh transforms and USD transforms.
- Replicator captures nothing: check capture-on-play, render products, writer attachment, output directory, and simulation stepping.
- RTX Lidar crash after UI changes: pause simulation before docking/redocking sensor windows.
- Object drops during grasp: tune collision proxies, spawn pose, close targets, drive force/damping, solver iterations, contact offsets, and friction; do not assume visuals equal collision.

## Local known blocker
`isaacsim_test/artifacts/isaacsim60_headless_status.json` previously recorded that the Isaac Sim 6.0 Docker image was not installed and pull stalled around one layer. Re-check the image before diagnosing scene code.

## Minimal evidence bundle
```bash
cd /home/dong/robot/superarm_ws
bash ~/.codex/skills/isaac-sim-60-runtime/scripts/check_isaacsim60_host.sh
python3 ~/.codex/skills/isaac-sim-60-troubleshooting/scripts/summarize_isaacsim60_logs.py \
  isaacsim_test/artifacts/isaac-sim-60-headless-screenshot.log
cat isaacsim_test/artifacts/isaacsim60_headless_status.json 2>/dev/null || true
```
