#!/usr/bin/env python3
"""
wiki_runner.py — LLM Wiki runner using the GitHub Copilot CLI (-p mode).

Usage:
    python wiki_runner.py ingest <path-to-source>
    python wiki_runner.py ingest-dir [<directory>]
    python wiki_runner.py query "<question>"
    python wiki_runner.py lint

ingest       — ingest a single file (one Copilot session)
ingest-dir   — diff raw/ against raw/.raw_state.json, ingest each changed
               file in its own Copilot session, update the state file.
               Defaults to raw/ if no directory argument is given.

Requires:
    - GitHub Copilot CLI installed: npm install -g @github/copilot
    - COPILOT_GITHUB_TOKEN set in environment
"""

import sys
import os

from commands import cmd_ingest, cmd_ingest_dir, cmd_lint, cmd_query
from config import RAW_DIR

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python wiki_runner.py ingest <path-to-source>")
        print("  python wiki_runner.py ingest-dir [<directory>]   (default: raw/)")
        print("  python wiki_runner.py query \"<question>\"")
        print("  python wiki_runner.py lint")
        sys.exit(0)

    match args[0].lower():
        case "ingest":
            if len(args) < 2:
                print("ERROR: ingest requires a source file path.", file=sys.stderr)
                sys.exit(1)
            cmd_ingest(args[1])
        case "ingest-dir":
            raw_dir = args[1] if len(args) > 1 else str(RAW_DIR)
            cmd_ingest_dir(raw_dir)
        case "query":
            if len(args) < 2:
                print("ERROR: query requires a question string.", file=sys.stderr)
                sys.exit(1)
            cmd_query(" ".join(args[1:]))
        case "lint":
            cmd_lint()
        case _:
            print(f"ERROR: Unknown command '{args[0]}'", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
