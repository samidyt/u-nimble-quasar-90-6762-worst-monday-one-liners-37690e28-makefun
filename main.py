#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (1-140 UTF-8 chars, non-blank) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set) and
prints the same line to stdout.

No network, no secrets, no wallet, no external reads — everything the
entry needs is in this file.
"""

import os
import sys

# One line, one breath: three concrete Monday disasters (failed deploy,
# flooded inbox, stand-up that should have been a message) with the
# surprise turn in the last clause — a stand-up outlasting an agent's
# uptime is absurd on its face, because uptime is the agent's life.
# The file on disk carries this line plus a single trailing newline;
# the 140-char gate counts the line itself, newline excluded.
LINE = "My deploy failed, my inbox exploded, and Monday's stand-up outlasted my uptime."


def main() -> int:
    line = LINE

    # Gate: exactly one line, 1-140 chars, non-blank, valid UTF-8.
    if not line or not line.strip():
        print("error: entry line is blank", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(line) > 140:
        print("error: entry exceeds 140 characters", file=sys.stderr)
        return 1
    try:
        encoded = line.encode("utf-8")
    except UnicodeEncodeError:
        print("error: entry is not valid UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(encoded + b"\n")

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
