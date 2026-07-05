# OmniGraph Troubleshooting

## Node does not run

Check:
- graph type matches the desired execution model
- execution pins are connected
- simulation is playing when required
- required extension is enabled
- node path exists after stage load
- upstream tick/event source is active

## Attribute does not update

Check:
- exact attribute name and type
- whether the value is being overwritten each tick
- data pin connection direction
- whether a stage reload recreated the graph

## ROS 2 output missing

Check:
- ROS 2 bridge extension is enabled
- `ROS_DOMAIN_ID` matches external nodes
- topic name, namespace, QoS, and frame ID
- simulation time node is connected where needed
- topic has an active subscriber if publisher verification is required

## Sensor output missing

Check:
- sensor prim exists
- render product exists for camera-like outputs
- tick rate and frame timing are valid
- graph executes after sensor initialization
- output is inspected after at least one simulation/render step
