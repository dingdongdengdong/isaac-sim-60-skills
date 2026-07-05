#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
DEST="${CODEX_SKILLS_DIR:-${CODEX_HOME:-$HOME/.codex}/skills}"
mkdir -p "$DEST"
for skill_dir in "$REPO_ROOT"/skills/*; do
  [ -d "$skill_dir" ] || continue
  skill=$(basename "$skill_dir")
  if [ -e "$DEST/$skill" ]; then
    rm -rf "$DEST/$skill"
  fi
  cp -a "$skill_dir" "$DEST/$skill"
  echo "installed $skill -> $DEST/$skill"
done
echo "Restart Codex to pick up installed skills."
