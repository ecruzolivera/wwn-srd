#!/usr/bin/env python3
"""Check the formatted English chapters without rebuilding the Spanish book.

Uses only the standard library. The raw SRD remains the reference for page
markers, including markers embedded in the introduction's linked TOC.
"""
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / 'en'
CHAPTERS = [
    '00-introduction.md',
    '01-character-creation.md',
    '02-rules-of-the-game.md',
    '03-equipment-armor-weapons.md',
    '04-magic-and-spellcasting.md',
    '05-monsters-and-foes.md',
    '06-factions.md',
    '07-major-projects.md',
]
PAGE = re.compile(r'<!-- p\.\d+ -->')
HEADING = re.compile(r'^#{1,6} (.+)$', re.MULTILINE)


def slugs(text):
    """GitHub-style slugs for this corpus's English, ASCII section titles."""
    counts = Counter()
    result = set()
    for title in HEADING.findall(text):
        slug = re.sub(r'[^a-z0-9_ -]', '', title.lower()).replace(' ', '-')
        occurrence = counts[slug]
        counts[slug] += 1
        result.add(f'{slug}-{occurrence}' if occurrence else slug)
    return result


def cells(line):
    return re.split(r'(?<!\\)\|', line.strip().strip('|'))


def main():
    errors = []
    texts = {name: (EN / name).read_text(encoding='utf-8') for name in CHAPTERS}
    raw = (EN / 'wwn-srd.md').read_text(encoding='utf-8')
    starts = [0]
    for name in CHAPTERS[1:]:
        title = HEADING.search(texts[name]).group(1)
        match = re.search(r'^' + re.escape(title) + r'$', raw, re.MULTILINE)
        if not match:
            errors.append(f'{name}: chapter title not found in raw SRD')
            continue
        starts.append(match.start())
    if len(starts) != len(CHAPTERS):
        raise SystemExit('\n'.join(errors))
    starts.append(len(raw))
    totals = Counter()
    for index, name in enumerate(CHAPTERS):
        text = texts[name]
        expected = PAGE.findall(raw[starts[index]:starts[index+1]])
        if PAGE.findall(text) != expected:
            errors.append(f'{name}: page markers differ from raw SRD')
        if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text):
            errors.append(f'{name}: extraction control characters remain')
        table_width = None
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f'{name}:{line_number}: trailing whitespace')
            if line.startswith('|'):
                width = len(cells(line))
                if table_width is None:
                    table_width = width
                    totals['tables'] += 1
                elif width != table_width:
                    errors.append(f'{name}:{line_number}: table column count differs')
            else:
                table_width = None
            if re.match(r'^[1-7](?:\.\d+){2,3} ', line):
                errors.append(f'{name}:{line_number}: unformatted numbered heading')
        totals['markers'] += len(expected)
        totals['headings'] += len(HEADING.findall(text))
    for target, anchor in re.findall(r'\]\(([^)#]+\.md)#([^)]*)\)', texts[CHAPTERS[0]]):
        if target not in texts:
            errors.append(f'00-introduction.md: unknown link target {target}')
        elif anchor not in slugs(texts[target]):
            errors.append(f'00-introduction.md: missing anchor {target}#{anchor}')
        totals['links'] += 1
    # Regression checks for the chapter-7 extraction-order repairs.
    projects = texts['07-major-projects.md']
    magical = projects.split('## 7.7.0 Magical Projects', 1)[1].split('## 7.8.0', 1)[0]
    for phrase in ['one great Working will be necessary', 'If these Workings are later destroyed']:
        if phrase not in magical:
            errors.append('07-major-projects.md: magical-project paragraph in wrong section')
    if 'Multiply opposition by x2 if the local population is emotionally or socially against it.' not in projects:
        errors.append('07-major-projects.md: opposition table note missing')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f"OK: {len(CHAPTERS)} chapters, {totals['links']} TOC links, "
          f"{totals['tables']} tables, {totals['markers']} page markers.")


if __name__ == '__main__':
    main()
