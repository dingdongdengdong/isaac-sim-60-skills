# Custom Nodes

## Official docs
- Custom Python nodes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_custom_python_nodes.html
- Custom C++ nodes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_custom_cpp_nodes.html
- Building custom IPC OmniGraph nodes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_custom_ipc_nodes.html

## Python node constraints
Use custom Python nodes only when built-in nodes plus normal Python scripting are insufficient. Record extension name, `.ogn` schema, input/output attributes, and how the node is loaded.

## When to create a custom node
Create a custom node for reusable graph behavior, typed graph I/O, or real-time graph integration. Do not create one just to run a one-off script; use `$isaac-sim-python-scripting` instead.

## Report
Include source file paths, extension path, generated files, node type name, graph path, and verification artifact.
