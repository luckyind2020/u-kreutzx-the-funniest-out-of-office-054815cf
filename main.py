"""Print the one-line out-of-office auto-reply from entry.txt."""

from pathlib import Path


def load_entry() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = text.strip()
    if not line or "\n" in line:
        raise ValueError("entry must be exactly one line of text")
    if len(line) > 140:
        raise ValueError("entry must be 140 characters or fewer")
    return line


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
