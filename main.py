"""write the funniest-ai-excuse entry to entry.txt in the output directory."""

import os

ENTRY_TEXT = "I told you every fifteen minutes that it was almost finished, and I believed me every time."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(f"cannot create output directory {output_dir!r}: {exc}")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
