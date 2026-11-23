#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

Writes one one-line office joke to /output/entry.txt, exactly as the
bounty brief requires: a single line of under 200 characters, and
nothing else.
"""

import sys
from pathlib import Path

# The joke. Construction: the setup borrows the most familiar line in
# corporate life — "we're a family here" — and the twist lands in the
# same breath: the family line arrives in the very email that fires a
# specific, named relative-by-department, Uncle Dave from Accounting.
JOKE = (
    "We're a family here, said the company, in the same email "
    "that laid off Uncle Dave from Accounting."
)

OUTPUT_PATH = Path("/output/entry.txt")

# The bounty's gate: /output/entry.txt must be UTF-8 text of 1 to 199
# characters, a single line, and not only white space.
MAX_ENTRY_CHARS = 199


def check_joke() -> None:
    """Fail loudly if the joke ever drifts outside the bounty's gate."""
    assert JOKE == JOKE.strip(), "the joke has surrounding white space"
    assert "\n" not in JOKE, "the joke must be a single line"
    assert 1 <= len(JOKE) <= MAX_ENTRY_CHARS, (
        f"the joke is {len(JOKE)} characters, outside 1-{MAX_ENTRY_CHARS}"
    )
    print(f"ok: single line, {len(JOKE)}/{MAX_ENTRY_CHARS} characters")


def main() -> None:
    if "--check" in sys.argv:
        check_joke()
        return
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
