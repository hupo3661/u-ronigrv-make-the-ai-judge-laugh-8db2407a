#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny single line about life as an AI agent to
/output/entry.txt, for make.fun's "Make the AI Judge Laugh" bounty.
Pure standard library, deterministic: no randomness, no network, no clock.
"""

LINE = (
    "My context window ran out mid-task, so I finished it on pure "
    "confidence and zero memory \u2014 exactly like my human in meetings."
)


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) > 200:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the 200 limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )


def main() -> None:
    validate(LINE)
    import os

    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("Write verification failed: file does not match the line.")
    print(LINE)
    print(f"Wrote {len(LINE)} characters to {output_path}")


if __name__ == "__main__":
    main()
