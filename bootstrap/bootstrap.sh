#!/usr/bin/env bash
set -euo pipefail
echo "Bootstrapping RIF Developer Platform..."
for s in docker python ai security; do
    f="$(dirname "$0")/install/${s}.sh"
    [ -f "$f" ] && bash "$f"
done
echo "Bootstrap complete."
