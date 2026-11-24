"""make.fun entry: Funniest Autocorrect Fail.

Stdlib-only, deterministic: writes one line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Never deletes anything.
"""

import os
from pathlib import Path

LINE = "I texted my date 'can't wait to see you' but autocorrect changed it to 'can't wait to sue you', so dinner is now a deposition."

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate: 1-200 chars of non-whitespace UTF-8 text, one line only.
    # Judge weighs clarity of the slip, surprise of the wrong word, first-read landing.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200
    assert "\n" not in LINE
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)

if __name__ == "__main__":
    main()
