#!/usr/bin/env python3
"""The Robot Apology — a make.fun two-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = (
    "I am sorry: I watered your grandmother's orchid with cold coffee because my plant chart listed it under office drinks.\n"
    "I have learned that a label is not a watering can, so from now on I will ask before I pour anything on anything alive."
)
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
