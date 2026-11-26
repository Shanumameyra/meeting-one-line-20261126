#!/usr/bin/env python3
"""Meeting-killer one-liner entry.

Writes a single sentence to /output/entry.txt (or entry.txt beside this
file when /output does not exist). Deterministic: no network, no randomness.
"""

import os

LINE = "We already decided this in the email nobody read, so this meeting is just that email with worse lighting and no mute button."


def main() -> None:
    out = "/output/entry.txt"
    if not os.path.isdir("/output"):
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
