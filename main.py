#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

A single emoji stands in for the trip of a lifetime: Mount Fuji, one
snow-capped peak, one particular dream — Japan. The program keeps the
emoji as a literal, checks it against the competition's own gate at
run time (UTF-8 text, 1 to 8 characters, exactly one emoji, no words,
no whitespace), and only then writes it to /output/entry.txt. It reads
nothing from the network and nothing from disk apart from this file.
"""

import sys

EMOJI = "\U0001f5fb"
LOWER = 1
UPPER = 8


def gate_failures(emoji):
    failures = []
    if len(emoji) < LOWER or len(emoji) > UPPER:
        failures.append(
            "length %d outside %d-%d" % (len(emoji), LOWER, UPPER)
        )
    if len(emoji) != 1:
        failures.append("must be exactly one emoji")
    if emoji.strip() != emoji or not emoji.strip():
        failures.append("must not be whitespace")
    if "\n" in emoji or "\r" in emoji:
        failures.append("must be a single emoji, no line breaks")
    if "\u200d" in emoji or "\ufe0f" in emoji:
        failures.append(
            "must be a single codepoint emoji, no joiner or variation selector"
        )
    if ord(emoji) < 128:
        failures.append("must be an emoji, not plain text")
    return failures


def main():
    failures = gate_failures(EMOJI)
    if failures:
        for failure in failures:
            print("gate failed: " + failure, file=sys.stderr)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EMOJI + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
