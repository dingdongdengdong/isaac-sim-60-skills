#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import inspect
import json
from datetime import datetime, timezone
from pathlib import Path


def parse_resolution(value: str) -> tuple[int, int]:
    parts = value.lower().replace(",", "x").split("x")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("resolution must look like 1280x720")
    width, height = int(parts[0]), int(parts[1])
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("resolution dimensions must be positive")
    return width, height


async def wait_frames(viewport, frames: int, next_viewport_frame_async) -> None:
    for _ in range(max(frames, 0)):
        try:
            await next_viewport_frame_async(viewport)
        except TypeError:
            await next_viewport_frame_async()


async def wait_capture(capture, completion_frames: int) -> None:
    if hasattr(capture, "wait_for_result"):
        result = capture.wait_for_result(completion_frames=completion_frames)
        if inspect.isawaitable(result):
            await result
        return
    if inspect.isawaitable(capture):
        await capture


def kit_version() -> str | None:
    try:
        import omni.kit.app

        app = omni.kit.app.get_app()
        return str(app.get_build_version())
    except Exception:
        return None


async def capture_active_viewport(args: argparse.Namespace) -> dict:
    from omni.kit.viewport.utility import (
        capture_viewport_to_file,
        get_active_viewport,
        get_active_viewport_camera_path,
        next_viewport_frame_async,
    )

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    image_path = Path(args.image)
    if not image_path.is_absolute():
        image_path = out_dir / image_path
    report_path = out_dir / args.report

    viewport = get_active_viewport()
    if viewport is None:
        raise RuntimeError("No active viewport. Use a camera/render-product workflow for headless mode.")

    viewport.resolution = args.resolution
    await wait_frames(viewport, args.frames, next_viewport_frame_async)
    capture = capture_viewport_to_file(viewport, file_path=str(image_path))
    await wait_capture(capture, args.completion_frames)

    report = {
        "script": Path(__file__).name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "runtime_mode": args.runtime_mode,
        "kit_version": kit_version(),
        "camera_path": str(get_active_viewport_camera_path() or getattr(viewport, "camera_path", "")),
        "resolution": list(args.resolution),
        "target_prims": [],
        "screenshot": str(image_path),
        "report": str(report_path),
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture the active Isaac Sim/Kit viewport.")
    parser.add_argument("--out-dir", default="outputs/viewport_debug", help="diagnostics output directory")
    parser.add_argument("--image", default="active_viewport.png", help="image path or name")
    parser.add_argument("--report", default="active_viewport_report.json", help="report JSON filename")
    parser.add_argument("--resolution", type=parse_resolution, default=(1280, 720), help="viewport resolution, e.g. 1280x720")
    parser.add_argument("--frames", type=int, default=5, help="viewport frames to wait before capture")
    parser.add_argument("--completion-frames", type=int, default=30, help="capture completion frames")
    parser.add_argument("--runtime-mode", default="gui", help="reported runtime mode")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    report = asyncio.get_event_loop().run_until_complete(capture_active_viewport(args))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
