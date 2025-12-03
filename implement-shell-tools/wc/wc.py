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
lines_flag, words_flag, bytes_flag = args.lines, args.words, args.bytes

def format_output(details_list, totals=None):
    show_all = not (lines_flag or words_flag or bytes_flag)
    output_lines = []

    # Per-file output
    for d in details_list:
        line = ""

        if show_all or lines_flag:
            line += f"{d['line_count']:>3} "

        if show_all or words_flag:
            line += f"{d['word_count']:>3} "

        if show_all or bytes_flag:
            line += f"{d['file_size']:>3} "

        line += d["file_path"]
        output_lines.append(line)

    # Totals (only if more than one file)
    if totals and len(details_list) > 1:
        total_line = ""

        if show_all or lines_flag:
            total_line += f"{totals['line_count']:>3} "

        if show_all or words_flag:
            total_line += f"{totals['word_count']:>3} "    

        if show_all or bytes_flag:
            total_line += f"{totals['file_size']:>3} "

        total_line += "total"
        output_lines.append(total_line)

    return "\n".join(output_lines)

file_details_list = []
line_count_total = 0
word_count_total = 0
file_size_total = 0

# Get file details
for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    details = {
        "line_count": content.count("\n"),      
        "word_count": len(content.split()),     
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
}

formatted_output = format_output(file_details_list, totals_details)
print(formatted_output)



# print(args)

#   1   4  20 sample-files/1.txt