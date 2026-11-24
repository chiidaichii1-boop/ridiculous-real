"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence pitching a bizarre startup that turns out to be a
real business: a candle blended to smell exactly like the buyer's
childhood home, rebuilt from a postcode and a single memory.
"""

import os

PITCH = (
    "Send us your postcode and one childhood memory, and we bottle the "
    "smell of your childhood home as a candle — homesick adults pay $38 "
    "a tin to miss somewhere on purpose."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
