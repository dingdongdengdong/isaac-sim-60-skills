#!/usr/bin/env python3
"""Generate an explicit articulation mapping template from inspection JSON."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def common_ancestor(paths: list[str]) -> str:
    components = [str(path).strip("/").split("/") for path in paths if str(path).startswith("/") and str(path).strip("/")]
    if not components:
        return "/World/Robot"
    if len(components) == 1:
        only = components[0]
        return "/" if len(only) <= 1 else "/" + "/".join(only[:-1])
    prefix: list[str] = []
    for parts in zip(*components):
        if len(set(parts)) != 1:
            break
        prefix.append(parts[0])
    return "/" if not prefix else "/" + "/".join(prefix)


def child_path(root: str, child: str) -> str:
    return f"/{child}" if root == "/" else f"{root}/{child}"


def make_template(inspection: dict[str, Any]) -> dict[str, Any]:
    links = inspection.get("candidate_link_prims") or []
    source_usd = inspection.get("source_usd", "")
    root_guess = common_ancestor([str(link) for link in links])

    return {
        "schema_version": "isaac-sim-articulation-map-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_usd": source_usd,
        "source_status": inspection.get("status"),
        "articulation_root": root_guess,
        "joint_container": child_path(root_guess, "ArticulationJoints"),
        "candidate_links": links,
        "instructions": [
            "Fill joints explicitly from a robot spec, CAD assembly knowledge, URDF/MJCF, or manual prim inspection.",
            "Do not infer joint semantics from mesh positions alone.",
            "Remove example entries or set enabled=false before scaffold authoring.",
        ],
        "joints": [
            {
                "enabled": False,
                "name": "example_joint_replace_me",
                "path": child_path(root_guess, "ArticulationJoints/example_joint_replace_me"),
                "type": "revolute",
                "parent": links[0] if links else "/World/Robot/base_link",
                "child": links[1] if len(links) > 1 else "/World/Robot/child_link",
                "axis": "Z",
                "limits": {"lower": -1.57, "upper": 1.57},
                "drive": {"type": "angular", "stiffness": 1000.0, "damping": 100.0, "max_force": 1000.0},
            }
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate an articulation mapping JSON template.")
    parser.add_argument("inspection_json", type=Path, help="output from inspect_usd_articulation.py")
    parser.add_argument("--out", type=Path, required=True, help="mapping template JSON path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    inspection = json.loads(args.inspection_json.read_text(encoding="utf-8"))
    template = make_template(inspection)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(template, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"mapping_template": str(args.out), "candidate_links": len(template["candidate_links"]), "example_enabled": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
