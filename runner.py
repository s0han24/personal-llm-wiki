#!/usr/bin/env python3
"""
wiki_runner.py — LLM Wiki runner using the GitHub Copilot CLI (-p mode).

Usage:
    python wiki_runner.py ingest <path-to-source-file>
    python wiki_runner.py query "<question>"
    python wiki_runner.py lint

Requires:
    - GitHub Copilot CLI installed (npm install -g @github/copilot)
    - COPILOT_GITHUB_TOKEN set in environment (PAT with Copilot Requests permission)

The script builds a detailed prompt and calls:
    copilot -p "PROMPT" --allow-tool=write --allow-tool='shell(find:*)' --no-ask-user

Copilot handles all file I/O directly via its built-in write and shell tools.
AGENTS.md is injected into the prompt so Copilot knows the wiki schema.
"""

import subprocess
import sys
import os
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WIKI_ROOT = Path(__file__).parent.resolve()
AGENTS_MD  = WIKI_ROOT / "AGENTS.md"
WIKI_DIR   = WIKI_ROOT / "wiki"
RAW_DIR    = WIKI_ROOT / "raw"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else f"(file not found: {path})"


def run_copilot(prompt: str) -> int:
    """
    Invoke the Copilot CLI in programmatic mode.
    Streams stdout/stderr live so you see Copilot's work as it happens.
    """
    cmd = [
        "copilot",
        "-p", prompt,
        "--allow-tool=write",           # lets Copilot write/edit files
        "--allow-tool=shell(find:*)",   # lets Copilot find/list files
        "--allow-tool=shell(cat:*)",    # lets Copilot read files for context
        "--allow-tool=shell(grep:*)",   # lets Copilot search for links/refs
        "--allow-tool=shell(tail:*)",   # lets Copilot read the log tail
        "--no-ask-user",                # non-interactive; required for CI
    ]
    result = subprocess.run(cmd, cwd=str(WIKI_ROOT))
    return result.returncode


# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def ingest_prompt(source_path: Path) -> str:
    today         = date.today().isoformat()
    agents        = read(AGENTS_MD)
    index         = read(WIKI_DIR / "index.md")
    overview      = read(WIKI_DIR / "overview.md")
    log_tail      = "\n".join(read(WIKI_DIR / "log.md").splitlines()[-20:])
    source_content = read(source_path)
    basename      = source_path.name
    try:
        rel = source_path.relative_to(WIKI_ROOT)
    except ValueError:
        rel = source_path

    return f"""You are maintaining a research wiki. Follow the schema and conventions in the AGENTS.md section below exactly.

Today's date: {today}
Wiki root: {WIKI_ROOT}

=== AGENTS.md (your schema) ===
{agents}

=== wiki/index.md ===
{index}

=== wiki/overview.md ===
{overview}

=== wiki/log.md (last 20 lines) ===
{log_tail}

=== SOURCE TO INGEST ===
Filename : {basename}
Repo path: {rel}

{source_content}

=== END SOURCE ===

Now perform the INGEST operation defined in AGENTS.md. Work through all 7 steps:
1. Write wiki/sources/<slug>.md (source summary page)
2. Create or update entity pages in wiki/entities/
3. Create or update concept pages in wiki/concepts/
4. Update wiki/overview.md
5. Update wiki/index.md
6. Append the ingest entry to wiki/log.md (starting with ## [{today}] ingest | {basename})
Do all file writes now. Use the write tool for new/updated pages and shell tools to inspect existing wiki files as needed."""


def query_prompt(question: str) -> str:
    today    = date.today().isoformat()
    agents   = read(AGENTS_MD)
    index    = read(WIKI_DIR / "index.md")
    overview = read(WIKI_DIR / "overview.md")

    return f"""You are maintaining a research wiki. Follow the schema and conventions in the AGENTS.md section below exactly.

Today's date: {today}
Wiki root: {WIKI_ROOT}

=== AGENTS.md (your schema) ===
{agents}

=== wiki/index.md ===
{index}

=== wiki/overview.md ===
{overview}

=== QUESTION ===
{question}

Perform the QUERY operation defined in AGENTS.md:
1. Use shell(cat) or shell(find) to read relevant wiki pages identified from the index
2. Synthesise a clear answer with [[wiki link]] citations
3. Print the answer to stdout
4. If the answer is valuable enough to keep, write it to wiki/analyses/<slug>.md and update wiki/index.md and wiki/log.md"""


def lint_prompt() -> str:
    today    = date.today().isoformat()
    agents   = read(AGENTS_MD)
    index    = read(WIKI_DIR / "index.md")
    log_tail = "\n".join(read(WIKI_DIR / "log.md").splitlines()[-30:])

    return f"""You are maintaining a research wiki. Follow the schema and conventions in the AGENTS.md section below exactly.

Today's date: {today}
Wiki root: {WIKI_ROOT}

=== AGENTS.md (your schema) ===
{agents}

=== wiki/index.md ===
{index}

=== wiki/log.md (last 30 lines) ===
{log_tail}

Perform the LINT operation defined in AGENTS.md:
1. Use shell(find) to list all wiki pages
2. Use shell(cat) and shell(grep) to check for the 7 issues in the LINT checklist
3. Print a lint report to stdout
4. Fix any clear issues (orphan links, missing index entries, stub markers)
5. Append a lint entry to wiki/log.md (## [{today}] lint ...)"""


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_ingest(source_path_str: str) -> None:
    source = Path(source_path_str).resolve()
    if not source.exists():
        print(f"ERROR: Source file not found: {source_path_str}", file=sys.stderr)
        sys.exit(1)
    print(f"\n{'━'*52}\n  LLM Wiki — INGEST: {source.name}\n{'━'*52}\n")
    prompt = ingest_prompt(source)
    sys.exit(run_copilot(prompt))


def cmd_query(question: str) -> None:
    print(f"\n{'━'*52}\n  LLM Wiki — QUERY\n  {question}\n{'━'*52}\n")
    prompt = query_prompt(question)
    sys.exit(run_copilot(prompt))


def cmd_lint() -> None:
    print(f"\n{'━'*52}\n  LLM Wiki — LINT\n{'━'*52}\n")
    prompt = lint_prompt()
    sys.exit(run_copilot(prompt))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python wiki_runner.py ingest <path-to-source>")
        print("  python wiki_runner.py query \"<question>\"")
        print("  python wiki_runner.py lint")
        sys.exit(0)

    match args[0].lower():
        case "ingest":
            if len(args) < 2:
                print("ERROR: ingest requires a source file path.", file=sys.stderr)
                sys.exit(1)
            cmd_ingest(args[1])
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
