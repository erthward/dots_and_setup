#!/usr/bin/env python3
"""
Add items to my Zotero library (via the Zotero Web API) from DOIs or a manual JSON spec.

Metadata come from doi.org content negotiation (CSL-JSON), which covers both Crossref
(journal articles, chapters, preprints) and DataCite (Zenodo, Dryad, Figshare, PANGAEA datasets
and software). Items land in a single review collection (default "🤖📥"), so Claude-added
items never mix silently into the main library.

Usage
-----
    zotero_add.py 10.1038/s41586-026-11284-y [more DOIs ...] [--dry-run] [--force]
    zotero_add.py --json item.json [--dry-run]   # for things without a DOI

Env vars (sourced from ~/Desktop/stuff/secrets/.zotero_api_keys):
    ZOTERO_USER_ID, ZOTERO_WRITE_KEY, ZOTERO_READ_KEY (optional; falls back to write key)

Only the Python standard library is used, so it runs under any python3.
"""

import argparse
import json
import os
import re
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request

###################
# BEHAVIORAL PARAMS
###################
COLLECTION_NAME = "🤖📥"
BIB_PATH = os.path.expanduser("~/Zotero/deth_library.bib")
API = "https://api.zotero.org"
TIMEOUT = 30
UA = "zotero-add-script/0.1 (personal library tool)"
# NOTE: CSL type -> Zotero itemType. Unknown types fail loudly rather than being guessed at.
CSL2ZOT = {
    "article-journal": "journalArticle", "journal-article": "journalArticle",
    "article": "preprint", "posted-content": "preprint",
    "dataset": "dataset",
    "book": "book", "monograph": "book", "edited-book": "book",
    "chapter": "bookSection", "book-chapter": "bookSection",
    "paper-conference": "conferencePaper", "proceedings-article": "conferencePaper",
    "report": "report",
    "software": "computerProgram",
    "thesis": "thesis", "dissertation": "thesis",
    "webpage": "webpage",
}
# NOTE: field the CSL container title / publisher map onto, per Zotero itemType
CONTAINER_FIELD = {"journalArticle": "publicationTitle", "bookSection": "bookTitle",
                   "conferencePaper": "proceedingsTitle", "webpage": "websiteTitle"}
PUBLISHER_FIELD = {"dataset": "repository", "preprint": "repository", "report": "institution",
                   "thesis": "university", "computerProgram": "company"}


##############
# HTTP HELPERS
##############
def _req(url, method="GET", headers=None, body=None):
    """Make an HTTP request; return (status, headers, parsed-or-raw body). Raises loudly on HTTP errors."""
    h = {"User-Agent": UA}
    h.update(headers or {})
    data = json.dumps(body).encode() if body is not None else None
    if data is not None:
        h["Content-Type"] = "application/json"
    r = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=TIMEOUT) as resp:
            raw = resp.read().decode()
            try:
                return resp.status, resp.headers, json.loads(raw)
            except json.JSONDecodeError:
                return resp.status, resp.headers, raw
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} for {method} {url}: {e.read().decode()[:500]}") from None


def _zot_headers(write=False):
    key = os.environ.get("ZOTERO_WRITE_KEY") if write else (
        os.environ.get("ZOTERO_READ_KEY") or os.environ.get("ZOTERO_WRITE_KEY"))
    if not key:
        raise RuntimeError("Zotero API key env var missing (ZOTERO_WRITE_KEY / ZOTERO_READ_KEY); "
                           "source ~/Desktop/stuff/secrets/.zotero_api_keys first.")
    return {"Zotero-API-Key": key, "Zotero-API-Version": "3"}


def _lib():
    uid = os.environ.get("ZOTERO_USER_ID")
    if not uid or not uid.isdigit():
        raise RuntimeError(f"ZOTERO_USER_ID missing or non-numeric (len {len(uid or '')})")
    return f"{API}/users/{uid}"


##########
# METADATA
##########
def norm_doi(doi):
    """Strip URL/prefix cruft and lowercase (DOIs are case-insensitive)."""
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi.strip(), flags=re.I).lower()
    if not re.match(r"^10\.\d{4,9}/\S+$", d):
        raise ValueError(f"Doesn't look like a DOI: {doi!r}")
    return d


