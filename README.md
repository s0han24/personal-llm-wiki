# LLM Wiki

A personal research knowledge base maintained by GitHub Copilot.
Based on the [LLM Wiki pattern](https://gist.github.com/).

---

## Setup

### 1. Clone / open in Obsidian

Open this folder as an Obsidian vault. Recommended plugins:
- **Dataview** — queries over page frontmatter
- **Obsidian Web Clipper** — clips articles to markdown (install in browser)
- **Marp for Obsidian** — render slide decks from wiki pages

In Obsidian Settings → Files and links:
- Set **Attachment folder path** to `raw/assets`
- Bind "Download attachments for current file" to a hotkey (e.g. `Ctrl+Shift+D`)

### 2. Open in VS Code

Open this same folder as a VS Code workspace. Copilot will have access to all files.

For Copilot Chat, always start your session with:
```
#file:AGENTS.md — read this first, it's my wiki schema.
```

For multi-file edits (ingest, updating 10+ pages), use **Copilot Edits** mode.

### 3. Make the CLI tools executable

```bash
chmod +x tools/ingest.sh tools/query.sh tools/lint.sh
```

Make sure `gh` CLI is installed and authenticated:
```bash
gh auth status
gh extension install github/gh-copilot
```

---

## Daily workflow

### Adding a source

1. Drop the file into `raw/papers/`, `raw/articles/`, or `raw/notes/`
2. **In VS Code (preferred for multi-file edits):**
   Open Copilot Edits, add `AGENTS.md` and the source file to context, then:
   ```
   Ingest raw/papers/my-paper.md into the wiki following the INGEST operation in AGENTS.md.
   ```
3. **Or in terminal:**
   ```bash
   ./tools/ingest.sh raw/papers/my-paper.md
   ```

### Asking a question

**In VS Code Copilot Chat:**
```
#file:AGENTS.md #codebase
Question: What do the papers say about X?
```

**In terminal:**
```bash
./tools/query.sh "What do the papers say about X?"
```

### Health check

```bash
./tools/lint.sh
# or in VS Code: ask Copilot to run a lint pass per AGENTS.md
```

---

## Directory layout

```
llm-wiki/
├── AGENTS.md              ← Copilot's schema; read first every session
├── README.md              ← this file
├── raw/                   ← your source documents (immutable)
│   ├── papers/
│   ├── articles/
│   ├── notes/
│   └── assets/
├── wiki/                  ← Copilot writes everything here
│   ├── index.md           ← master page catalog
│   ├── log.md             ← append-only operation log
│   ├── overview.md        ← living synthesis
│   ├── sources/           ← one page per ingested source
│   ├── entities/          ← people, models, datasets, institutions
│   ├── concepts/          ← ideas, methods, theories
│   └── analyses/          ← comparisons, syntheses, filed Q&As
└── tools/
    ├── ingest.sh
    ├── query.sh
    └── lint.sh
```

---

## Tips

- **Obsidian graph view** (`Ctrl+G`) shows what's connected. Orphan nodes = lint targets.
- **File good Q&A answers**: after a useful query response, ask Copilot to save it to `wiki/analyses/`. These compound just like ingested sources.
- **Update dates**: make sure Copilot updates the `updated:` frontmatter field on every page it touches.
- **Version control**: `git init` this folder. Commit after every ingest. You get full history of how your knowledge evolved.
- **Batch ingest**: you can drop multiple sources and ask Copilot to process them all, but quality is better one at a time with you in the loop.

---

## Grep the log

```bash
# Last 5 operations
grep "^## \[" wiki/log.md | tail -5

# All ingests
grep "^## \[" wiki/log.md | grep "ingest"

# All contradictions flagged
grep "⚠️" wiki/**/*.md
```
