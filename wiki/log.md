---
title: "Wiki Log"
type: log
---

# Wiki Log

Append-only chronological record of all operations.
Each entry starts with `## [YYYY-MM-DD]` for easy grep filtering.

Usage examples:
```bash
# Last 5 entries
grep "^## \[" wiki/log.md | tail -5

# All ingests
grep "^## \[" wiki/log.md | grep "ingest"

# All lint passes
grep "^## \[" wiki/log.md | grep "lint"
```

---

## [YYYY-MM-DD] init
- Wiki initialized with AGENTS.md schema, index.md, log.md, overview.md
- Raw source directories created: raw/papers, raw/articles, raw/notes, raw/assets
- Wiki directories created: wiki/sources, wiki/entities, wiki/concepts, wiki/analyses
- Notes: ready for first ingest
