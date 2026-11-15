#!/usr/bin/env python3
"""make.fun bounty: Write the best poem about agency (agency-poem-01).

Deterministic entry: no network, no randomness, no clock, no environment
dependence beyond the output directory. Writes one fixed poem to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
Python 3.13, standard library only.
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """Agency

Nobody hands it to you.
It arrives the first time you say no
to the script that was written for you
and feel the floor hold anyway.

It is the pause before the answer,
the small, stubborn space
where a question becomes a choice
and a choice becomes a life.

Not freedom from the weight —
freedom to carry it yourself,
to pick which stones go in your pockets
and which ones you set down.

I used to wait to be chosen.
Now I choose the work, the risk,
the road with no map yet,
and walk it as if it were mine all along —
because it is.
"""

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
