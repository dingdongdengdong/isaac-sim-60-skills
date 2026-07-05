# SimulationApp Patterns

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

## Diagnostics

Record:
- command line
- headless flag
- Isaac Sim version when available
- enabled extensions
- stage path
- output artifacts
- exception text and log path
