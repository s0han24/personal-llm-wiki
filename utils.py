from pathlib import Path
import subprocess
from config import WIKI_ROOT


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
