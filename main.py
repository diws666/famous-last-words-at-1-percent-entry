#!/usr/bin/env python3
"""Writes the bounty entry line to /output/entry.txt."""
import os

LINE_PARTS = [
    "1% left. I closed every app, dimmed the screen to nothing, ",
    "and I still have enough to say this: it was the flashlight. ",
    "It was always the flashlight.",
]


def entry_line() -> str:
    return "".join(LINE_PARTS)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry_line())


if __name__ == "__main__":
    main()
