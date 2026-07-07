#!/usr/bin/env python3
"""Inspect a USD for Isaac Sim articulation controllability evidence."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

JOINT_TYPE_NAMES = {
    "PhysicsJoint",
    "PhysicsFixedJoint",
    "PhysicsRevoluteJoint",
    "PhysicsPrismaticJoint",
    "PhysicsSphericalJoint",
    "PhysicsDistanceJoint",
}
MOVABLE_DRIVE_JOINT_TYPES = {"PhysicsRevoluteJoint", "PhysicsPrismaticJoint"}


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


def is_physics_joint_type(type_name: str) -> bool:
    return type_name in JOINT_TYPE_NAMES or (type_name.endswith("Joint") and type_name.startswith("Physics"))


def relationship_targets(prim: Any, rel_name: str) -> list[str]:
    rel = prim.GetRelationship(rel_name)
    if not rel:
        return []
    return [str(target) for target in rel.GetTargets()]


def target_status(stage: Any, target_path: str) -> dict[str, Any]:
    prim = stage.GetPrimAtPath(target_path)
    exists = bool(prim and prim.IsValid())
    return {
        "path": target_path,
        "exists": exists,
        "rigid_body": bool(exists and has_schema(prim, "RigidBodyAPI")),
    }


def classify(meshes: int, rigid_bodies: int, joints: int, roots: int, drives: int, invalid_joint_relationships: int = 0) -> str:
    if meshes > 0 and rigid_bodies == 0 and joints == 0 and roots == 0 and invalid_joint_relationships == 0:
        return "visual_only"
    if invalid_joint_relationships > 0:
        return "invalid_articulation_relationships"
    if joints > 0 and roots == 0:
        return "partial_articulation_missing_root"
    if roots > 0 and joints == 0:
        return "partial_articulation_missing_joints"
    if rigid_bodies > 0 and joints == 0 and roots == 0:
        return "rigid_body_not_articulated"
    if joints > 0 and roots > 0 and drives == 0:
        return "articulated_no_drives"
    if joints > 0 and roots > 0 and drives > 0:
        return "controllable_candidate"
    return "no_controllability_evidence"


def inspect_usd(path: Path) -> dict[str, Any]:
    try:
        from pxr import Usd, UsdGeom
    except Exception as exc:  # pragma: no cover - depends on Isaac/USD runtime
        raise SystemExit(f"pxr/USD Python modules are required: {exc}") from exc

    stage = Usd.Stage.Open(str(path))
    if stage is None:
        raise SystemExit(f"failed to open USD stage: {path}")

    meshes: list[str] = []
    rigid_bodies: list[str] = []
    joints: list[dict[str, Any]] = []
    valid_joints: list[dict[str, Any]] = []
    invalid_joint_relationships: list[dict[str, Any]] = []
    articulation_roots: list[str] = []
    drives: list[dict[str, str]] = []
    stray_drives: list[dict[str, str]] = []

    for prim in stage.Traverse():
        prim_path = str(prim.GetPath())
        type_name = prim.GetTypeName()
        if prim.IsA(UsdGeom.Mesh) or type_name == "Mesh":
            meshes.append(prim_path)
        if has_schema(prim, "RigidBodyAPI"):
            rigid_bodies.append(prim_path)
        if has_schema(prim, "ArticulationRootAPI"):
            articulation_roots.append(prim_path)

        is_joint = is_physics_joint_type(type_name)
        joint_record: dict[str, Any] | None = None
        if is_joint:
            body0 = relationship_targets(prim, "physics:body0")
            body1 = relationship_targets(prim, "physics:body1")
            body_targets = [target_status(stage, target) for target in [*body0, *body1]]
            relationship_valid = bool(body0 and body1 and all(target["exists"] and target["rigid_body"] for target in body_targets))
            joint_record = {
                "path": prim_path,
                "type": type_name,
                "body0": body0,
                "body1": body1,
                "body_targets": body_targets,
                "valid_body_targets": relationship_valid,
            }
            joints.append(joint_record)
            if relationship_valid:
                valid_joints.append(joint_record)
            else:
                invalid_joint_relationships.append(joint_record)

        drive_schemas = [schema for schema in prim.GetAppliedSchemas() if schema.startswith("PhysicsDriveAPI")]
        for schema in drive_schemas:
            drive_record = {"path": prim_path, "schema": schema}
            if is_joint and joint_record and joint_record["valid_body_targets"] and type_name in MOVABLE_DRIVE_JOINT_TYPES:
                drives.append(drive_record)
            else:
                stray_drives.append(drive_record)

    status = classify(
        len(meshes),
        len(rigid_bodies),
        len(valid_joints),
        len(articulation_roots),
        len(drives),
        len(invalid_joint_relationships),
    )
    warnings: list[str] = []
    if status == "rigid_body_not_articulated":
        warnings.append("Rigid bodies exist, but physics joints and articulation root are missing.")
    if status == "invalid_articulation_relationships":
        warnings.append("One or more physics joints have missing or non-rigid body targets; do not treat this as controllable.")
    if stray_drives:
        warnings.append("Drive APIs not attached to valid movable joint prims were ignored for controllability classification.")
    if status in {
        "visual_only",
        "rigid_body_not_articulated",
        "partial_articulation_missing_root",
        "partial_articulation_missing_joints",
        "invalid_articulation_relationships",
    }:
        warnings.append("Do not bind ROS/LeRobot or tune drives until valid articulation structure exists.")

    return {
        "script": Path(__file__).name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_usd": str(path),
        "counts": {
            "meshes": len(meshes),
            "rigid_bodies": len(rigid_bodies),
            "physics_joints": len(joints),
            "valid_physics_joints": len(valid_joints),
            "invalid_joint_relationships": len(invalid_joint_relationships),
            "articulation_roots": len(articulation_roots),
            "drives": len(drives),
            "stray_drives": len(stray_drives),
        },
        "status": status,
        "mesh_prims": meshes,
        "rigid_body_prims": rigid_bodies,
        "physics_joints": joints,
        "valid_physics_joints": valid_joints,
        "invalid_joint_relationships": invalid_joint_relationships,
        "articulation_roots": articulation_roots,
        "drives": drives,
        "stray_drives": stray_drives,
        "candidate_link_prims": rigid_bodies,
        "warnings": warnings,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect USD articulation controllability evidence.")
    parser.add_argument("usd", type=Path, help="source USD path")
    parser.add_argument("--out", type=Path, help="write JSON report to this path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report = inspect_usd(args.usd)
    text = json.dumps(report, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
