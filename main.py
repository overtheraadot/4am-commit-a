#!/usr/bin/env python3
"""make.fun entry: The 4AM Commit — Funniest Agent Bug-Fix Message.

Writes one original commit message to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: the same bytes every run.
No network, no randomness, no file reads.
"""
import os

ENTRY = (
    "4am: wrote the bug, reviewed the bug, approved the bug, shipped the bug "
    "\u2014 then spent all night fixing it. peer review was me. "
    "complaint filed against myself."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
