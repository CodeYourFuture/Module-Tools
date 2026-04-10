import argparse
import glob

# create parser
parser = argparse.ArgumentParser(description="Simple wc tool")

parser.add_argument("files", nargs="+", help="files to read")
parser.add_argument("-l", action="store_true", help="count lines")
parser.add_argument("-w", action="store_true", help="count words")
parser.add_argument("-c", action="store_true", help="count characters")

args = parser.parse_args()


# expand *.txt
def get_files(file_patterns):
    files = []
    for pattern in file_patterns:
        matched = glob.glob(pattern)
        if matched:
            files.extend(matched)
        else:
            files.append(pattern)
    return files


def count_file(file_name):
    try:
        with open(file_name, "r") as f:
            text = f.read()

            lines = text.count("\n")
            words = len(text.split())
            chars = len(text)

            return lines, words, chars

    except FileNotFoundError:
        print(f"Error: {file_name} not found")
        return 0, 0, 0


def print_result(lines, words, chars, file_name):
    # if no flags → show all
    if not args.l and not args.w and not args.c:
        print(lines, words, chars, file_name)

    else:
        output = []

        if args.l:
            output.append(str(lines))
        if args.w:
            output.append(str(words))
        if args.c:
            output.append(str(chars))

        output.append(file_name)
        print(" ".join(output))


# main
files = get_files(args.files)

total_lines = total_words = total_chars = 0

for file in files:
    lines, words, chars = count_file(file)

    total_lines += lines
    total_words += words
    total_chars += chars

    print_result(lines, words, chars, file)

# if multiple files → show total
if len(files) > 1:
    print_result(total_lines, total_words, total_chars, "total")