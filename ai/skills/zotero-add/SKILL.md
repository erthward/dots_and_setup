---
name: zotero-add
description: Add papers, datasets, software, or other references to my Zotero library (into the "🤖📥" review collection) from a DOI or a hand-built item. Use when I ask to add/save something to Zotero, and offer it (don't do it unasked) when you recommend a paper or dataset I don't already have in ~/Zotero/deth_library.bib.
---

# zotero-add

Script: `~/dots_and_setup/ai/skills/zotero-add/zotero_add.py` (stdlib-only Python).

## rules
- **Only add when I've said yes** (in this conversation) to that specific item. Adding writes to my
  synced library.
- Run `--dry-run` first if the item type is unusual (dataset, software, report, chapter) and show me
  the one-line summary; for ordinary journal articles, go straight to the real run.
- Never print, echo, or read the key file; just source it.
- After adding, tell me the item key and remind me it lands in `🤖📥` for review. Better BibTeX
  exports it to the .bib only after Zotero desktop syncs; it is NOT citable until it's in the .bib.

## run (Bash; needs network to these hosts)
```zsh
source ~/Desktop/stuff/secrets/.zotero_api_keys && \
  python3 -I ~/dots_and_setup/ai/skills/zotero-add/zotero_add.py <DOI> [<DOI> ...] [--dry-run] [--force]
```
allowed_domains: `doi.org`, `api.crossref.org`, `data.crosscite.org`, `api.datacite.org`, `api.zotero.org`

## things without a DOI (datasets, government data, webpages, software)
Write a JSON Zotero item to the scratchpad and pass `--json path`. Field names must match the
Zotero template for that itemType (the script validates and fails loudly). See valid fields with
`curl -s 'https://api.zotero.org/items/new?itemType=dataset'`. Example:
```json
{"itemType": "dataset", "title": "National Forest and Sparse Woody Vegetation Data",
 "creators": [{"creatorType": "author", "name": "Department of Climate Change, Energy, the Environment and Water"}],
 "date": "2023", "versionNumber": "8.0", "repository": "DCCEEW", "url": "https://..."}
```
Organisations go in `"name"`; people use `"firstName"`/`"lastName"`.

## behavior
- Duplicate check: DOI against the .bib, then a Zotero server-side search (catches synced-but-not-yet-
  exported items). Use `--force` only if I confirm it's not a real duplicate.
- Unknown CSL types fail loudly; extend `CSL2ZOT` in the script rather than guessing.
- Creates `🤖📥` if it doesn't exist.
- Doesn't attach PDFs (paywalls; I'll grab them via the browser connector if I want them).
