# Extensions and Environment

## Official docs checked
- Extension enabling/development tools: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/index.html
- Python environment installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_python.html
- ROS 2 installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_ros.html
- Release notes breaking changes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html

## Enable extensions intentionally
Enable extensions before importing or using their APIs. Prefer current `isaacsim.*` extension names in 6.0.

```python
from omni.isaac.core.utils.extensions import enable_extension  # migration-only helper in older code

enable_extension("isaacsim.ros2.bridge")
```

If the helper is unavailable or migrated, use the Kit extension manager API. Always record which extension names were enabled and whether any old `omni.isaac.*` names were replaced.

## Python packages
Use the Isaac Sim Python interpreter for packages that must import inside Isaac Sim:

```bash
./python.sh -m pip install package-name
```

For pip-based Isaac Sim installs, prefer a dedicated virtual environment and record installed `isaacsim-*` packages.

## ROS 2 environment
When scripts use ROS 2, preserve `ROS_DOMAIN_ID`, `RMW_IMPLEMENTATION`, and middleware-specific variables. Hand off to `$isaac-sim-60-ros2-sitl` for ROS bridge behavior, topics, QoS, and LeRobot contracts.

## MCP and remote execution safety
- Treat Python Server and MCP as control surfaces for a running Isaac Sim app, not as standalone script equivalents.
- Record session endpoint, enabled extensions, stage path, and any generated artifacts.
- Do not leave remote execution enabled without noting how it was started and stopped.

## Avoid environment drift
Do not silently change global shell profiles, Docker images, or source asset paths. Prefer per-command environment variables and saved diagnostics.
