
#!/usr/bin/env bash
# Usage: ./tools/ingest-dir.sh [directory]
# Defaults to raw/ if no argument given.
set -euo pipefail
cd "$(dirname "$0")/.."
exec python wiki_runner.py ingest-dir "${1:-raw}"
