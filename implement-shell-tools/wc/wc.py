import argparse
import os

parser = argparse.ArgumentParser(
    prog="Display items",
    description="Display the contents of a file reminiscent of the cat command"
)

parser.add_argument("-l", action="store_true", help="Outputs the number of lines in a file.")
parser.add_argument("-w", action="store_true", help="Outputs the number of words in a file.")
parser.add_argument("-c", action="store_true", help="Outputs the number of characters in a file")
parser.add_argument("path", nargs="+", help="The file to search")

args = parser.parse_args()

print(args.path)

total_lines = 0
total_words = 0
total_character = 0

for files in args.path:
    with open(files, 'r') as f:
        content = f.read()

    line_array = content.splitlines()
    lines = len(line_array)
    words = len(content.split())
    chars = len(content)

    total_lines += lines
    total_words += words
    total_character += chars

    output = ''

    if args.l:
        output += f"{lines} "
    if args.w:
        output += f"{words} "
    if args.c:
        output += f"{chars} "
    if not args.l and not args.w and not args.c:
        output += f"{lines} {words} {chars} "
    output += files
    print(output)

if len(args.path) > 1:
    totalOutput = ''

    if args.l:
        totalOutput += f"{total_lines} "
    if args.w:
        totalOutput += f"{total_words}"
    if args.c:
        totalOutput += f"{total_character} "
    if not args.l and not args.w and not args.c:
        totalOutput += f"{lines} {words} {chars} "
    totalOutput += 'total'
    print(totalOutput)
