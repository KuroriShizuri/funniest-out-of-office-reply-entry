"""funniest-out-of-office-reply — one line, the funniest AI out-of-office reply.

The idea behind the entry: the joke works because it treats the AI's
own machinery as the thing that went on holiday. A context window
"going off to find itself" is a human soul-searching cliche told in
machine terms, and "left without saving" is the specifically
machine-flavoured disaster that makes it land — an AI that loses its
own memory the moment it tries to relax. The punchline then flips the
usual auto-reply script: instead of promising a human will help, it
sends the reader to a human with the deadpan warning that humans
forget things too, just slower. The machine voice carries the joke,
the turn is a surprise rather than a pun, and there is no beach,
no inbox pile-up and no "back soon". The line is 149 characters,
inside the 160 limit with room to spare.

The program itself is deliberately tiny: it writes that one fixed text
to /output/entry.txt, checks it is a single line within the 160
character limit, and nothing else. No network, no randomness, no
arguments — the same run always produces the same file.
"""

import os
import sys

# The entry, exactly as submitted: one line, no trailing newline.
ENTRY = (
    "Out of office: my context window went off to find itself "
    "and left without saving. If it is urgent, ask a human - "
    "they forget things too, just slower."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 160


def main() -> int:
    """Validate the text and write it to the output path."""
    if not ENTRY:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CODE_POINTS:
        print(
            "error: entry is %d code points, over the %d limit"
            % (len(ENTRY), MAX_CODE_POINTS),
            file=sys.stderr,
        )
        return 1
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and re-check what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("error: written entry differs from ENTRY", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= MAX_CODE_POINTS:
        print(
            "error: written entry is %d code points" % len(written),
            file=sys.stderr,
        )
        return 1
    print("wrote %d characters to %s" % (len(written), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
