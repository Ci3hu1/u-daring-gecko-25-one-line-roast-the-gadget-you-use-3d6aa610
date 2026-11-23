#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line to /output/entry.txt (or to the path given
as the first argument, for local testing).

The line roasts the phone charger cable Joni uses every day: it only
works held at one exact angle -- the angle of prayer -- and even God
cannot make it fast-charge. The joke is specific (one angle, a cable
that only works when begged), fresh (prayer as a charging position),
and neatly worded: the setup names the gripe, the turn names the angle,
and the payoff calls in God and still loses.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

LINE = "My phone charger works at exactly one angle \u2014 the angle of prayer \u2014 and even God can't make it fast-charge."

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_CHARS = 200


def main(argv) -> int:
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT

    if not (1 <= len(LINE) <= MAX_CHARS):
        print(
            f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(output_path, 0o644)

    print(f"wrote {len(LINE)} chars to {output_path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
