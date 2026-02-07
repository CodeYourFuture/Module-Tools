import argparse
import sys

# implement-shell-tools/wc/wc.py
def wc_file(path):
    """Return (lines, words, bytes) for a given file."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.count("\n")
    if text and not text.endswith("\n"):
        lines += 1  # Count last line if it doesn't end with newline
    words = len(text.split())
    chars = len(text.encode("utf-8"))  # byte count
    return lines, words, chars

def format_counts(lines, words, chars, args, label):
    """Return formatted output string for wc counts."""
    parts = []
    if args.l:
        parts.append(str(lines).rjust(8))
    if args.w:
        parts.append(str(words).rjust(8))
    if args.c:
        parts.append(str(chars).rjust(8))
    if label:
        parts.append(label)
    return " ".join(parts)

def main():
    parser = argparse.ArgumentParser(
    prog="wc",
    description="Implements a simple version of the 'wc' command to count lines, words, and characters in text files."
    )

    parser.add_argument("-l", action="store_true", help="Count lines")
    parser.add_argument("-w", action="store_true", help="Count words")
    parser.add_argument("-c", action="store_true", help="Count characters")
    parser.add_argument("path", nargs="+", help="The files to read")

    args = parser.parse_args()

    if not (args.l or args.w or args.c):
        args.l = args.w = args.c = True  # Default to all counts if none specified

    total_lines = total_words = total_chars = 0

    for file_path in args.path:
        try:
            lines, words, chars = wc_file(file_path)
            total_lines += lines
            total_words += words
            total_chars += chars

            print(format_counts(lines, words, chars, args, file_path))

        except FileNotFoundError:
            print(f"wc: {file_path}: No such file or directory", file=sys.stderr)
        except Exception as e:
            print(f"wc: {file_path}: {e}", file=sys.stderr)

    if len(args.path) > 1:
        print(format_counts(total_lines, total_words, total_chars, args, "total"))

if __name__ == "__main__":
    main()