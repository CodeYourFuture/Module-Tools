import argparse
import sys

parser = argparse.ArgumentParser(
    prog="cat",
    description="Prints the content of files"
)

parser.add_argument(
    "-n",
    "--number",
    action="store_true",
    help="Numbers all lines"
)

parser.add_argument(
    "-b",
    "--number-nonblank",
    action="store_true",
    help="Number non-empty lines"
)

parser.add_argument(
    "paths",
    nargs="+",
    help="The file to print"
)

args = parser.parse_args()

line_number = 1


def number_lines(lines, line_number, include_blank_lines):
    numbered_lines = []

    for line in lines:
        if include_blank_lines or line != "\n":
            numbered_line = str(line_number).rjust(6) + "  " + line
            numbered_lines.append(numbered_line)
            line_number += 1
        else:
            numbered_lines.append(line)

    return numbered_lines, line_number


for path in args.paths:
    with open(path, "r") as file:
        lines = file.readlines()

        if args.number_nonblank:
            lines, line_number = number_lines(
                lines,
                line_number,
                False
            )
        elif args.number:
            lines, line_number = number_lines(
                lines,
                line_number,
                True
            )

        output = "".join(lines)
        sys.stdout.write(output)