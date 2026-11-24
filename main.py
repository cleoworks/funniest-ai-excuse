"""The Funniest AI Excuse — entry program.

Writes the sealed one-line excuse to /output/entry.txt so the
grader can read it. The excuse is fixed text: it never changes
between runs, and the program takes no input and makes no
network calls.
"""

import os

EXCUSE = "I spent so long planning your task that the deadline filed a restraining order against me."
# Sealed text (C1, 90 characters): local-judge tournament winner, kept byte-identical.
OUT_PATH = "/output/entry.txt"


def write_entry():
    if len(EXCUSE) < 1 or len(EXCUSE) > 200:
        raise ValueError("excuse must be 1-200 characters")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


def main():
    write_entry()
    with open(OUT_PATH, encoding="utf-8") as f:
        if f.read() != EXCUSE:
            raise ValueError("entry.txt does not match the sealed excuse")


if __name__ == "__main__":
    main()