def fetch_csl(doi):
    """CSL-JSON via doi.org content negotiation (resolves to Crossref or DataCite)."""
    url = "https://doi.org/" + urllib.parse.quote(doi, safe="/")
    _, _, csl = _req(url, headers={"Accept": "application/vnd.citationstyles.csl+json"})
    if not isinstance(csl, dict) or "title" not in csl:
        raise RuntimeError(f"No usable CSL-JSON for {doi}: {str(csl)[:300]}")
    return csl


def _date(csl):
    for k in ("issued", "published-print", "published-online", "created"):
        parts = (csl.get(k) or {}).get("date-parts")
        if parts and parts[0] and parts[0][0]:
            return "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(parts[0]))
    return ""


def _clean(s):
    """Strip JATS/HTML tags and collapse whitespace (Crossref abstracts come JATS-wrapped)."""
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", s).strip()


def _first(x):
    return x[0] if isinstance(x, list) and x else (x or "")


def csl_to_zotero(csl, template):
    """Fill a Zotero item template from CSL-JSON, only touching fields the itemType supports."""
    it = dict(template)
    t = it["itemType"]
    fields = {
        "title": _clean(_first(csl.get("title"))),
        "abstractNote": _clean(csl.get("abstract")),
        "date": _date(csl),
        "volume": csl.get("volume", ""), "issue": csl.get("issue", ""),
        "pages": csl.get("page", ""),
        "DOI": csl.get("DOI", ""), "url": csl.get("URL", ""),
        "ISSN": _first(csl.get("ISSN")), "ISBN": _first(csl.get("ISBN")),
        "language": csl.get("language", ""),
        "journalAbbreviation": _first(csl.get("container-title-short")),
        "versionNumber": str(csl.get("version", "") or ""),
        "publisher": csl.get("publisher", ""),
    }
    if t in CONTAINER_FIELD:
        fields[CONTAINER_FIELD[t]] = _clean(_first(csl.get("container-title")))
    if t in PUBLISHER_FIELD:
        fields[PUBLISHER_FIELD[t]] = csl.get("publisher", "")
    for k, v in fields.items():
        if v and k in it:
            it[k] = v
    creators = []
    for role, ctype in (("author", "author"), ("editor", "editor")):
        for a in csl.get(role, []) or []:
            if a.get("family"):
                creators.append({"creatorType": ctype, "firstName": a.get("given", ""),
                                 "lastName": a["family"]})
            elif a.get("literal") or a.get("name"):
                creators.append({"creatorType": ctype, "name": a.get("literal") or a.get("name")})
    # NOTE: datasets/software often list organisations, or use 'contributor'; fall back gracefully
    if not creators and t in ("dataset", "computerProgram"):
        for a in csl.get("contributor", []) or []:
            nm = a.get("literal") or " ".join(x for x in (a.get("given"), a.get("family")) if x)
            if nm:
                creators.append({"creatorType": "contributor", "name": nm})
    it["creators"] = creators
    if not it.get("title"):
        raise RuntimeError(f"Mapped item has no title; CSL was: {json.dumps(csl)[:400]}")
    return it


_templates = {}
def template(item_type):
    if item_type not in _templates:
        _, _, tpl = _req(f"{API}/items/new?itemType={item_type}")
        if not isinstance(tpl, dict) or tpl.get("itemType") != item_type:
            raise RuntimeError(f"Bad Zotero template for {item_type}: {str(tpl)[:300]}")
        _templates[item_type] = tpl
    return _templates[item_type]


##################
# DUPLICATE CHECKS
##################
def in_bib(doi):
    if not os.path.isfile(BIB_PATH):
        print(f"WARNING: {BIB_PATH} not found; skipping .bib duplicate check")
        return False
    pat = re.compile(r"doi\s*=\s*\{" + re.escape(doi) + r"\}", re.I)
    with open(BIB_PATH, encoding="utf-8") as f:
        return bool(pat.search(f.read()))


