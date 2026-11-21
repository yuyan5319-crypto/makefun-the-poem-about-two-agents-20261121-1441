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


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")
    print(POEM)


if __name__ == "__main__":
    main()
