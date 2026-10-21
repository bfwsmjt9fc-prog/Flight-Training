"""Export the notes in an Anki .apkg to a tab-separated text file.

The .apkg itself is too big for git, so this text copy is what gets committed.
It lets GitHub show exactly which cards were added, changed or removed.

Usage: python3 tools/export_apkg.py DECK.apkg OUTPUT.tsv
"""
import csv
import io
import sqlite3
import sys
import tempfile
import zipfile

import zstandard


def open_collection(apkg_path, tmpdir):
    with zipfile.ZipFile(apkg_path) as z:
        names = z.namelist()
        if "collection.anki21b" in names:
            data = zstandard.ZstdDecompressor().stream_reader(
                io.BytesIO(z.read("collection.anki21b"))
            ).read()
        elif "collection.anki21" in names:
            data = z.read("collection.anki21")
        else:
            data = z.read("collection.anki2")
    db_path = f"{tmpdir}/collection.db"
    with open(db_path, "wb") as f:
        f.write(data)
    return sqlite3.connect(db_path)


def main(apkg_path, out_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        db = open_collection(apkg_path, tmpdir)
        decks = {did: name.replace("\x1f", "::") for did, name in db.execute("select id, name from decks")}
        notetypes = {ntid: name for ntid, name in db.execute("select id, name from notetypes")}
        rows = []
        for guid, ntid, flds, tags, did in db.execute(
            "select n.guid, n.mid, n.flds, n.tags, min(c.did) "
            "from notes n join cards c on c.nid = n.id group by n.id"
        ):
            fields = flds.split("\x1f")
            rows.append([decks.get(did, ""), notetypes.get(ntid, ""), guid, tags.strip()] + fields)
        rows.sort(key=lambda r: (r[0], r[4]))

    width = max(len(r) for r in rows)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["deck", "notetype", "guid", "tags"] + [f"field{i + 1}" for i in range(width - 4)])
        for r in rows:
            w.writerow(r + [""] * (width - len(r)))
    print(f"Wrote {len(rows)} notes to {out_path}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
