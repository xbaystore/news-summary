#!/usr/bin/env python3
"""make.fun bounty news-summary-01 entry.

Writes the repository's summary of 11 November 2026's world news to
/output/entry.txt, byte for byte. Standard library only, no network,
and every run writes identical bytes.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "summary.txt"), "rb") as fh:
        data = fh.read()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
