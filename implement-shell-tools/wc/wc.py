import argparse

parser = argparse.ArgumentParser(prog="wc")
parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
parser.add_argument("files", nargs="+")

args = parser.parse_args()


def format_counts(lines, words, chars):
    if not args.l and not args.w and not args.c:
        return f"{lines:8}{words:8}{chars:8}"

    output = ""

    if args.l:
        output += f"{lines:8}"
    if args.w:
        output += f"{words:8}"
    if args.c:
        output += f"{chars:8}"

    return output


total_lines = 0
total_words = 0
total_chars = 0

for file in args.files:
    with open(file, "r") as f:
        text = f.read()

    lines = text.count("\n")

    stripped = text.strip()
    words = len(stripped.split()) if stripped else 0

    chars = len(text.encode())

    total_lines += lines
    total_words += words
    total_chars += chars

    print(format_counts(lines, words, chars), file)


if len(args.files) > 1:
    print(
        format_counts(total_lines, total_words, total_chars),
        "total"
    )