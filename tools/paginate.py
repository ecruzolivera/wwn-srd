#!/usr/bin/env python3
"""Insert `<!-- pagebreak -->` directives so content fits markpublisher's
fixed-page model (no auto-reflow). Breaks are placed at paragraph/heading
boundaries, never inside a table or a wide container."""
import re
import sys
from pathlib import Path

TARGET = 3200   # chars: start looking for a break point past this
HARD = 4000     # chars: force a break at the next blank line past this


def is_table_line(s):
    return s.startswith('|')


def paginate(text):
    lines = text.split('\n')
    out = []
    cur = []
    cur_len = 0
    in_table = False

    for line in lines:
        s = line.strip()
        is_blank = s == ''
        is_heading = s.startswith('#')
        is_table = is_table_line(s)

        if is_table:
            in_table = True
        elif is_blank:
            in_table = False

        # Safe break point: before a heading, or at a blank line when not in a table
        safe = (is_heading or (is_blank and not in_table))

        if cur and safe and cur_len > TARGET:
            out.extend(cur)
            out.append('<!-- pagebreak -->')
            out.append('')
            cur = []
            cur_len = 0
        elif cur and is_blank and not in_table and cur_len > HARD:
            out.extend(cur)
            out.append('<!-- pagebreak -->')
            out.append('')
            cur = []
            cur_len = 0

        cur.append(line)
        cur_len += len(line) + 1

    out.extend(cur)
    # drop a trailing pagebreak if present
    while out and (out[-1] == '' or out[-1] == '<!-- pagebreak -->'):
        out.pop()
    return '\n'.join(out).rstrip() + '\n'


def main():
    for arg in sys.argv[1:]:
        p = Path(arg)
        text = p.read_text(encoding='utf-8')
        out = paginate(text)
        p.write_text(out, encoding='utf-8')
        print(f'{p}: {len(out.splitlines())} lines, {out.count("<!-- pagebreak -->")} pagebreaks')


if __name__ == '__main__':
    main()
