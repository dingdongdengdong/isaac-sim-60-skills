# Custom Nodes

## Official docs
- Custom Python nodes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_custom_python_nodes.html
- Custom C++ nodes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_custom_cpp_nodes.html
- Building custom IPC OmniGraph nodes: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_custom_ipc_node.html

## Python node constraints

For Python nodes:
- the Python class name must match the node definition
- the `.ogn` definition and implementation file names must align with the node type
- `compute(db)` must return a success value when execution succeeds
- Action Graph nodes need an execution input when they must be explicitly triggered

## When to create a custom node

Create a custom node only when reusable graph behavior is needed. For one-off automation, prefer a standalone Python script or a small graph using existing nodes.

## Report

Document node package path, node type name, inputs, outputs, execution pins, and how the node was triggered in a running graph.
