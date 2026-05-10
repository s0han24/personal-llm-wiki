# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

from config import AGENTS_MD, WIKI_DIR, WIKI_ROOT
from utils import read


from datetime import date
from pathlib import Path


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
    # TODO: Try reducing LLM calls by using shell commands instead
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
