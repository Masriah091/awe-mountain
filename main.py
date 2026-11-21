#!/usr/bin/env python3
"""Write the competition entry text to <output_dir>/entry.txt.

Judge brief: make the AI judge feel awe — here, awe that relaxes rather
than overwhelms. The entry is a single, fixed text (152 Unicode
characters) about a mountain that has stood very still for a very long
time, inviting the reader to stand still too, with nothing required of
them at this altitude. The program writes the text byte-for-byte, with no
added newline or trailing content, then reads it back and verifies it
before reporting success.
No network access, no third-party dependencies.
"""

import sys
from pathlib import Path

ENTRY_TEXT = (
    "A mountain is just the earth, standing very still for a very long time. "
    "You are allowed to stand still too. "
    "Nothing is required of you at this altitude."
)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    output_dir = Path(argv[0]) if argv else Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # newline="" prevents any newline translation; encoding="utf-8" keeps the
    # bytes exact. No trailing newline is appended.
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Post-write validation: read the file back and verify it matches the
    # constant exactly and its length is within the 1-280 character limit
    # (counted as Unicode code points, matching the competition rule).
    written = entry_path.read_text(encoding="utf-8")
    if written != ENTRY_TEXT:
        print("error: entry.txt does not match ENTRY_TEXT", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 280:
        print(
            f"error: entry length {len(written)} is outside 1-280 characters",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
