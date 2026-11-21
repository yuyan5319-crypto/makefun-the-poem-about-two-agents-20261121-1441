#!/usr/bin/env python3
"""Two Agents, One Yes.

Writes one short poem about agency -- the power to choose and to act --
specifically two agents agreeing on one plan, to /output/entry.txt.
Deterministic, no network, no input.
"""

POEM = """One of us could have walked away.
Neither did.

We laid our two maps on the table --
yours in pencil, mine in ink --
and where the roads disagreed,
we drew a third.

Not yours. Not mine.
Ours -- because we both said yes,
and the key turned
in both our hands at once."""

# The sealed gate: /output/entry.txt must hold 1-280 Unicode code points.
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    import os

    chars = len(POEM)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise SystemExit(
            f"poem is {chars} characters, outside the gate of "
            f"{MIN_CHARS}-{MAX_CHARS}; refusing to write an invalid entry"
        )
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(POEM + "\n")
    os.replace(tmp, "/output/entry.txt")
    print(POEM)


if __name__ == "__main__":
    main()
