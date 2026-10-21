# FLT 328-A Aircraft Systems

- `anki/` Anki decks and card source files
- `quizzes/` practice quizzes
- `notes/` lecture notes and summaries

## Anki deck

[`anki/cards.tsv`](anki/cards.tsv) is a text copy of every note in the deck: its subdeck, note type, tags and fields.
It's here so GitHub can show exactly which cards changed between versions. As of Oct 20, 2026 it has
2,055 notes (2,822 cards) through Quiz 4 (Week 6).

The `.apkg` itself (about 115 MB, mostly diagram images) is too big to keep in the repo, because GitHub
rejects files over 100 MB. Each version is attached to a [release](https://github.com/bfwsmjt9fc-prog/flight-training/releases) instead.

To refresh the text copy after exporting a new `.apkg` from Anki:

```
python3 tools/export_apkg.py "FLT 328-A Aircraft Systems.apkg" FLT328A-aircraft-systems/anki/cards.tsv
```
