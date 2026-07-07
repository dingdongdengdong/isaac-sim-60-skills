#!/usr/bin/env python3
"""Author a non-destructive Isaac Sim articulation scaffold from explicit mapping JSON."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

JOINT_TYPES = {"revolute", "prismatic", "fixed", "spherical"}
DRIVE_TYPES = {"angular", "linear"}
JOINT_DRIVE_TYPES = {"revolute": "angular", "prismatic": "linear"}
AXES = {"X", "Y", "Z"}


def require_pxr():
    try:
        from pxr import Sdf, Usd, UsdPhysics
    except Exception as exc:  # pragma: no cover - depends on Isaac/USD runtime
        raise SystemExit(f"pxr/USD Python modules are required: {exc}") from exc
    return Sdf, Usd, UsdPhysics


def has_schema(prim: Any, schema_name: str) -> bool:
    try:
        if schema_name in prim.GetAppliedSchemas():
            return True
    except Exception:
        pass
    try:
        from pxr import UsdPhysics

        schema = getattr(UsdPhysics, schema_name, None)
        if schema is not None and prim.HasAPI(schema):
            return True
    except Exception:
        pass
    return False


def as_path(value: str, field: str):
    from pxr import Sdf

    if not value:
        raise ValueError(f"missing {field}")
    path = Sdf.Path(value)
    if not path.IsAbsolutePath():
        raise ValueError(f"{field} must be an absolute prim path: {value}")
    return path


def require_rigid_body_target(stage: Any, value: str, field: str):
    path = as_path(value, field)
    prim = stage.GetPrimAtPath(path)
    if not prim or not prim.IsValid():
        raise ValueError(f"{field} target does not exist on composed stage: {value}")
    if not has_schema(prim, "RigidBodyAPI"):
        raise ValueError(f"{field} target must have RigidBodyAPI: {value}")
    return path


def define_joint(UsdPhysics: Any, stage: Any, joint_type: str, joint_path: str):
    if joint_type == "revolute":
        return UsdPhysics.RevoluteJoint.Define(stage, joint_path)
    if joint_type == "prismatic":
        return UsdPhysics.PrismaticJoint.Define(stage, joint_path)
    if joint_type == "fixed":
        return UsdPhysics.FixedJoint.Define(stage, joint_path)
    if joint_type == "spherical":
        return UsdPhysics.SphericalJoint.Define(stage, joint_path)
    raise ValueError(f"unsupported joint type: {joint_type}")


def set_if_supported(schema_obj: Any, method_name: str, value: Any) -> bool:
    method = getattr(schema_obj, method_name, None)
    if method is None:
        return False
    method(value)
    return True


def validate_drive(joint_type: str, drive_spec: dict[str, Any]) -> str:
    if not drive_spec:
        return ""
    expected = JOINT_DRIVE_TYPES.get(joint_type)
    if expected is None:
        raise ValueError(f"{joint_type} joints must not define drives in this scaffold; use explicit movable revolute/prismatic joints")
    drive_type = str(drive_spec.get("type", expected)).lower()
    if drive_type not in DRIVE_TYPES:
        raise ValueError(f"unsupported drive type: {drive_type!r}")
    if drive_type != expected:
        raise ValueError(f"{joint_type} joint drive must be {expected!r}, got {drive_type!r}")
    return drive_type


def author(source_usd: Path, mapping_path: Path, out_path: Path, report_path: Path) -> dict[str, Any]:
    Sdf, Usd, UsdPhysics = require_pxr()
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    source_abs = source_usd.resolve()
    if not source_abs.exists():
        raise SystemExit(f"source USD does not exist: {source_usd}")

    stage = Usd.Stage.CreateNew(str(out_path))
    stage.GetRootLayer().subLayerPaths.append(str(source_abs))

    report: dict[str, Any] = {
        "script": Path(__file__).name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_usd": str(source_abs),
        "mapping_json": str(mapping_path),
        "output_usd": str(out_path),
        "authored_articulation_roots": [],
        "authored_joints": [],
        "skipped_joints": [],
        "failed_enabled_joints": [],
        "warnings": [],
    }

    root_path = mapping.get("articulation_root")
    if not root_path:
        raise SystemExit("mapping must define articulation_root")
    root_prim = stage.OverridePrim(as_path(root_path, "articulation_root"))
    UsdPhysics.ArticulationRootAPI.Apply(root_prim)
    report["authored_articulation_roots"].append(str(root_prim.GetPath()))

    joint_container = mapping.get("joint_container")
    if joint_container:
        stage.DefinePrim(as_path(joint_container, "joint_container"), "Scope")

    for index, joint_spec in enumerate(mapping.get("joints", [])):
        if joint_spec.get("enabled") is False:
            report["skipped_joints"].append({"index": index, "reason": "enabled=false", "name": joint_spec.get("name")})
            continue
        try:
            joint_type = str(joint_spec.get("type", "")).lower()
            if joint_type not in JOINT_TYPES:
                raise ValueError(f"unsupported joint type: {joint_type!r}")
            name = joint_spec.get("name") or f"joint_{index}"
            joint_path = joint_spec.get("path") or f"{joint_container or root_path + '/ArticulationJoints'}/{name}"
            parent = require_rigid_body_target(stage, joint_spec.get("parent", ""), "parent")
            child = require_rigid_body_target(stage, joint_spec.get("child", ""), "child")
            axis = joint_spec.get("axis")
            axis_value = str(axis).upper() if axis else ""
            if axis_value and axis_value not in AXES:
                raise ValueError(f"axis must be one of X, Y, or Z, got {axis!r}")
            drive_spec = joint_spec.get("drive") or {}
            drive_type = validate_drive(joint_type, drive_spec)

            joint = define_joint(UsdPhysics, stage, joint_type, str(as_path(joint_path, "joint path")))
            joint.CreateBody0Rel().SetTargets([parent])
            joint.CreateBody1Rel().SetTargets([child])

            if axis_value and hasattr(joint, "CreateAxisAttr"):
                joint.CreateAxisAttr(axis_value)
            limits = joint_spec.get("limits") or {}
            if "lower" in limits and hasattr(joint, "CreateLowerLimitAttr"):
                joint.CreateLowerLimitAttr(float(limits["lower"]))
            if "upper" in limits and hasattr(joint, "CreateUpperLimitAttr"):
                joint.CreateUpperLimitAttr(float(limits["upper"]))

            drive_report = None
            if drive_spec:
                drive = UsdPhysics.DriveAPI.Apply(joint.GetPrim(), drive_type)
                if "stiffness" in drive_spec:
                    drive.CreateStiffnessAttr(float(drive_spec["stiffness"]))
                if "damping" in drive_spec:
                    drive.CreateDampingAttr(float(drive_spec["damping"]))
                if "max_force" in drive_spec:
                    set_if_supported(drive, "CreateMaxForceAttr", float(drive_spec["max_force"]))
                drive_report = {"type": drive_type, "authored": True}

            report["authored_joints"].append({
                "name": name,
                "path": str(joint.GetPath()),
                "type": joint_type,
                "parent": str(parent),
                "child": str(child),
                "drive": drive_report,
            })
        except Exception as exc:
            failure = {"index": index, "name": joint_spec.get("name"), "reason": str(exc)}
            report["skipped_joints"].append(failure)
            report["failed_enabled_joints"].append(failure)

    if not report["authored_joints"]:
        report["warnings"].append("No enabled joints were authored; output only applies articulation root and sublayers the source.")
    if report["failed_enabled_joints"]:
        report["warnings"].append("One or more enabled joints failed validation; command exits nonzero.")
    stage.GetRootLayer().Save()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Author articulation scaffold into a separate USD layer/stage.")
    parser.add_argument("source_usd", type=Path, help="source USD path; never modified")
    parser.add_argument("mapping_json", type=Path, help="explicit articulation mapping JSON")
    parser.add_argument("--out", type=Path, required=True, help="output USD path to write")
    parser.add_argument("--report", type=Path, required=True, help="report JSON path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    report = author(args.source_usd, args.mapping_json, args.out, args.report)
    print(json.dumps(report, indent=2))
    return 1 if report["failed_enabled_joints"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
