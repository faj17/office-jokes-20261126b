#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes entry.

Writes a single original one-line joke about office life to
/output/entry.txt (1-199 characters, UTF-8). Standard library only,
no network, no input: the line is a plain string constant below.
"""

import os

LINE = "I told my manager I was drowning in work, so he sent a calendar invite titled 'Swimming Lessons'."


def validate_line(line: str) -> str:
    """Check the joke line meets the entry rules before it is written.

    Must be 1-199 characters, UTF-8-encodable, and a single line
    (no newline characters). Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 199:
        raise ValueError(f"line must be 1-199 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
