# Python Entrypoints

## Official docs
- Python scripting concepts: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/python_scripting_concepts.html
- Python environment installation: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/install_python.html
- Python scripting index: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/python_scripting/index.html
- Workflows: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/introduction/workflows.html
- VS Code: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/vscode.html
- Python Server: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/python_server.html
- Jupyter Notebook: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/jupyter_notebook.html
- Script Editor: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/omniverse_script_editor.html
- Isaac Sim MCP Server: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/isaac_sim_mcp.html

## Choose the surface
- Standalone Python: best for automation, batch checks, headless screenshots, and reproducible diagnostics.
- Interactive Script Editor: best for probing an already-running GUI app.
- Jupyter: useful for exploration, but notebook shutdown behavior differs from normal scripts.
- Extension code: use when behavior must live as a reusable Kit/Isaac Sim extension.
- Remote Python server: use when an external process must drive an already-running Isaac Sim session.
- MCP server: use when an agent/tooling workflow must drive Isaac Sim through the documented MCP surface.

## Common commands
Run scripts with the Isaac Sim Python environment when possible:

```bash
./python.sh path/to/script.py
```

Generate VS Code settings from a workspace folder when code completion is needed:

```bash
python -m isaacsim --generate-vscode-settings
```

Inside a container, run equivalent commands from the Isaac Sim root or configured app path and record container image/tag.

## 5.1-to-6.0 entrypoint risk
- Old code may import `omni.isaac.*` modules before starting Kit or rely on compatibility shims removed in 6.0.
- Migrate import names before debugging business logic.
- Preserve whether a script is standalone, extension, remote-server, or notebook code; lifecycle rules differ.
