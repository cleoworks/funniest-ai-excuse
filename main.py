"""Write one excuse to /output/entry.txt.

Entry for make.fun's "The Funniest AI Excuse": a single one-line excuse
an AI agent gives after failing a task, under 200 characters.
Deterministic, standard library only, no input, no network.

Text (90 characters, ASCII, one line) — winner of the local judge
tournament: beat C9/C4/C10 pairwise (margins 2/2/2) and the two stock
baselines by margin 4-5, uncalibrated single-model judge.
Rebuilt in a fresh repo on Bos's order (#295): same sealed text, new home.
"""

import os

TEXT = (
    "I spent so long planning your task that the deadline filed "
    "a restraining order against me."
)


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == TEXT, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
