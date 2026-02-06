import argparse
import os

parser = argparse.ArgumentParser(
    prog="py-ls",
    description="A Python implementation of the Unix ls command",
)

parser.add_argument("-1", dest="_1", action="store_true", help="List one file per line")
parser.add_argument("-a", "--all", action="store_true", help="Include entries that begin with a dot (.)")
parser.add_argument("path", nargs="?", default=".", help="Directory to list")

args = parser.parse_args()

files = os.listdir(args.path)

if args.all:
    files = [".", ".."] + files
else:
    files = [file for file in files if not file.startswith(".")]

if args._1:
    print("\n".join(files))
else:
    print("  ".join(files))
