import argparse

parser = argparse.ArgumentParser(
    prog="wc.py",
    description="Count lines, words, and characters in text files."
)

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count characters")

parser.add_argument("files", nargs="+", help="Text files to read")

args = parser.parse_args()

# Totals for multiple files
total_lines = 0
total_words = 0
total_chars = 0

# Loop through each file
for file_path in args.files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    line_count = content.count("\n")
    word_count = len(content.split())
    char_count = len(content)

    total_lines += line_count
    total_words += word_count
    total_chars += char_count

    # Prepare output per file
    output = []

    if args.l:
        output.append(str(line_count))
    if args.w:
        output.append(str(word_count))
    if args.c:
        output.append(str(char_count))

    # If no flag is given, show all
    if not (args.l or args.w or args.c):
        output = [str(line_count), str(word_count), str(char_count)]

    output.append(file_path)
    print(" ".join(output))

# Show total only if multiple files given
if len(args.files) > 1:
    total_output = []

    if args.l:
        total_output.append(str(total_lines))
    if args.w:
        total_output.append(str(total_words))
    if args.c:
        total_output.append(str(total_chars))

    if not (args.l or args.w or args.c):
        total_output = [str(total_lines), str(total_words), str(total_chars)]

    total_output.append("total")
    print(" ".join(total_output))
