import argparse
import os

parser = argparse.ArgumentParser(
    prog="Implement ls command in Python",
    description="List files in a directory"
    )

parser.add_argument("-a", action="store_true", help="Display all files include hidden files")
parser.add_argument("-1", action="store_true", help="list one file per line")
parser.add_argument("dir", nargs="?", default=".", help="Directory to list, default curent directory")

args = parser.parse_args()

files = os.listdir(args.dir)

if not args.a:
    files = [f for f in files if not f.startswith(".")]
files.sort()

if args.__dict__["1"]:
    for f in files:
        print(f)
else:
    print(' '.join(files))

