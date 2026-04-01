import argparse 
import os

parser = argparse.ArgumentParser(
    prog="ls shell tool",
    description="making ls tool with python"
)

parser.add_argument(
    "-1",
    dest="one_per_line",
    action="store_true",
    help="lists one per line"
)
parser.add_argument(
    "-a",
    dest="show_hidden",
    action="store_true",
    help="show files even hidden files"
)
parser.add_argument(
    "items",
    nargs="*", #defualt to current directory
    help="items to list"
)

args = parser.parse_args()

paths = args.items if args.items else ['.']

for path in paths:
    try:
        entries = os.listdir(path)
        if not args.show_hidden:
            entries = [e for e in entries if not e.startswith(".")]
        if args.one_per_line:
            for entry in entries:
                print(entry)
        else:
            print(" ".join(entries))
    except:
        print(f"ls can not access this directory: {path}")
