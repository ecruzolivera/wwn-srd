#!/usr/bin/env python3
"""Extract the WWN SRD PDF to Markdown with column-aware reading order.

Usage: pdf_to_md.py <input.pdf> <output.md>

Uses PyMuPDF text blocks. Each block is one table row, heading, or paragraph.
For two-column pages, blocks are emitted full-width-first, then the left
column top-to-bottom, then the right column top-to-bottom. Decorative running
headers and footers (page numbers) are dropped. Emits `<!-- p.N -->` markers.
"""
import sys
import re
import pymupdf

PAGE_MARK = "<!-- p.{} -->"

HEADER_TOP = 20       # blocks starting above this are running headers (y0~10)
FOOTER_BOTTOM = 60    # blocks starting closer than this to bottom are footers
FULL_RATIO = 0.55     # block spanning >= this fraction of text width is "full"


def block_text(b):
    """Join a block's internal lines into a single spaced line."""
    t = re.sub(r"\s+", " ", b[4].replace("\u00a0", " ")).strip()
    return t


def classify(b, page_width, text_width):
    x0, y0, x1, y1 = b[0], b[1], b[2], b[3]
    if x1 - x0 >= FULL_RATIO * text_width:
        return "full"
    if x0 < page_width / 2:
        return "left"
    return "right"


def process_page(page):
    blocks = page.get_text("blocks")
    page_width = page.rect.width
    page_height = page.rect.height
    text_width = page_width - 2 * HEADER_TOP

    items = []
    for b in blocks:
        if b[6] != 0:
            continue
        txt = block_text(b)
        if not txt:
            continue
        x0, y0, x1, y1 = b[0], b[1], b[2], b[3]
        if y0 < HEADER_TOP:
            continue
        if y0 > page_height - FOOTER_BOTTOM:
            continue
        if re.fullmatch(r"\d{1,3}", txt):
            continue
        items.append({
            "y0": y0,
            "x0": x0,
            "kind": classify(b, page_width, text_width),
            "text": txt,
        })

    if not items:
        return []

    has_right = any(it["kind"] == "right" for it in items)
    if not has_right:
        items.sort(key=lambda it: (round(it["y0"], 1), it["x0"]))
        return [it["text"] for it in items]

    full = sorted([it for it in items if it["kind"] == "full"],
                  key=lambda it: round(it["y0"], 1))
    left = sorted([it for it in items if it["kind"] == "left"],
                  key=lambda it: round(it["y0"], 1))
    right = sorted([it for it in items if it["kind"] == "right"],
                   key=lambda it: round(it["y0"], 1))
    return [it["text"] for it in (full + left + right)]


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]

    parts = ["# Worlds Without Number — SRD v1.0 (en)\n"]
    doc = pymupdf.open(src)
    for i, page in enumerate(doc):
        lines = process_page(page)
        parts.append(PAGE_MARK.format(i + 1))
        parts.extend(lines)
    doc.close()

    text = "\n".join(parts) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {dst} ({len(text)} chars)")


if __name__ == "__main__":
    main()