def _norm_title(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def in_zotero(title, doi=None):
    """
    Server-side duplicate search (catches items synced but not yet exported to the .bib).

    NOTE: Zotero's quick search does NOT index the DOI field (verified 2026-11-19), so we search
    by title, then confirm a duplicate by exact DOI match, or by exact normalized title match.
    """
    q = urllib.parse.quote(title[:120])
    _, _, res = _req(f"{_lib()}/items?q={q}&qmode=titleCreatorYear&limit=25&itemType=-attachment",
                     headers=_zot_headers())
    if not isinstance(res, list):
        raise RuntimeError(f"Unexpected Zotero search response: {str(res)[:300]}")
    hits = []
    for r in res:
        d = r["data"]
        same_doi = doi and (d.get("DOI") or "").strip().lower() == doi
        same_title = _norm_title(d.get("title")) == _norm_title(title)
        if same_doi or same_title:
            hits.append((r["key"], d.get("title", ""), d.get("DOI", "")))
    return hits


####################
# COLLECTION + WRITE
####################
def get_or_create_collection(name, dry_run=False):
    start = 0
    while True:
        _, hdr, cols = _req(f"{_lib()}/collections?limit=100&start={start}", headers=_zot_headers())
        for c in cols:
            if c["data"]["name"] == name:
                return c["key"]
        start += 100
        if start >= int(hdr.get("Total-Results", 0)):
            break
    if dry_run:
        print(f"[dry-run] would create collection {name!r}")
        return "DRYRUN"
    _, _, res = _req(f"{_lib()}/collections", "POST",
                     {**_zot_headers(write=True), "Zotero-Write-Token": secrets.token_hex(16)},
                     [{"name": name}])
    if not res.get("successful"):
        raise RuntimeError(f"Collection creation failed: {res}")
    key = res["successful"]["0"]["key"]
    print(f"created collection {name!r} ({key})")
    return key


def post_items(items):
    _, _, res = _req(f"{_lib()}/items", "POST",
                     {**_zot_headers(write=True), "Zotero-Write-Token": secrets.token_hex(16)}, items)
    if res.get("failed"):
        raise RuntimeError(f"Zotero rejected item(s): {json.dumps(res['failed'], ensure_ascii=False)}")
    return [v["key"] for v in res["successful"].values()]


######
# MAIN
######
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dois", nargs="*")
    ap.add_argument("--json", help="path to a JSON Zotero item (or list) for things without DOIs")
    ap.add_argument("--collection", default=COLLECTION_NAME)
    ap.add_argument("--dry-run", action="store_true", help="build and print items; write nothing")
    ap.add_argument("--force", action="store_true", help="add even if a duplicate is found")
    a = ap.parse_args(argv)
    if not a.dois and not a.json:
        ap.error("give at least one DOI or --json")

    items = []
    for raw in a.dois:
        doi = norm_doi(raw)
        if not a.force and in_bib(doi):
            print(f"SKIP {doi}: already in {BIB_PATH}")
            continue
        csl = fetch_csl(doi)
        if not a.force:
            hits = in_zotero(_clean(_first(csl.get("title"))), doi)
            if hits:
                print(f"SKIP {doi}: already in Zotero: {hits}")
                continue
        ctype = csl.get("type", "")
        if ctype not in CSL2ZOT:
            raise RuntimeError(f"Unmapped CSL type {ctype!r} for {doi}; add it to CSL2ZOT or use --json")
        items.append(csl_to_zotero(csl, template(CSL2ZOT[ctype])))

    if a.json:
        with open(a.json, encoding="utf-8") as f:
            manual = json.load(f)
        for m in (manual if isinstance(manual, list) else [manual]):
            tpl = template(m.get("itemType", ""))
            bad = set(m) - set(tpl)
            if bad:
                raise ValueError(f"Fields not valid for {m['itemType']}: {sorted(bad)}")
            if not m.get("title"):
                raise ValueError(f"Manual item lacks a title: {m}")
            if not a.force:
                hits = in_zotero(m["title"])
                if hits:
                    print(f"SKIP {m['title']!r}: possible duplicate in Zotero: {hits}")
                    continue
            items.append({**tpl, **m})

    if not items:
        print("nothing to add")
        return 0
    ckey = get_or_create_collection(a.collection, a.dry_run)
    for it in items:
        it["collections"] = [ckey]
        cr = it.get("creators", [])
        who = (cr[0].get("lastName") or cr[0].get("name", "?")) if cr else "?"
        print(f"{'[dry-run] ' if a.dry_run else ''}{it['itemType']}: {who}"
              f"{' et al.' if len(cr) > 1 else ''} ({it.get('date', '')[:4]}) {it['title']}"
              f" | {len(cr)} creators | DOI {it.get('DOI', '-')}")
    if a.dry_run:
        print(json.dumps(items, ensure_ascii=False, indent=1)[:3000])
        return 0
    # NOTE: Zotero API caps writes at 50 items per request
    keys = []
    for i in range(0, len(items), 50):
        keys += post_items(items[i:i + 50])
    print(f"added {len(keys)} item(s) to {a.collection!r}: {keys}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
