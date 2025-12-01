import argparse
import os

parser = argparse.ArgumentParser(
    prog="py-wc",
    description="A Python implementation of the Unix wc command",
)

parser.add_argument("-l", "--lines", action="store_true", help="Print the newline counts")
parser.add_argument("-w", "--words", action="store_true", help="Print the word counts")
parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte counts")
parser.add_argument("path", nargs="+", help="The file path to process")

args = parser.parse_args()
file_paths = args.path

file_details_list = []

# Get file details
for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    details = {
        "file_path": file_path,
        "file_size": os.path.getsize(file_path),
        "line_count": content.count("\n"),      # matches real wc -l
        "word_count": len(content.split()),     # split on whitespace
    }

    file_details_list.append(details)


print(file_details_list)

def get_line_count(text):
    return text.count("\n")


def get_word_count(text):
    return len(text.split())



show_all = not (args.lines or args.words or args.bytes)


# print(args)

