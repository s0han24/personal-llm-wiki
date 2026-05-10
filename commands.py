# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

from prompts import ingest_prompt, lint_prompt, query_prompt
from raw_tracker import find_changed, load_state, save_state
from raw_tracker import update_state_for_file
from utils import run_copilot


import sys
from pathlib import Path


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


def cmd_ingest_dir(raw_dir_str: str) -> None:
    raw_dir = Path(raw_dir_str).resolve()
    if not raw_dir.is_dir():
        print(f"ERROR: Not a directory: {raw_dir_str}", file=sys.stderr)
        sys.exit(1)

    state = load_state(raw_dir)
    changed = find_changed(raw_dir, state)

    if not changed:
        print(f"\n{'━'*52}\n  LLM Wiki — INGEST-DIR\n  No changes detected in {raw_dir_str}\n{'━'*52}\n")
        return

    print(f"\n{'━'*52}")
    print(f"  LLM Wiki — INGEST-DIR")
    print(f"  Directory : {raw_dir_str}")
    print(f"  Changed   : {len(changed)} file(s)")
    for f in changed:
        print(f"    • {f.relative_to(raw_dir)}")
    print(f"{'━'*52}\n")

    failed = []
    for source in changed:
        print(f"\n── Ingesting: {source.relative_to(raw_dir)} ──\n")
        prompt = ingest_prompt(source)
        rc = run_copilot(prompt)
        if rc == 0:
            # Only update state for files Copilot processed successfully
            update_state_for_file(raw_dir, source, state)
            save_state(raw_dir, state)  # save after each success so a crash mid-run doesn't lose progress
        else:
            print(f"WARNING: Copilot exited {rc} for {source.name} — state not updated for this file.", file=sys.stderr)
            failed.append(source)

    print(f"\n{'━'*52}")
    print(f"  INGEST-DIR complete")
    print(f"  Ingested : {len(changed) - len(failed)}/{len(changed)}")
    if failed:
        print(f"  Failed   : {len(failed)} (will retry on next run)")
        for f in failed:
            print(f"    • {f.relative_to(raw_dir)}")
    print(f"{'━'*52}\n")

    if failed:
        sys.exit(1)
