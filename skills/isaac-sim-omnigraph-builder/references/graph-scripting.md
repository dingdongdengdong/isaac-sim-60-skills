# Graph Scripting

## Official docs
- OmniGraph overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/index.html
- Isaac Sim OmniGraph tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_tutorial.html
- OmniGraph via Python scripting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_scripting.html
- Commonly used OmniGraph shortcuts: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omnigraph/omnigraph_shortcuts.html

## Build pattern
1. Start or attach to Isaac Sim through `$isaac-sim-python-scripting`.
2. Enable required extensions.
3. Create or locate a stable graph path.
4. Create nodes with explicit type names.
5. Set attributes.
6. Connect execution pins and data pins.
7. Run the graph trigger while simulation is playing or stepped.
8. Save a report with graph path, node paths, attributes, connections, extensions, and verification artifact.

## Graph report fields
- graph path and graph type
- extension names enabled
- nodes and type names
- attribute values changed
- connections made
- execution trigger
- downstream artifact checked

## Execution triggers
A graph with no trigger is not a runnable workflow. For simulation graphs, connect an appropriate tick/playback trigger. For one-shot diagnostics, document how the graph was evaluated.
