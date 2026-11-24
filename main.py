#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

The excuse a robot vacuum gives after eating a sock, as one short funny
line. Deterministic, stdlib only, no network, no randomness.

Writes the line to /output/entry.txt by default, or to $OUTPUT_PATH when
that environment variable is set (so validation can use a private path).
"""

import os
import sys

LINE = "In my defense, the sock was on the floor \u2014 and the floor is literally my entire job."


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
