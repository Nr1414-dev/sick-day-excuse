#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — one line under 200 characters.

A bee stings the sender's eyelid, so the face looks permanently
suspicious and has to stay home until it stops accusing people.
"""
import os

ENTRY = "A bee stung my eyelid and now I look permanently suspicious, so I'm staying home until my face stops accusing people."


def main():
    # Gate guard: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space.
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    # Read-back check: what landed on disk must be exactly the entry.
    with open(path, encoding="utf-8") as handle:
        if handle.read() != ENTRY:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
