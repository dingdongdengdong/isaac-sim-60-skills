# OmniGraph Troubleshooting

## Node does not run
Check extension enabled, node type available, graph execution trigger connected, simulation playing/stepped, and log errors.

## Attribute does not update
Check attribute name, type, graph evaluation order, source-node output, and whether a stale UI value differs from runtime data.

## ROS 2 output missing
Check bridge extension, domain, topic/QoS, source-node migration, execution trigger, and external `ros2 topic` command.

## Sensor output missing
Check sensor prim, render product, annotator/GenericModelOutput, tick/render policy, and at least one simulation/render step.

## Migration symptom
If a 5.1 graph loaded into 6.0 shows disconnected or ignored prim path inputs, consult the ROS/sensor migration docs before adding replacement nodes.

## Execution order checks
If values update one frame late or never reach a publisher, inspect graph evaluation order and trigger placement. Report whether the data source is read before or after simulation, sensor, or ROS bridge updates.

## Report fields
For every graph failure, preserve graph path, node type names, extension names, changed attributes, connections, trigger source, simulation play/paused state, and the downstream artifact that failed to appear.
