"""Five Seconds to Explain the Glass.

A house cat delivers its one-sentence defence, in five seconds flat,
for knocking a glass off the table. No apology, no confession:
the glass was given notice and refused to leave the sunspot.
"""

import os
import sys

LINE = "I gave that glass three days to move out of my sunspot and it refused, so I evicted it the only way the lease allows."

MAX_CHARS = 200


def validate(line):
    """Check the line fits the bounty: one sentence, 1-200 chars, clean edges."""
    if not line:
        raise ValueError("line must not be empty")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the 200-char limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.endswith("."):
        raise ValueError("line must be one complete sentence ending in a period")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
