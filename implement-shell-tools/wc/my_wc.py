import os
import sys
import argparse

# CLI argument parsing
parser = argparse.ArgumentParser(description="Simplified implementation of wc")
parser.add_argument("paths", nargs="*", default=["."], help="One or more file or directory paths")
parser.add_argument("-l", "--line", action="store_true", help="Count lines")
parser.add_argument("-w", "--word", action="store_true", help="Count words")
parser.add_argument("-c", "--character", action="store_true", help="Count characters")

args = parser.parse_args()
file_paths = args.paths

# Fallback: if no options passed, show all
show_line = args.line
show_word = args.word
show_char = args.character
show_all = not (show_line or show_word or show_char)

# Count content in a string
def count_content(content):
    lines = content.splitlines()
    words = content.strip().split()
    characters = len(content)
    return len(lines), len(words), characters

# Totals for multiple files
total = {
    "lines": 0,
    "words": 0,
    "characters": 0
}

file_count = 0

for input_path in file_paths:
    try:
        if os.path.isdir(input_path):
            print(f"{input_path} is a directory. Skipping.")
            continue

        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        lines, words, characters = count_content(content)

        total["lines"] += lines
        total["words"] += words
        total["characters"] += characters
        file_count += 1

        # Prepare output per file
        output_parts = []
        if show_line or show_all:
            output_parts.append(f"{lines:8}")
        if show_word or show_all:
            output_parts.append(f"{words:8}")
        if show_char or show_all:
            output_parts.append(f"{characters:8}")

        output_parts.append(input_path)
        print(" ".join(output_parts))

    except Exception as e:
        print(f'Error reading "{input_path}": {e}', file=sys.stderr)

# Print totals if more than one file processed
if file_count > 1:
    output_parts = []
    if show_line or show_all:
        output_parts.append(f"{total['lines']:8}")
    if show_word or show_all:
        output_parts.append(f"{total['words']:8}")
    if show_char or show_all:
        output_parts.append(f"{total['characters']:8}")
    output_parts.append("total")
    print(" ".join(output_parts))
