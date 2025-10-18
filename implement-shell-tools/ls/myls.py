import argparse
import os

parser = argparse.ArgumentParser(
    prog="myls",
    description="List directory contents like the ls command"
)

parser.add_argument("-1", dest="one_per_line", action="store_true",
                    help="List one file per line")
parser.add_argument("-a", dest="all_files", action="store_true",
                    help="Include hidden files starting with '.'")
parser.add_argument("path", nargs="?", default=".", help="Directory to list (default: current directory)")

args = parser.parse_args()

try:
    entries = os.listdir(args.path)
except FileNotFoundError:
    print(f"my_ls: cannot access '{args.path}': No such file or directory")
    exit(1)

if not args.all_files:
    entries = [e for e in entries if not e.startswith('.')]

entries.sort()

if args.one_per_line:
    for entry in entries:
        print(entry)
else:
    print("  ".join(entries))
