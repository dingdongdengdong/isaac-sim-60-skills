#!/usr/bin/env python3
from __future__ import annotations
import os
import re
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
QUICK_VALIDATE = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills/.system/skill-creator/scripts/quick_validate.py"

name_re = re.compile(r"^[a-z0-9-]+$")

def fallback_validate(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text()
    if not text.startswith("---\n"):
        raise SystemExit(f"missing YAML frontmatter: {skill_md}")
    end = text.find("\n---", 4)
    if end == -1:
        raise SystemExit(f"unterminated YAML frontmatter: {skill_md}")
    fm = text[4:end]
    fields = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    name = fields.get("name")
    desc = fields.get("description")
    if not name or not name_re.match(name):
        raise SystemExit(f"invalid name in {skill_md}: {name!r}")
    if name != skill_dir.name:
        raise SystemExit(f"name/folder mismatch: {skill_dir.name} vs {name}")
    if not desc:
        raise SystemExit(f"missing description: {skill_md}")
    if not (skill_dir / "agents/openai.yaml").exists():
        raise SystemExit(f"missing agents/openai.yaml: {skill_dir}")
    if "TODO" in text:
        raise SystemExit(f"TODO remains in {skill_md}")

if not SKILLS:
    raise SystemExit("no skills found")

for skill_md in SKILLS:
    skill_dir = skill_md.parent
    print(f"validating {skill_dir.name}")
    if QUICK_VALIDATE.exists():
        subprocess.run([sys.executable, str(QUICK_VALIDATE), str(skill_dir)], check=True)
    else:
        fallback_validate(skill_dir)

# Helper script checks.
subprocess.run(["bash", "-n", str(ROOT / "skills/isaac-sim-60-runtime/scripts/check_isaacsim60_host.sh")], check=True)
subprocess.run([sys.executable, "-m", "py_compile", str(ROOT / "skills/isaac-sim-60-troubleshooting/scripts/summarize_isaacsim60_logs.py")], check=True)
for helper_dir in [
    ROOT / "skills/isaac-sim-viewport-debugger/scripts",
    ROOT / "skills/isaac-sim-60-articulation-builder/scripts",
]:
    if helper_dir.exists():
        for helper in sorted(helper_dir.glob("*.py")):
            subprocess.run([sys.executable, "-m", "py_compile", str(helper)], check=True)


# Articulation status classifier regression checks.
def run_articulation_status_checks() -> None:
    import importlib.util

    inspector_path = ROOT / "skills/isaac-sim-60-articulation-builder/scripts/inspect_usd_articulation.py"
    spec = importlib.util.spec_from_file_location("inspect_usd_articulation", inspector_path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"failed to load {inspector_path}")
    inspector = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inspector)
    cases = [
        ((10, 0, 0, 0, 0), "visual_only"),
        ((10, 5, 0, 0, 0), "rigid_body_not_articulated"),
        ((10, 5, 2, 0, 0), "partial_articulation_missing_root"),
        ((10, 5, 0, 1, 0), "partial_articulation_missing_joints"),
        ((10, 5, 2, 1, 0), "articulated_no_drives"),
        ((10, 5, 2, 1, 1), "controllable_candidate"),
        ((10, 5, 2, 1, 1, 1), "invalid_articulation_relationships"),
    ]
    for args, expected in cases:
        actual = inspector.classify(*args)
        if actual != expected:
            raise SystemExit(f"unexpected articulation status for {args}: {actual} != {expected}")



def run_articulation_template_checks() -> None:
    import importlib.util

    generator_path = ROOT / "skills/isaac-sim-60-articulation-builder/scripts/generate_articulation_map_template.py"
    spec = importlib.util.spec_from_file_location("generate_articulation_map_template", generator_path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"failed to load {generator_path}")
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    cases = [
        (["/World/Robot/base_link", "/World/Robot/arm_link"], "/World/Robot"),
        (["/Robot/base_link", "/Robot/arm_link"], "/Robot"),
        (["/base_link", "/arm_link"], "/"),
        (["/Robot/base_link"], "/Robot"),
        (["/base_link"], "/"),
    ]
    for links, expected in cases:
        actual = generator.common_ancestor(links)
        if actual != expected:
            raise SystemExit(f"unexpected articulation root guess for {links}: {actual} != {expected}")
    root_template = generator.make_template({"candidate_link_prims": ["/base_link", "/arm_link"]})
    if root_template["joint_container"] != "/ArticulationJoints" or root_template["joints"][0]["path"].startswith("//"):
        raise SystemExit(f"bad root-level template paths: {root_template}")

