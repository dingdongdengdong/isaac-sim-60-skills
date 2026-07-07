# SimulationApp Patterns

## Official docs checked
- Python scripting concepts: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/python_scripting_concepts.html
- Python environment: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/manual_standalone_python.html
- Core API overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/core_api_overview.html

## Standalone import order
Use this order in standalone scripts:

```python
from isaacsim.simulation_app import SimulationApp

simulation_app = SimulationApp({"headless": True})

import omni.usd
from pxr import Usd
```

Import `omni.*`, `pxr.*`, and runtime Isaac Sim modules only after `SimulationApp` starts. Break this rule only for modules documented as pure Python setup code.

## Headless flag
Use `{"headless": True}` for CI, containers, and remote artifact generation. Use `{"headless": False}` when a GUI viewport or interactive UI is required.

## Update loop
Call app updates after opening stages, enabling extensions, adding sensors, or changing graph state:

```python
for _ in range(10):
    simulation_app.update()
```

Prefer a condition-based wait when checking for a loaded stage, initialized articulation, available viewport, ROS topic, or saved artifact.

## Shutdown
If the script created the app, close it:

```python
simulation_app.close()
```

In notebooks, closing the app can terminate the kernel; document that behavior before using it.

## Migration checks
- Verify `isaacsim.*` imports and extension names before assuming missing Python paths.
- Check old Core API usage against the current 6.0 experimental/core guidance when porting 5.1 scripts.
- Run a minimal script that starts, opens/creates a stage, updates a few frames, writes one artifact, and closes.

## Diagnostics
Record command line, headless flag, Isaac Sim version when available, enabled extensions, stage path, output artifacts, exception text, and log path.

## Minimal smoke script expectation
A useful automation smoke test starts `SimulationApp`, enables required extensions, opens or creates one simple stage, advances a few frames, writes one artifact or prints one inspected value, and closes cleanly. Use this before running large scene automation.
