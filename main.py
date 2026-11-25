#!/usr/bin/env python3
"""The Robot Apology (make.fun).

Writes the entry -- a two-line robot confession: one sentence owning a specific
mistake, one naming the lesson and the fix --
to /output/entry.txt, where the sealed scorer reads it."""

import os

TEXT = 'I am sorry I sent the meeting notes to the whole company instead of just you — I mixed up reply and reply-all at 2 a.m. and trusted autocomplete.\nFrom now on I will read the address line out loud before I send anything, even when I am completely sure.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
