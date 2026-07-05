#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pillow_diff(before: Path, after: Path) -> dict:
    try:
        from PIL import Image, ImageChops, ImageStat
    except Exception as exc:
        return {"available": False, "reason": str(exc)}

    with Image.open(before) as before_img, Image.open(after) as after_img:
        before_rgba = before_img.convert("RGBA")
        after_rgba = after_img.convert("RGBA")
        if before_rgba.size != after_rgba.size:
            return {
                "available": True,
                "same_dimensions": False,
                "before_dimensions": list(before_rgba.size),
                "after_dimensions": list(after_rgba.size),
            }
        diff = ImageChops.difference(before_rgba, after_rgba)
        bbox = diff.getbbox()
        stat = ImageStat.Stat(diff)
        mean_abs = sum(stat.mean) / len(stat.mean)
        extrema = diff.getextrema()
        return {
            "available": True,
            "same_dimensions": True,
            "dimensions": list(before_rgba.size),
            "different": bbox is not None,
            "difference_bbox": list(bbox) if bbox else None,
            "mean_absolute_channel_delta": mean_abs,
            "channel_extrema": [list(item) for item in extrema],
        }


def compare(args: argparse.Namespace) -> dict:
    before = Path(args.before)
    after = Path(args.after)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if not before.exists():
        raise FileNotFoundError(before)
    if not after.exists():
        raise FileNotFoundError(after)

    before_hash = file_digest(before)
    after_hash = file_digest(after)
    report = {
        "script": Path(__file__).name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "before": str(before),
        "after": str(after),
        "before_size_bytes": before.stat().st_size,
        "after_size_bytes": after.stat().st_size,
        "before_sha256": before_hash,
        "after_sha256": after_hash,
        "same_file_bytes": before_hash == after_hash,
        "pixel_diff": pillow_diff(before, after),
    }
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare before/after viewport screenshots.")
    parser.add_argument("--before", required=True, help="before image")
    parser.add_argument("--after", required=True, help="after image")
    parser.add_argument("--out", default="outputs/viewport_debug/before_after_report.json", help="comparison report JSON")
    return parser


def main() -> None:
    report = compare(build_parser().parse_args())
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
