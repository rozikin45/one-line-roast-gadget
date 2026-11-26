#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<=200 chars) to /output/entry.txt.
Deterministic: same bytes on every run, from any working directory.
"""
import os
from pathlib import Path

LINE = (
    "My phone hits 4% at 4pm every day, then dims itself like it is "
    "clocking out early - the only thing in my life with a healthier "
    "work-life balance than me."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
