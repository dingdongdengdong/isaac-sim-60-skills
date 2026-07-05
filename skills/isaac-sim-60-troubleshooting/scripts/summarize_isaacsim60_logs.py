#!/usr/bin/env python3
"""Summarize Isaac Sim 6.0 logs without modifying them."""
from __future__ import annotations
import re
import sys
from pathlib import Path

PATTERNS = {
    "errors": re.compile(r"\b(ERROR|CRITICAL|Traceback|Exception|Segmentation fault|crash)\b", re.I),
    "warnings": re.compile(r"\b(WARN|WARNING)\b", re.I),
    "simready": re.compile(r"SimReady|Loading .*USD|echo_full_robot_arm_hand", re.I),
    "ros": re.compile(r"ROS|ros2|/leader/joint_commands|/follower/joint_states|ROS_DOMAIN_ID", re.I),
    "screenshot": re.compile(r"screenshot|ScreenCapture|capture", re.I),
    "docker_pull": re.compile(r"pull|layer|sha256|download|extract", re.I),
    "physics": re.compile(r"PhysX|physics|contact|joint|articulation|grasp|collision", re.I),
}

def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: summarize_isaacsim60_logs.py LOG [LOG ...]", file=sys.stderr)
        return 2
    for arg in argv[1:]:
        p = Path(arg)
        print(f"== {p} ==")
        if not p.exists():
            print("missing")
            continue
        lines = p.read_text(errors="replace").splitlines()
        print(f"lines: {len(lines)} bytes: {p.stat().st_size}")
        for name, pattern in PATTERNS.items():
            hits = [(i + 1, line) for i, line in enumerate(lines) if pattern.search(line)]
            print(f"{name}: {len(hits)}")
            for lineno, line in hits[:8]:
                print(f"  {lineno}: {line[:220]}")
            if len(hits) > 8:
                print(f"  ... {len(hits) - 8} more")
        print()
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
