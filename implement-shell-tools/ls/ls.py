import argparse
import os

parser = argparse.ArgumentParser(description="Display one file per line from ls directory")

parser.add_argument("-1", dest="one", action="store_true", help="List one file per line")
parser.add_argument("-a", action="store_true", help="Include hidden files (those starting with .)")
parser.add_argument("path", nargs="?", default=".", help="The directory to list (default: current directory)")

args = parser.parse_args()


files = sorted(os.listdir(args.path))


if not args.a:
    files = [f for f in files if not f.startswith(".")]

if args.one:
    for f in files:
        print(f)
else:
    print("  ".join(files))