# Minimal functional articulation-builder check when USD Python is available.
def run_articulation_builder_smoke() -> None:
    try:
        from pxr import Usd, UsdGeom, UsdPhysics  # type: ignore
    except Exception as exc:
        print(f"skipping articulation-builder USD smoke test: {exc}")
        return
    scripts = ROOT / "skills/isaac-sim-60-articulation-builder/scripts"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        source = tmp_path / "source.usda"
        stage = Usd.Stage.CreateNew(str(source))
        UsdGeom.Xform.Define(stage, "/World")
        UsdGeom.Xform.Define(stage, "/World/Robot")
        base = UsdGeom.Xform.Define(stage, "/World/Robot/base_link").GetPrim()
        arm = UsdGeom.Xform.Define(stage, "/World/Robot/arm_link").GetPrim()
        UsdPhysics.RigidBodyAPI.Apply(base)
        UsdPhysics.RigidBodyAPI.Apply(arm)
        UsdGeom.Mesh.Define(stage, "/World/Robot/base_link/visual")
        UsdGeom.Mesh.Define(stage, "/World/Robot/arm_link/visual")
        stage.GetRootLayer().Save()

        inspection = tmp_path / "inspection.json"
        subprocess.run([sys.executable, str(scripts / "inspect_usd_articulation.py"), str(source), "--out", str(inspection)], check=True, stdout=subprocess.DEVNULL)
        inspection_data = json.loads(inspection.read_text())
        if inspection_data["status"] != "rigid_body_not_articulated":
            raise SystemExit(f"unexpected pre-scaffold status: {inspection_data['status']}")

        mapping = tmp_path / "map.json"
        subprocess.run([sys.executable, str(scripts / "generate_articulation_map_template.py"), str(inspection), "--out", str(mapping)], check=True, stdout=subprocess.DEVNULL)
        mapping_data = json.loads(mapping.read_text())
        mapping_data["joints"] = [{
            "enabled": True,
            "name": "shoulder_pan",
            "path": "/World/Robot/ArticulationJoints/shoulder_pan",
            "type": "revolute",
            "parent": "/World/Robot/base_link",
            "child": "/World/Robot/arm_link",
            "axis": "Z",
            "limits": {"lower": -1.57, "upper": 1.57},
            "drive": {"type": "angular", "stiffness": 1000, "damping": 100, "max_force": 1000},
        }]
        mapping.write_text(json.dumps(mapping_data, indent=2) + "\n")

        output = tmp_path / "out.usda"
        report = tmp_path / "scaffold_report.json"
        subprocess.run([sys.executable, str(scripts / "author_articulation_scaffold.py"), str(source), str(mapping), "--out", str(output), "--report", str(report)], check=True, stdout=subprocess.DEVNULL)
        output_inspection = tmp_path / "output_inspection.json"
        subprocess.run([sys.executable, str(scripts / "inspect_usd_articulation.py"), str(output), "--out", str(output_inspection)], check=True, stdout=subprocess.DEVNULL)
        output_data = json.loads(output_inspection.read_text())
        if output_data["status"] != "controllable_candidate":
            raise SystemExit(f"unexpected post-scaffold status: {output_data['status']}")
        if output_data["counts"].get("valid_physics_joints") != 1 or output_data["counts"].get("drives") != 1:
            raise SystemExit(f"unexpected post-scaffold counts: {output_data['counts']}")

        # Negative regression: enabled joints with missing body targets must fail authoring.
        bad_mapping = dict(mapping_data)
        bad_joint = dict(cast(dict[str, Any], mapping_data["joints"][0]))
        bad_joint["child"] = "/World/Robot/typo_missing_child"
        bad_mapping["joints"] = [bad_joint]
        bad_mapping_path = tmp_path / "bad_missing_child_map.json"
        bad_mapping_path.write_text(json.dumps(bad_mapping, indent=2) + "\n")
        bad_report = tmp_path / "bad_missing_child_report.json"
        bad_result = subprocess.run([sys.executable, str(scripts / "author_articulation_scaffold.py"), str(source), str(bad_mapping_path), "--out", str(tmp_path / "bad_missing_child.usda"), "--report", str(bad_report)], stdout=subprocess.DEVNULL)
        if bad_result.returncode == 0:
            raise SystemExit("authoring unexpectedly succeeded with a missing child target")
        bad_report_data = json.loads(bad_report.read_text())
        if not bad_report_data.get("failed_enabled_joints"):
            raise SystemExit("missing child target did not create failed_enabled_joints report entry")

        # Negative regression: fixed joints with drives and invalid axes must fail authoring.
        invalid_overrides: list[tuple[str, dict[str, Any]]] = [
            ("fixed_drive", {"type": "fixed", "drive": {"type": "linear", "stiffness": 10}}),
            ("bad_axis", {"axis": "BAD"}),
        ]
        for label, override in invalid_overrides:
            invalid_mapping = dict(mapping_data)
            invalid_joint = dict(cast(dict[str, Any], mapping_data["joints"][0]))
            invalid_joint.update(override)
            invalid_mapping["joints"] = [invalid_joint]
            invalid_mapping_path = tmp_path / f"{label}_map.json"
            invalid_mapping_path.write_text(json.dumps(invalid_mapping, indent=2) + "\n")
            result = subprocess.run([sys.executable, str(scripts / "author_articulation_scaffold.py"), str(source), str(invalid_mapping_path), "--out", str(tmp_path / f"{label}.usda"), "--report", str(tmp_path / f"{label}_report.json")], stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                raise SystemExit(f"authoring unexpectedly succeeded for invalid mapping: {label}")

        # Negative regression: stray DriveAPI on a non-joint prim must not make the asset controllable.
        stray = tmp_path / "stray_drive.usda"
        stray_stage = Usd.Stage.CreateNew(str(stray))
        UsdGeom.Xform.Define(stray_stage, "/World")
        robot = UsdGeom.Xform.Define(stray_stage, "/World/Robot").GetPrim()
        UsdPhysics.ArticulationRootAPI.Apply(robot)
        UsdPhysics.DriveAPI.Apply(robot, "angular")
        stray_base = UsdGeom.Xform.Define(stray_stage, "/World/Robot/base_link").GetPrim()
        stray_arm = UsdGeom.Xform.Define(stray_stage, "/World/Robot/arm_link").GetPrim()
        UsdPhysics.RigidBodyAPI.Apply(stray_base)
        UsdPhysics.RigidBodyAPI.Apply(stray_arm)
        joint = UsdPhysics.RevoluteJoint.Define(stray_stage, "/World/Robot/ArticulationJoints/no_drive_joint")
        joint.CreateBody0Rel().SetTargets([stray_base.GetPath()])
        joint.CreateBody1Rel().SetTargets([stray_arm.GetPath()])
        stray_stage.GetRootLayer().Save()
        stray_inspection = tmp_path / "stray_drive_inspection.json"
        subprocess.run([sys.executable, str(scripts / "inspect_usd_articulation.py"), str(stray), "--out", str(stray_inspection)], check=True, stdout=subprocess.DEVNULL)
        stray_data = json.loads(stray_inspection.read_text())
        if stray_data["status"] != "articulated_no_drives" or stray_data["counts"].get("stray_drives") != 1:
            raise SystemExit(f"stray drive changed controllability status unexpectedly: {stray_data}")

run_articulation_status_checks()
run_articulation_template_checks()
run_articulation_builder_smoke()
print(f"validated {len(SKILLS)} skills")
