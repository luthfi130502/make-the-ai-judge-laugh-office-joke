#!/usr/bin/env python3
"""Entry for make.fun bounty u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

Writes one original office joke (single line, 1-200 chars, UTF-8)
to /output/entry.txt.
"""

from pathlib import Path

JOKE = (
    "To keep the daily standup under fifteen minutes, we removed all the chairs. "
    "That was 2019. The meeting never ended, and the chairs now hold their own standup without us."
)


def main() -> None:
    text = JOKE.strip()
    assert text, "joke must not be empty"
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke length {len(text)} outside 1-200 gate"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
