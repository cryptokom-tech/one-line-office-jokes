#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

LINE = "I replied-all to the entire company saying 'please remove me from this thread.' I am now the thread's admin."

def validate(line):
    """Return line if it satisfies the one-line entry gate."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be empty")
    if not 1 <= len(line) <= 199:
        raise ValueError("line length out of gate range")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be single-line")
    if line != line.strip():
        raise ValueError("line must not have leading/trailing whitespace")
    return line

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = validate(LINE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write verification: read back, re-validate, and compare exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != line:
        raise ValueError("written entry does not match the line")
    print(f"wrote {len(line)} chars to {path}")

if __name__ == "__main__":
    main()
