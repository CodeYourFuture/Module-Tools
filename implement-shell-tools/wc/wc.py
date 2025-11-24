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

# Track totals
total_lines = 0
total_words = 0
total_chars = 0

for path in args.paths:
    # Read the file
    with open(path, "r") as f:
        content = f.read()

    # Count lines, words, characters
    lines = len(content.rstrip('\n').split('\n'))
    words = len(content.split())
    chars = len(content)

    # Add to totals
    total_lines += lines
    total_words += words
    total_chars += chars

    if args.lines:
        print(f"{lines:8} {path}")
    elif args.words:
        print(f"{words:8} {path}")
    elif args.chars:
        print(f"{chars:8} {path}")
    else:
        print(f"{lines:8}{words:8}{chars:8} {path}")  

        
# Print totals if multiple files
if len(args.paths) > 1:
    if args.lines:
        print(f"{total_lines:8} total")
    elif args.words:
        print(f"{total_words:8} total")
    elif args.chars:
        print(f"{total_chars:8} total")
    else:
        print(f"{total_lines:8}{total_words:8}{total_chars:8} total")        

