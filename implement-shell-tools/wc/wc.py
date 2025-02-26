import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="word, line, and byte count",
)
parser.add_argument("-c", action="store_true", help="Output the number of bytes.")
parser.add_argument("-w", action="store_true", help="Output the number of words.")
parser.add_argument("-l", action="store_true", help="Output the number of lines.")
parser.add_argument("paths", nargs="+", help="Paths to list")
args = parser.parse_args()

show_all = not (args.c or args.w or args.l)
show_bytes = args.c or show_all
show_words = args.w or show_all
show_lines = args.l or show_all

def format_output_line(bytes, words, lines, path):
    line = ""
    if show_lines:
        line += f"{lines}".rjust(8)
    if show_words:
        line += f"{words}".rjust(8)
    if show_bytes:
        line += f"{bytes}".rjust(8)
    line += " " + path
    return line

total_bytes = 0
total_words = 0
total_lines = 0
for path in args.paths:
    with open(path, "r") as f:
        content = f.read()
    bytes = len(content)
    words = len(content.split())
    raw_lines = len(content.split("\n"))
    lines = raw_lines - 1 if content[-1] == "\n" else raw_lines
    total_bytes += bytes
    total_words += words
    total_lines += lines
    print(format_output_line(bytes, words, lines, path))

if len(args.paths) > 1:
    print(format_output_line(total_bytes, total_words, total_lines, "total"))
