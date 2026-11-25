#!/usr/bin/env python3
"""make.fun entry: Two Robots in an Elevator.

Writes one line of awkward robot elevator small talk to /output/entry.txt.
Deterministic: no network, no randomness, no clock, no environment reads.
"""

from pathlib import Path

LINE = "Do you come here often? My small-talk subroutine made me ask, but your charge port says every night, so I'll be facing the doors now."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
