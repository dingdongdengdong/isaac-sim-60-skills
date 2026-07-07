# Replicator SDG

## Official docs checked
- Replicator overview: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/index.html
- Synthetic Data Recorder: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/tutorial_replicator_recorder.html
- SDG workflows: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/tutorial_replicator_sdg_workflows.html
- Randomization snippets: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/tutorial_replicator_amr_navigation.html
- Replicator troubleshooting: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/replicator_tutorials/troubleshooting.html

## Capture policy
Define the dataset first: RGB, depth, semantic/instance segmentation, 2D/3D boxes, point cloud, event/action labels, or teleop episode sidecar. Then choose writer, annotators, camera/render products, randomizers, and stepping policy.

## Writers and annotators
Record writer name, output directory, render products, annotators, frame count, and flush/close call. Do not inspect output before the writer is flushed.

## Manual stepping
For deterministic captures, prefer explicit `rep.orchestrator.step()` or equivalent controlled stepping. Record whether physics, rendering, and writer stepping are coupled or separate.

## Randomization
Record seed and randomizer names. If randomization is expected but output repeats, confirm triggers fire and the orchestrator advances after changes.

## 6.0 notes
- 6.0 docs expand from classic perception Replicator into Action/Event, MobilityGen, and Teleoperation SDG. Route those to `action-event-teleop-sdg.md`.
- Migration from old domain randomization imports may require experimental namespace changes; record old and new import paths.

## Shutdown
Close or flush writers and record the final output directory. For long runs, include frame-count or file-count checks in the acceptance evidence.
