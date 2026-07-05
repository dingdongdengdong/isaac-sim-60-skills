# Python Entrypoints

## Official docs
- Python scripting concepts: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/python_scripting_concepts.html
- Python environment installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_python.html
- Python scripting index: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/index.html
- Workflows: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/introduction/workflows.html

## Choose the surface
- Standalone Python: best for automation, batch checks, headless screenshots, and reproducible diagnostics.
- Interactive Script Editor: best for probing an already-running GUI app.
- Jupyter: useful for exploration, but remember notebook shutdown behavior differs from normal scripts.
- Extension code: use when behavior must live as a reusable Kit/Isaac Sim extension.
- Remote Python server or MCP: use when an external agent must drive a running Isaac Sim session.

## Common commands
Run scripts with the Isaac Sim Python environment when possible:

```bash
./python.sh path/to/script.py
```

Generate VS Code settings from a workspace folder when code completion is needed:

```bash
python -m isaacsim --generate-vscode-settings
```

Inside a container, run the same commands from the Isaac Sim root or configured app path.
