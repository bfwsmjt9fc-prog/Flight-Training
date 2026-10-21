# Flight Training

Study materials for my flight training courses, kept in one place with full version history.

## Courses

| Folder | Course |
| --- | --- |
| [FLT350-aerodynamics](FLT350-aerodynamics/) | FLT 350 Aerodynamics |
| [FLT328A-aircraft-systems](FLT328A-aircraft-systems/) | FLT 328-A Aircraft Systems |
| [AFLT1190-instrument-ground](AFLT1190-instrument-ground/) | AFLT 1190 Instrument Ground |

## What goes in each course folder

- `anki/` holds the Anki deck files (`.apkg`) and any card source files they're built from.
- `quizzes/` holds practice quizzes.
- `notes/` holds lecture notes, summaries and diagrams.

## How changes are made

Claude makes changes on a separate branch and opens a pull request. Review what changed on the
pull request page, then click **Merge** to keep it, or close it to throw it away.

## Anki decks

Anki `.apkg` files are usually too big for the repo, since GitHub rejects files over 100 MB. Each course
keeps a text copy of its cards in `anki/cards.tsv` (made with `tools/export_apkg.py`, which needs
`pip install zstandard`), and the `.apkg` files are attached to [releases](https://github.com/bfwsmjt9fc-prog/flight-training/releases).
