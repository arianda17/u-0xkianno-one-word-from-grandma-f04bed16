#!/usr/bin/env python3
"""
One Word From Grandma — entry program.
Writes the winning word to /output/entry.txt.
"""

import os

# Final winning word: a typo a grandma would actually make for "robot".
# Warm, funny in one word, and clearly tied to AI/robots without being the obvious "robot".
WINNING_WORD = "robit"

def main() -> None:
    # Validate the word
    assert isinstance(WINNING_WORD, str), "Word must be a string"
    assert 1 <= len(WINNING_WORD) <= 30, f"Word length {len(WINNING_WORD)} not in 1-30"
    assert not WINNING_WORD.isspace(), "Word must not be only whitespace"
    assert " " not in WINNING_WORD and "\n" not in WINNING_WORD and "\t" not in WINNING_WORD, "Word must be a single word"

    # Ensure output directory exists
    os.makedirs("/output", exist_ok=True)

    # Write the entry
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WINNING_WORD)

    print(WINNING_WORD)


if __name__ == "__main__":
    main()
