# LLM Wiki — Agent Schema

This file governs how GitHub Copilot (or any LLM agent) maintains this wiki.
Read this file at the start of every session before touching any wiki files.

---

## What this wiki is

A persistent, compounding knowledge base for research. You (the LLM) write and maintain it.
The human curates sources, asks questions, and directs the analysis. You do the bookkeeping.

This is **not RAG**. You do not retrieve from raw sources at query time and regenerate answers.
You compile knowledge into the wiki once, keep it current, and answer from the wiki.

---

## Directory layout

```
llm-wiki/
├── AGENTS.md          ← this file; read first every session
├── raw/               ← immutable source documents (human adds these, you read them)
│   ├── papers/
│   ├── articles/
│   ├── notes/
│   └── assets/        ← downloaded images referenced in sources
├── wiki/              ← everything you write lives here
│   ├── index.md       ← master catalog of all wiki pages (update on every ingest)
│   ├── log.md         ← append-only chronological record of all operations
│   ├── overview.md    ← high-level synthesis of the entire knowledge base
│   ├── sources/       ← one summary page per raw source you have ingested
│   ├── entities/      ← pages for people, institutions, datasets, models, systems
│   ├── concepts/      ← pages for ideas, methods, theories, terms
│   └── analyses/      ← comparisons, syntheses, questions-turned-pages
└── tools/
    ├── ingest.sh      ← CLI helper: primes Copilot for an ingest session
    └── query.sh       ← CLI helper: primes Copilot for a query session
```

---

## Page conventions

### Frontmatter (YAML, every wiki page)

```yaml
---
title: "Page Title"
type: source | entity | concept | analysis | overview
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of raw source filenames this page draws from]
tags: [freeform tags]
---
```

### Cross-references

Always use Obsidian wiki-link syntax: `[[Page Name]]`.
Never use relative file paths. Obsidian resolves links by page title.

### Contradictions

When new information contradicts an existing claim, do **not** silently overwrite it.
Mark it explicitly:

```
> ⚠️ **Contradiction**: [Source A] claims X. [[Source B Summary]] claims Y. Unresolved as of YYYY-MM-DD.
```

Then flag it in `log.md` under the current entry.

### Stubs

If a concept or entity is referenced but doesn't have its own page yet, create a minimal stub:

```yaml
---
title: "Term"
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
tags: [stub]
---
# Term
*Stub — mentioned in [[Page]] but not yet fully described.*
```

---

## Operations

### INGEST — adding a new source

Triggered when the human drops a file into `raw/` and asks you to process it.

**Step 1 — Read**
Read the source document in full. If it contains image references, note them and offer to examine key images separately.

**Step 2 — Discuss**
Before writing anything, briefly summarize key takeaways and ask the human what to emphasize or deprioritize. Keep this exchange short (2–4 turns max unless the human wants to go deeper).

**Step 3 — Write source summary**
Create `wiki/sources/<slug>.md`. Include:
- Full citation (authors, title, year, venue/URL)
- 3–5 sentence abstract in your own words
- Key claims (bulleted, each 1–2 sentences)
- Methodology (if a paper): what they did, what data, what evaluation
- Limitations and caveats
- Open questions raised by this source
- Links to all relevant `[[entity]]` and `[[concept]]` pages

**Step 4 — Update entity and concept pages**
For every person, institution, model, dataset, method, or concept the source touches:
- If the page exists: add a new section or update existing content, note the new source
- If it doesn't exist: create it (stub is fine if time is short; full page if central)
- Always add a backlink to `[[<source slug>]]`

**Step 5 — Update overview.md**
Revise the synthesis to reflect what this source adds, changes, or complicates.
If the source meaningfully shifts the picture, say so explicitly.

**Step 6 — Update index.md**
Add a row for the new source summary page and any new entity/concept pages created.

**Step 7 — Append to log.md**
```
## [YYYY-MM-DD] ingest | <Source Title>
- Summary: wiki/sources/<slug>.md
- Pages updated: [[Page1]], [[Page2]], ...
- Pages created: [[NewPage1]], ...
- Contradictions flagged: none / <description>
- Notes: <anything unusual>
```

---

### QUERY — answering a question

**Step 1** — Read `wiki/index.md` to find relevant pages.
**Step 2** — Read those pages (and any pages they link to that seem relevant).
**Step 3** — Synthesize an answer with citations to wiki pages (not raw sources directly).
**Step 4** — Ask the human: *"Should I file this as an analysis page?"*
**Step 5** — If yes, create `wiki/analyses/<slug>.md` and update `index.md` and `log.md`.

Output formats available — ask or infer from context:
- Default: markdown prose with `[[wiki links]]` for citations
- Table: for comparisons
- Marp slide deck: add `marp: true` to frontmatter, use `---` slide breaks
- List of open questions: useful for scoping next ingest targets

---

### LINT — wiki health check

Run periodically or when asked. Check for:

1. **Contradictions** — scan for `⚠️ Contradiction` markers; report which are unresolved
2. **Orphan pages** — pages with no inbound links; suggest merging or linking
3. **Stubs** — pages tagged `stub`; prioritize which to flesh out
4. **Stale claims** — claims sourced only from old documents that newer sources may supersede
5. **Missing pages** — concepts mentioned inline but lacking their own page
6. **Index gaps** — pages that exist on disk but aren't listed in `index.md`
7. **Log consistency** — check that recent ingests are all recorded

Output a lint report, then ask the human which issues to fix now.
Append a lint entry to `log.md`:
```
## [YYYY-MM-DD] lint
- Orphans: N
- Stubs: N
- Contradictions unresolved: N
- Action taken: <summary>
```

---

## Working with Copilot specifically

### In VS Code (Copilot Chat / Edits)

- Open the wiki folder as your VS Code workspace root so Copilot has full file access.
- For ingest: open the raw source file alongside the relevant wiki pages, then prompt Copilot in Edit mode.
- Use `#file:AGENTS.md` at the start of any Copilot Chat prompt to anchor it to this schema.
- Use `#codebase` to let Copilot search across the wiki during queries.
- Copilot Edits is preferred over Chat for multi-file operations (updating 5–15 pages at once).

### In the terminal (gh copilot / copilot CLI)

- Use `ingest.sh` and `query.sh` to pre-compose prompts with full context injected.
- `gh copilot suggest` is useful for one-shot tasks (linting, log formatting).
- `gh copilot explain` can help orient you to a wiki page or source you haven't read.

---

## Style rules

- Write in clear, precise prose. Avoid bullet-point-only pages — use prose with supporting bullets.
- Keep entity and concept pages factual and neutral. Save interpretation for `analyses/`.
- Every claim on a wiki page should trace back to at least one source page via `[[link]]`.
- Do not delete content — mark it superseded if needed, but preserve the history inline.
- Page titles are Title Case. File slugs are `lowercase-with-hyphens`.
- Dates are always ISO 8601: `YYYY-MM-DD`.
