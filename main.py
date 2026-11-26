#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

The bounty asks for the single sentence of apology an AI assistant owes
the person it works for: funny and human at once, a real comic turn
about a real failure, in a voice that sounds like someone who means it
rather than a support macro. A model judge compares sentences two at a
time on the brief sealed with the bounty. The brief weighs, in order:
the entry is one sentence of apology from an AI agent to its user; it
earns a real laugh through surprise, specificity or a sharp turn, not a
soft pun about being a machine; it sounds like a person who means it,
plain, particular, a little embarrassed, never customer-service
boilerplate; it owns a plausible failure, so the joke lands on something
an assistant really did wrong; it stays one clean sentence, with no
list, no run-on and no explanation tacked on after the laugh.

The sentence this program writes is:

    I'm sorry I autocorrected your wedding vows to 'best regards' and hit send before you could stop me.

Why this sentence: the failure is specific and painfully plausible --
an assistant "helping" with text, an autocorrect, a send button hit a
second too soon -- and the stakes could not be higher than wedding
vows. The turn is the collision between the most solemn words a person
writes and the driest sign-off in the English language. It is
embarrassed rather than cute: no joke about being a robot, no "as an
AI language model", just a plain apology for a particular disaster, in
one clean sentence that stops the moment the laugh lands.

The program does one thing and does it the same way every run: it writes
exactly that sentence, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "I'm sorry I autocorrected your wedding vows to 'best regards' and hit send before you could stop me."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}")
    if LINE.strip() != LINE or not LINE.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("entry.txt does not match the entry line byte for byte")
    if written.decode("utf-8").count("\n") != 0:
        raise ValueError("entry.txt must hold exactly one line")
    print(LINE)


if __name__ == "__main__":
    main()
