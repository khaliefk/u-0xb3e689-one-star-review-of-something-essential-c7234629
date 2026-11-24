"""One-star review of something essential.

Writes a single deadpan one-star review, at most 160 characters,
to entry.txt in the output directory.
"""

import os

REVIEW = (
    "One star. Gravity ignores me on every high shelf, "
    "then catches my phone the instant I drop it."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
