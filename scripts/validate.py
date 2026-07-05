#!/usr/bin/env python3
from __future__ import annotations
import os
import re
import subprocess
import sys
from pathlib import Path

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
print(f"validated {len(SKILLS)} skills")
