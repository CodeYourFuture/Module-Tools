import argparse
import os

parser = argparse.ArgumentParser(description="dispaly one file per line from ls directory")

parser.add_argument("-1", action="store_true", help="List one file per line")
parser.add_argument("-a", action="store_true", help="Include hidden files (those starting with .)")
parser.add_argument("path", nargs="?", default=".", help="The directory to list (default: current directory)")

args = parser.parse_args()

for filename in sorted(os.listdir(args.path)):
    if not args.a and filename.startswith("."):
        # skip hidden files unless -a is provided
        continue 
    print(filename)