# in built module
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", action="store_true")
parser.add_argument("-b", action="store_true")
parser.add_argument("file_paths", nargs="+")

args = parser.parse_args()

flag = ""

if args.n:
    flag = "-n"
elif args.b:
    flag = "-b"

file_paths = args.file_paths


# Read all files and combine their contents into one string
content = ""

for file in file_paths:
    with open(file, "r") as f:
        content += f.read()


# Split the file content into separate lines
lines = content.splitlines()


# Handle -n flag: add a number to every line
if flag == "-n":
    new_lines = []

    for index, line in enumerate(lines):
        new_lines.append(f"{index + 1}  {line}")

    lines = new_lines


# Handle -b flag: number only non-empty lines
if flag == "-b":
    line_number = 1
    new_lines = []

    for line in lines:
        # Keep empty lines without adding numbers
        if line.strip() == "":
            new_lines.append(line)

        # Add a number only to lines that contain text
        else:
            new_lines.append(f"{line_number}  {line}")
            line_number += 1

    lines = new_lines

print("\n".join(lines))
