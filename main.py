#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry.

Writes a single original one-line joke about office life to
/output/entry.txt (1-199 characters, UTF-8). Standard library only,
no network, no input: the line is a plain string constant below.
"""

import os

LINE = "I told my manager I was drowning in work, so he sent a calendar invite titled 'Swimming Lessons'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
