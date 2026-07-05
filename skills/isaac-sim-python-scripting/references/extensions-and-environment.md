# Extensions and Environment

## Enable extensions intentionally

Enable extensions before importing or using their APIs:

```python
from omni.isaac.core.utils.extensions import enable_extension

enable_extension("isaacsim.ros2.bridge")
```

If that helper is not available in the installed version, use the Kit extension manager API. Always record which extension names were enabled.

## Python packages

Use the Isaac Sim Python interpreter for packages that must import inside Isaac Sim:

```bash
./python.sh -m pip install package-name
```

For pip-based Isaac Sim installs, prefer a dedicated virtual environment and record the installed `isaacsim-*` packages.

## ROS 2 environment

When scripts use ROS 2, preserve `ROS_DOMAIN_ID`, `RMW_IMPLEMENTATION`, and middleware-specific variables. Hand off to `$isaac-sim-60-ros2-sitl` for ROS bridge behavior, topics, QoS, and LeRobot contracts.

## Avoid environment drift

Do not silently change global shell profiles, Docker images, or source asset paths. Prefer per-command environment variables and saved diagnostics.
