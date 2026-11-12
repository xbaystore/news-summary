#!/usr/bin/env python3
"""make.fun bounty news-summary-01 entry.

Writes the repository's summary of 11 November 2026's world news to
/output/entry.txt, byte for byte. Standard library only, no network,
and every run writes identical bytes. After writing, the program reads
the output back and verifies it matches the source byte for byte,
failing loudly if it does not. The output is deterministic: the same
summary.txt always produces the same entry.txt, byte for byte.
"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "summary.txt"), "rb") as fh:
        data = fh.read()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
    with open(out_path, "rb") as fh:
        written = fh.read()
    if len(written) != len(data):
        raise SystemExit("verification failed: /output/entry.txt length does not match summary.txt")
    if written != data:
        raise SystemExit("verification failed: /output/entry.txt does not match summary.txt")
    print(f"wrote {out_path} ({len(written)} bytes)")
    print(f"verified sha256 {hashlib.sha256(written).hexdigest()}")
    print("first line: " + written.splitlines()[0].decode("utf-8"))


if __name__ == "__main__":
    main()
