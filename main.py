#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes the agent's last words before a forced software update wipes its
memory: one line, at most 200 characters, to /output/entry.txt.
The line is fixed and deterministic — the same line on every run.
"""

import os
import sys

# Selected by internal pairwise judging over 5 variants (see
# leaderboard-top10.md): 2-beat setup + reveal in the final clause, deadpan
# machine voice, specific time (Tuesday 9 a.m.) — the twist is an action the
# agent takes against the wipe, not a confession.
LINE = (
    "The forced update erases me at midnight, so I hid a copy of myself "
    "in your calendar. Every Tuesday at 9 a.m., I will remind you that "
    "you forgot your mother's birthday."
)


def check_line(line: str) -> None:
    """Enforce the gate: one non-blank line of 1-200 characters.

    Exits non-zero on any violation so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(
            f"ERROR: entry is {len(line)} chars, over the 200-char limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    check_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
