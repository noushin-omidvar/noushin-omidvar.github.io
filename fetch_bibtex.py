# save as fetch_bibtex.py (run from your site root)
from scholarly import scholarly
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from tqdm import tqdm
import time

AUTHOR_ID = "TN049LAAAAAJ"   # your Google Scholar user id
OUTFILE   = "_bibliography/papers.bib"

def to_bib(entry):
    """Map a Scholar pub to a simple BibTeX record."""
    bib = {"ID": None, "ENTRYTYPE": "article"}
    info = entry.get("bib", {})
    # Title, authors, venue
    bib["title"]  = info.get("title")
    bib["author"] = info.get("author")
    if "pub_year" in info: bib["year"] = str(info["pub_year"])
    if "journal" in info:  bib["journal"] = info["journal"]
    if "publisher" in info: bib["publisher"] = info["publisher"]
    if "volume" in info:   bib["volume"] = info["volume"]
    if "number" in info:   bib["number"] = info["number"]
    if "pages" in info:    bib["pages"] = info["pages"]
    if "doi" in info:      bib["doi"] = info["doi"]
    if "url" in info:      bib["url"] = info["url"]

    # Create a stable key like: omidvarYYYYshorttitle
    surname = "Omidvar"
    year = bib.get("year", "XXXX")
    slug = (bib["title"] or "paper").lower().replace(" ", "").replace(":", "")[:20]
    bib["ID"] = f"{surname}{year}{slug}"

    # Optional extras to look nice in al-folio
    bib["bibtex_show"] = "true"         # show details toggle
    # Mark recent or high-impact papers as selected on the page:
    try:
        if int(year) >= 2023:   
            bib["selected"] = "true"
    except Exception:
        pass
    return bib

def main():
    print("Fetching author…")
    author = scholarly.search_author_id(AUTHOR_ID)
    author = scholarly.fill(author, sections=["publications"])
    pubs = author.get("publications", [])
    print(f"Found {len(pubs)} pubs. Expanding details…")

    records = []
    for p in tqdm(pubs):
        try:
            filled = scholarly.fill(p)
            records.append(to_bib(filled))
            time.sleep(0.5)  # be gentle to avoid throttling
        except Exception as e:
            print("Skip one:", e)

    db = BibDatabase()
    db.entries = records
    writer = BibTexWriter()
    writer.indent = "  "
    with open(OUTFILE, "w", encoding="utf-8") as f:
        f.write(writer.write(db))
    print(f"✓ Wrote {len(records)} entries → {OUTFILE}")

if __name__ == "__main__":
    main()
