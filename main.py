#!/usr/bin/env python3
"""Entry for make.fun: 'One-Liner Laugh Lab'.

Writes one short funny line to the output entry file: the excuse a
robot vacuum gives after eating a sock. Stdlib only, deterministic.
"""

import os
import sys

LINE = (
    "The sock never moved, never thanked me, and smelled like a dare "
    "\u2014 so I ate it."
)
# 78 chars. Three-beat deadpan excuse (never moved / never thanked /
# smelled like a dare) with the confession as the punchline: fits the
# robot-vacuum prompt, lands the twist in the last four words, no
# setup that overstays. The em dash keeps it one line.

MAX_CHARS = 200


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the written file back and check it against the kit gate:
    UTF-8 text of 1 to 200 characters, not only white space, one line."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"gate FAIL: {len(text)} chars (need 1-200)")
    if not text.strip():
        raise SystemExit("gate FAIL: entry is only white space")
    if "\n" in text.strip():
        raise SystemExit("gate FAIL: entry is not one line")
    print(f"gate PASS: {len(text)} chars")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    verify(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
