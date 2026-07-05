#!/usr/bin/env bash
set -u
IMAGE="${ISAAC_SIM_IMAGE:-nvcr.io/nvidia/isaac-sim:6.0.0}"
WS="${SUPERARM_WS_PATH:-/home/dong/robot/superarm_ws}"
SIMREADY_DEFAULT="$WS/isaacsim_test/outputs/simready/echo_full/pipeline/04_conform/repair-loop-02-fet005/fet005-grasp/echo_full_robot_arm_hand.usd"
SIMREADY_PATH="${SIMREADY_USD_PATH:-$SIMREADY_DEFAULT}"

echo "[isaacsim60-host-check] image=$IMAGE"
echo "[isaacsim60-host-check] workspace=$WS"
echo "[isaacsim60-host-check] simready_usd=$SIMREADY_PATH"

check_cmd() {
  if command -v "$1" >/dev/null 2>&1; then
    echo "OK command: $1 ($(command -v "$1"))"
    return 0
  else
    echo "MISSING command: $1"
    return 1
  fi
}

check_cmd nvidia-smi || true
check_cmd docker || true
if command -v nvidia-smi >/dev/null 2>&1; then
  nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader || true
fi
if command -v docker >/dev/null 2>&1; then
  docker --version || true
  if docker image inspect "$IMAGE" >/dev/null 2>&1; then
    echo "OK docker image present: $IMAGE"
  else
    echo "MISSING docker image: $IMAGE"
    echo "pull command: docker pull $IMAGE"
  fi
fi
[ -f "$WS/isaacsim_test/docker-compose.yml" ] && echo "OK compose file present" || echo "MISSING compose file: $WS/isaacsim_test/docker-compose.yml"
[ -f "$SIMREADY_PATH" ] && echo "OK SimReady USD present" || echo "MISSING SimReady USD: $SIMREADY_PATH"
[ -f "$WS/isaacsim_test/.env" ] && echo "OK .env present" || echo "NOTE .env absent: copy isaacsim_test/.env.example if needed"
