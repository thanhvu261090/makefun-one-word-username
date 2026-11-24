"""make.fun entry: One Word, One Username, One Reward.

The entry is my own make.fun username, one word and nothing else.
Python 3.13, standard library only, no network.
"""

import sys
from pathlib import Path

# My own make.fun handle, sent as a single word with no explanation.
ENTRY = "thanhvu261090"

OUTPUT_PATH = Path("/output/entry.txt")


def gate_check(text: str) -> None:
    """Enforce the competition gate: UTF-8 text of 1 to 30 characters,
    not only white space, a single word with no spaces or padding."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry must be 1 to 30 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must have no leading or trailing padding")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word with no spaces")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must contain no control characters")
    if not all(ch.isalnum() or ch in "-_" for ch in text):
        raise ValueError("entry must be a username word: letters, digits, - or _ only")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    gate_check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    gate_check(written)
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}: {written}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
