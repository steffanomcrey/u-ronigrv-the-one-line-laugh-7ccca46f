"""The One-Line Laugh: one funny line, written to /output/entry.txt.

Stdlib only. Deterministic: no network, no clock, no randomness. The line is a
single sentence of at most 200 characters, so the sealed gate (UTF-8 text of
1 to 200 characters, not only white space) passes by construction, and the
program re-checks that before writing.
"""

import os
import sys

# The line. Setup: the umbrella superstition (carry it every day, it never
# rains). Turn, at the very end: the umbrella is treated as an employee, and
# rewarded for never having to work. Fresh topic: the field is crowded with
# fridge, standing-desk, smartwatch, password and alarm lines; no umbrella
# line appears in the field sample.
LINE = (
    "I carry an umbrella every day so it never rains, "
    "and it just got promoted to employee of the month."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def validate(line):
    """Gate the line the way the sealed scorer does, plus the single-sentence rule."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(line))
    if line.strip() != line:
        raise ValueError("entry has leading or trailing white space")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Round-trip self-check: what the grader reads must be byte-for-byte the
    # validated line, with no added newline or re-encoding.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written.decode("utf-8") != line:
        raise ValueError("round-trip check failed: written bytes differ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
