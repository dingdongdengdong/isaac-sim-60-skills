# Camera Workflows

## Official docs checked
- Camera sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_camera.html
- Depth sensors: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_camera_depth.html
- Structured light cameras: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/sensors/isaacsim_sensors_camera_structured_light.html
- Camera migration: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/migration_guides/isaac_sim_6_0/sensors_camera_to_experimental_rtx.html
- ROS 2 camera tutorial: https://docs.isaacsim.omniverse.nvidia.com/6.0.0/ros2_tutorials/tutorial_ros2_camera.html

## API choice
- Human viewport evidence: use `$isaac-sim-viewport-debugger`, not this reference.
- Dataset/render-product cameras: use Replicator or camera sensor APIs and record render product, annotators, and writer.
- New 6.0 work: prefer the documented experimental camera/RTX path; old Camera API imports are migration-only unless the workspace pins them.

## Output checklist
Record camera prim path, parent frame, resolution, focal/lens settings, RGB/depth/semantic/instance outputs, render product path, annotators/writers, timing policy, frames stepped, output files, and metadata.

## Timing
A camera that exists is not a camera that has produced data. After creating/changing cameras, advance enough app/render frames and verify the file/buffer timestamp changed.

## Lens distortion and calibration
When replay fidelity matters, persist calibration metadata with the episode/dataset. For ROS CameraInfo, verify intrinsics instead of assuming square pixels or `fx == fy`.

## Capture checks
If an image is blank or stale, check stage load, camera orientation, clipping range, render product, writer flush, and frame stepping before changing materials or lighting.
