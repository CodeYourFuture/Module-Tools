import argparse
import sys
import os

parser = argparse.ArgumentParser(
    prog="wc",
    description="Print newline, word, and byte counts for files"
)

parser.add_argument(
    "-l",
    "--lines",
    action="store_true",
    help="Print the newline counts"
)

parser.add_argument(
    "-w",
    "--words",
    action="store_true",
    help="Print the word counts"
)

parser.add_argument(
    "-c",
    "--bytes",
    action="store_true",
    help="Print the byte counts"
)

parser.add_argument(
    "paths",
    nargs="*",
    help="The file to print"
)

args = parser.parse_args()

total_line_count = 0
total_word_count = 0
total_byte_count = 0

rows = []

def get_counts(path):
    with open(path, "r") as file:
        content = file.readlines()

        lines_count = len(content)

        joined_content = "".join(content)

        words = joined_content.split()
        word_count = len(words)

        byte_count = len(joined_content.encode())

        return lines_count, word_count, byte_count


def select_count(lines_count, word_count, byte_count):
    selected_counts = []

    if args.lines:
        selected_counts.append(lines_count)

    if args.words:
        selected_counts.append(word_count)

    if args.bytes:
        selected_counts.append(byte_count)

    if len(selected_counts) == 0:
        selected_counts.append(lines_count)
        selected_counts.append(word_count)
        selected_counts.append(byte_count)

    return selected_counts


for path in args.paths:
    lines_count, word_count, byte_count = get_counts(path)

    total_line_count += lines_count
    total_word_count += word_count
    total_byte_count += byte_count

    selected_counts = select_count(
        str(lines_count),
        str(word_count),
        str(byte_count)
    )

    rows.append((selected_counts, path))
    
if len(args.paths) > 1:
    total_counts = select_count(
        str(total_line_count),
        str(total_word_count),
        str(total_byte_count)
    )
    rows.append((total_counts, "total"))

padding = max(
    len(count)
    for counts, _ in rows
    for count in counts
)

output = []

for counts, path in rows:
    padded_counts = []

    for count in counts:
        padded_counts.append(count.rjust(padding))

    output.append(" ".join(padded_counts) + " " + path)

print("\n".join(output))