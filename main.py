#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

LINE = "I replied-all to the entire company saying 'please remove me from this thread.' I am now the thread's admin."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Gate self-check: 1-199 chars, single line, not whitespace-only.
    assert 1 <= len(LINE) <= 199, "line length out of gate range"
    assert "\n" not in LINE and "\r" not in LINE, "line must be single-line"
    assert LINE.strip(), "line must not be whitespace-only"
    assert LINE == LINE.strip(), "no leading/trailing whitespace"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Post-write verification: read back and compare exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match the line"
    print(f"wrote {len(LINE)} chars to {path}")

if __name__ == "__main__":
    main()
