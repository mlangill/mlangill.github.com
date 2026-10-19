"""Fill in publication details for entries that only have a DOI.

Reads _data/publications.yml. For any entry with a `doi` but no `title`,
it looks the DOI up on Crossref and adds the title, authors, journal, year
and volume details. Entries you have already filled in are never changed.
The list is then sorted newest first (keeping your order within a year).

Run by the GitHub Action in .github/workflows/fill-dois.yml, or by hand:
    pip install pyyaml requests
    python scripts/fill_dois.py
"""
import html
import re
import sys
from pathlib import Path

import requests
import yaml

DATA = Path(__file__).resolve().parent.parent / "_data" / "publications.yml"

HEADER = """# Lab publications, newest first.
#
# To add a paper, the quickest way is a new entry with just the DOI:
#   - doi: 10.1186/s40168-026-02529-z
# When you push, a GitHub Action looks up the title, authors, journal and
# year and fills them in for you.
#
# Optional fields on any entry:
#   featured: true      shows the paper on the homepage
#   tags: [methods]     groups papers on the Publications page
#
"""

FIELD_ORDER = ["authors", "year", "title", "link", "journal", "details", "doi", "featured", "tags"]


def initials(given):
    parts = re.split(r"[\s.\-]+", given or "")
    return "".join(p[0].upper() for p in parts if p)


def format_authors(authors):
    names = []
    for a in authors:
        if "family" in a:
            names.append(f"{a['family']} {initials(a.get('given', ''))}".strip())
        elif "name" in a:
            names.append(a["name"])
    return ", ".join(names)


def clean(text):
    text = re.sub(r"<[^>]+>", "", text or "")
    return " ".join(html.unescape(text).split())


def lookup(doi):
    r = requests.get(
        f"https://api.crossref.org/works/{doi}",
        headers={"User-Agent": "LangilleLabWebsite/1.0 (mailto:morgan.langille@dal.ca)"},
        timeout=30,
    )
    r.raise_for_status()
    m = r.json()["message"]
    date = (m.get("published-print") or m.get("published-online") or m.get("issued") or {}).get("date-parts", [[None]])
    entry = {
        "authors": format_authors(m.get("author", [])),
        "year": date[0][0],
        "title": clean((m.get("title") or [""])[0]),
        "link": f"https://doi.org/{doi}",
        "journal": clean((m.get("container-title") or [""])[0]),
    }
    details = ":".join(x for x in [m.get("volume", ""), m.get("page") or m.get("article-number", "")] if x)
    if details:
        entry["details"] = details
    return {k: v for k, v in entry.items() if v}


def ordered(entry):
    keys = [k for k in FIELD_ORDER if k in entry] + [k for k in entry if k not in FIELD_ORDER]
    return {k: entry[k] for k in keys}


def main():
    pubs = yaml.safe_load(DATA.read_text(encoding="utf-8")) or []
    filled, failed = 0, []
    for i, p in enumerate(pubs):
        if p.get("doi") and not p.get("title"):
            doi = str(p["doi"]).strip()
            try:
                found = lookup(doi)
            except Exception as err:  # keep going; report at the end
                failed.append(f"{doi}: {err}")
                continue
            pubs[i] = ordered({**found, **p, "doi": doi})
            filled += 1
            print(f"Filled {doi}: {found.get('title', '')[:70]}")
    pubs.sort(key=lambda p: -(p.get("year") or 0))
    DATA.write_text(
        HEADER + yaml.safe_dump(pubs, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    print(f"{filled} entries filled in")
    if failed:
        print("Could not look up:\n  " + "\n  ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
