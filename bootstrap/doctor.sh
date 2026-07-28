#!/usr/bin/env bash
set -e
check(){ command -v "$1" >/dev/null && echo "✓ $1" || echo "✗ $1"; }
echo "=== RIF Doctor ==="
for c in docker git python3 uv gh; do
    check "$c"
done
