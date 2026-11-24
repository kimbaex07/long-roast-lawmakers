#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Reads the single satirical sentence from entry.txt next to this file,
validates the competition gate (UTF-8 text, 1-320 characters, not only
whitespace), and writes it byte-identical to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: output/entry.txt).

Pure Python standard library only.
"""

import os
import sys

MAX_CHARS = 320


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "entry.txt")

    with open(src_path, "rb") as f:
        data = f.read()

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        print("entry.txt is not valid UTF-8", file=sys.stderr)
        return 1

    if not 1 <= len(text) <= MAX_CHARS:
        print(
            "entry.txt must be 1-%d characters, got %d" % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1

    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)

    print("wrote %s (%d characters)" % (out_path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
