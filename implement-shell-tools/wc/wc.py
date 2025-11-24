import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="wc",
    description="Count lines, words, and characters"
)
parser.add_argument("paths", nargs='+', help="Files to count")
parser.add_argument("-l", "--lines", action="store_true", help="Count lines only")
parser.add_argument("-w", "--words", action="store_true", help="Count words only")
parser.add_argument("-c", "--chars", action="store_true", help="Count characters only")

args = parser.parse_args()

for path in args.paths:
    # Read the file
    with open(path, "r") as f:
        content = f.read()

    # Count lines, words, characters
    lines = len(content.rstrip('\n').split('\n'))
    words = len(content.split())
    chars = len(content)

    if args.lines:
        print(f"{lines:8} {path}")
    elif args.words:
        print(f"{words:8} {path}")
    elif args.chars:
        print(f"{chars:8} {path}")
    else:
        print(f"{lines:8}{words:8}{chars:8} {path}")  