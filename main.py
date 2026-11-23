#!/usr/bin/env python3
"""Dad Joke Showdown — one original dad joke, written to /output/entry.txt.

Pure stdlib Python 3.13. The joke is the whole entry.
"""

import os

JOKE = "My son asked me to stop making jokes about his height. I said, 'Sorry — it's a shortcoming.'"

# Gate: the entry must be one joke of 1-200 characters, no trailing
# explanation and no second line.
assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
