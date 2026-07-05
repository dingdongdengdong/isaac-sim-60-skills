# Graph Scripting

## Official docs
- OmniGraph overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/index.html
- Isaac Sim OmniGraph tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_tutorial.html
- OmniGraph via Python scripting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_scripting.html
- Commonly used OmniGraph shortcuts: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_shortcuts.html

## Build pattern

Use Python graph creation when the graph must be repeatable. The exact API varies across Kit versions, but the process is stable:

1. Enable graph-dependent extensions.
2. Create or reuse an Action Graph prim.
3. Create nodes with stable names.
4. Set attributes.
5. Connect execution pins first, then data pins.
6. Save a report of graph topology.

## Graph report fields

Record:
- graph path
- graph type
- node type names
- node prim paths
- key attribute values
- execution connections
- data connections
- required extensions
- verification result

## Execution triggers

For Action Graphs, confirm an execution source such as playback tick, physics step, stage event, or explicit trigger. For Push Graphs, confirm that automatic frame evaluation is intended.
