import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="wc",
    description="Count lines, words, and characters"
)
parser.add_argument("paths", nargs='+', help="Files to count")

args = parser.parse_args()

for path in args.paths:
    # Read the file
    with open(path, "r") as f:
        content = f.read()

    # Count lines, words, characters
    lines = len(content.rstrip('\n').split('\n'))
    words = len(content.split())
    chars = len(content)

    print(f"{lines:8}{words:8}{chars:8} {path}")  