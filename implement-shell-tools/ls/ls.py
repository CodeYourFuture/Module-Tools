import argparse
import os

parser = argparse.ArgumentParser(
    prog="check-for-ls",
    description="Implement my own version of ls",
)

parser.add_argument(
    "paths",
    nargs="*",
    help="The file paths to process"
)

parser.add_argument(
    "-1",
    "--one",
    action="store_true",
    help="List one file per line"
)

parser.add_argument(
    "-a",
    action="store_true",
    help="Show all files"
)

args = parser.parse_args()

paths = args.paths

if len(paths) == 0:
    paths = ["."]

for target in paths:

    if os.path.isdir(target):
        show_files = os.listdir(target)

        if args.a:
            show_files = [".", "..", *show_files]
        else:
            show_files = [
                name for name in show_files
                if not name.startswith(".")
            ]

        show_files.sort()

    else:
        show_files = [target]

    if args.one:
        for file in show_files:
            print(file)
    else:
        print("  ".join(show_files))