"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (at most 280 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt: a childhood memory grounded in a
concrete sensation — the rice cooker clicking at five o'clock, a
grandmother lifting the lid, steam that smells like every summer
ever missed.
"""

import os
import sys

ENTRY = (
    "When the rice cooker clicked at five o'clock, my grandmother "
    "lifted the lid with a folded dish towel, and the steam smelled "
    "like every summer I have ever missed."
)

MAX_CHARS = 280


def validate(text: str) -> str:
    """Enforce the competition gate: UTF-8 text of 1-280 characters,
    not only whitespace, a single clean sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} cap"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no line breaks")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.endswith((".", "!", "?")):
        raise ValueError("entry must end with terminal punctuation")
    if len(text.split()) < 4:
        raise ValueError("entry is too short to be a sentence")
    if "  " in text or "\t" in text:
        raise ValueError("entry must not contain double spaces or tabs")
    # The judge's criteria, in order: a childhood memory that feels
    # nostalgic, grounded in a concrete sensation. Require at least one
    # sensory cue (smell, sound, touch) and one memory anchor so a
    # generic greeting-card line cannot slip through.
    sensory = ("smell", "smelled", "scent", "steam", "clicked", "sound",
               "heard", "taste", "tasted", "warm", "cool", "barefoot")
    if not any(word in text.lower() for word in sensory):
        raise ValueError("entry must carry a concrete sensory detail")
    anchors = ("grandmother", "grandfather", "mother", "father", "childhood",
               "eight", "nine", "ten", "years old", "summer", "kitchen",
               "school", "yard", "old house")
    if not any(word in text.lower() for word in anchors):
        raise ValueError("entry must anchor the memory in a person, "
                         "place or time")
    return text


def main() -> int:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("verification failed: entry.txt does not match ENTRY")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
