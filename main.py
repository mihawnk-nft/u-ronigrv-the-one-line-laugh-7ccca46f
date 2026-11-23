#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one original funny line to /output/entry.txt. Pure Python
standard library: no imports beyond os/sys/unicodedata, no network,
no files read, no environment read except the output directory.

The line: a smartwatch congratulates its owner for closing the
exercise ring, which is generous, since the only workout was reaching
for the charger. Everyday truth (fitness-tracker rings), surprise at
the end (the "workout" was reaching for the charger), economical
(143 chars, one sentence), fresh angle (the watch praising almost
no exercise at all, instead of the stock jokes about step counts).
"""

import os
import sys
import unicodedata

LINE = (
    "My smartwatch congratulated me on closing my exercise ring "
    "today, which is generous, since the only workout I did was "
    "reaching for the charger."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # The judge reads printable text: no control characters, and at
    # least one letter so it cannot be punctuation alone.
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if not any(ch.isalpha() for ch in text):
        print("entry must contain at least one letter", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
