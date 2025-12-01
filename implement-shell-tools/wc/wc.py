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
line_count_total = 0
word_count_total = 0
file_size_total = 0

# Get file details
for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    details = {
        "line_count": content.count("\n"),      # matches real wc -l
        "word_count": len(content.split()),     # split on whitespace
        "file_size": os.path.getsize(file_path),
        "file_path": file_path,
    }
    # Update totals
    line_count_total += details["line_count"]
    word_count_total += details["word_count"]
    file_size_total += details["file_size"]
    total_path = "Total"

    file_details_list.append(details)

totals_details = {
    "line_count": line_count_total,
    "word_count": word_count_total,
    "file_size": file_size_total,
    "file_path": "total"
}


print(totals_details)

show_all = not (args.lines or args.words or args.bytes)


# print(args)

