from pathlib import Path

STATE_FILENAME = ".raw_state.json"  # lives inside raw/, gitignored with it

def state_path(raw_dir: Path) -> Path:
    return raw_dir / STATE_FILENAME


# ---------------------------------------------------------------------------
# Raw state tracking
# ---------------------------------------------------------------------------




def load_state(raw_dir: Path) -> dict:
    """Return {relative_path_str: {mtime, size}} or {} if no state file yet."""
    p = state_path(raw_dir)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_state(raw_dir: Path, state: dict) -> None:
    p = state_path(raw_dir)
    p.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def file_record(path: Path) -> dict:
    """Stat a file and return its tracking record."""
    st = path.stat()
    return {"mtime": st.st_mtime, "size": st.st_size}


def find_changed(raw_dir: Path, state: dict) -> list[Path]:
    """
    Walk raw_dir and return files whose mtime or size differs from state,
    plus files not in state at all. Skips the state file itself.
    """
    changed = []
    for path in sorted(raw_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.name == STATE_FILENAME:
            continue
        key = str(path.relative_to(raw_dir))
        record = file_record(path)
        existing = state.get(key)
        if existing is None or existing["mtime"] != record["mtime"] or existing["size"] != record["size"]:
            changed.append(path)
    return changed


def update_state_for_file(raw_dir: Path, path: Path, state: dict) -> dict:
    """Mark a single file as current in the state dict (does not save to disk)."""
    key = str(path.relative_to(raw_dir))
    state[key] = file_record(path)
    return state
