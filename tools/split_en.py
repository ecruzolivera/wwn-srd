#!/usr/bin/env python3
"""Split en/wwn-srd.md into one file per top-level section."""
import re
from pathlib import Path

SRC = Path(__file__).parent.parent / "en" / "wwn-srd.md"
OUT = Path(__file__).parent.parent / "en"

sections = [
    ("00-introduction.md", None),
    ("01-character-creation.md", "1.0.0 Character Creation"),
    ("02-rules-of-the-game.md", "2.0.0 The Rules of the Game"),
    ("03-equipment-armor-weapons.md", "3.0.0 Equipment, Armor, and Weapons"),
    ("04-magic-and-spellcasting.md", "4.0.0 Magic and Spellcasting"),
    ("05-monsters-and-foes.md", "5.0.0 Monsters and Foes"),
    ("06-factions.md", "6.0.0 Factions"),
    ("07-major-projects.md", "7.0.0 Major Projects"),
]

text = SRC.read_text(encoding="utf-8")
lines = text.split("\n")

# find content start markers (a line that is exactly the section header)
bounds = {}
for i, ln in enumerate(lines):
    for fname, marker in sections:
        if marker and ln.strip() == marker:
            bounds.setdefault(fname, i)

starts = [("00-introduction.md", 0)]
for fname, _ in sections[1:]:
    starts.append((fname, bounds[fname]))

for idx, (fname, start) in enumerate(starts):
    end = starts[idx + 1][1] if idx + 1 < len(starts) else len(lines)
    body = "\n".join(lines[start:end]).strip()
    (OUT / fname).write_text(body + "\n", encoding="utf-8")
    print(f"{fname}: lines {start}-{end} ({len(body.splitlines())} lines)")
