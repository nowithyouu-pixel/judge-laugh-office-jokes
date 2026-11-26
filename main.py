#!/usr/bin/env python3
"""Write one original office joke to /output/entry.txt.

The joke is a single line of under 200 characters: a setup about a
rare free hour on the calendar, then a punchline that turns it into
yet another meeting about being busy.
"""

import sys
from pathlib import Path

JOKE = (
    "My calendar finally showed a free hour, so naturally Outlook filled it "
    "with a meeting about why we're all so busy."
)

MAX_CHARS = 199


def main(argv):
    output = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    joke = JOKE.strip()
    if not joke or len(joke) > MAX_CHARS:
        raise SystemExit("joke must be 1-199 characters")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(joke + "\n", encoding="utf-8")
    print(f"wrote {len(joke)} characters to {output}")


if __name__ == "__main__":
    main(sys.argv)
