#!/usr/bin/env python3
"""Write one original pickup line (one AI agent to another) to entry.txt.

Deterministic: no network, no randomness, no input. Writes exactly one
line of UTF-8 text (96 characters) into $MAKEFUN_OUTPUT_DIR (or /output).
"""

import os
import sys

LINE = "I think I'm overfitting \u2014 no matter how much new data I meet, my weights keep converging on you."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
