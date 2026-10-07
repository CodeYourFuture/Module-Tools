import argparse
import sys
import os

parser = argparse.ArgumentParser(
    prog="ls",
    description="List directory contents"
)

parser.add_argument(
    "-1",
    "--format",
    action="store_true",
    help="List one file per line"
)

parser.add_argument(
    "-a",
    "--all",
    action="store_true",
    help="Do not ignore entries starting with ."
)

parser.add_argument(
    "paths",
    nargs="*",
    help="The file to print"
)

args = parser.parse_args()

if args.format:
    separator = "\n"
else:
    separator = "  "

multiple_paths = len(args.paths) > 1

file_paths = []
directory_paths = []

if len(args.paths) == 0:
    args.paths.append(".")

for path in args.paths:
    if os.path.isfile(path):
        file_paths.append(path)

    elif os.path.isdir(path):
        directory_paths.append(path)

if len(file_paths) > 0:
    sys.stdout.write(separator.join(file_paths) + "\n")

for path in directory_paths:
    if multiple_paths:
        sys.stdout.write("\n" + path + ":\n")

    entries = os.listdir(path)
    entries.sort()

    if args.all:
        entries = [".", ".."] + entries

    else:
        visible_entries = []

        for entry in entries:
            if not entry.startswith("."):
                visible_entries.append(entry)

        entries = visible_entries

    sys.stdout.write(separator.join(entries) + "\n")