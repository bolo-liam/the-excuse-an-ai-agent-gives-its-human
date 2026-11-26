#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human -- make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest, most believable excuse an AI agent could give its human
for missing a deadline.
"""

import os

LINE = "I was on schedule until my context window filled up, so I evicted the deadline to make room for the apology you're reading now."

def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
