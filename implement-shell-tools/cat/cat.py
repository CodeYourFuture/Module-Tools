import argparse

parser = argparse.ArgumentParser(
    prog="py-cat",
    description="A Python implementation of the Unix cat command",
)

parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("-b", "--numberNonBlank", action="store_true", help="Numbers only non-empty lines. Overrides -n option")
parser.add_argument("path", nargs="+", help="The file path to process")

args = parser.parse_args()

def number_all(lines):
    numbered = []
    for i, line in enumerate(lines):
        numbered.append(f"{i + 1:>6}\t{line}")
    return numbered

def number_non_blank(lines):
    numbered = []
    counter = 1
    for line in lines:
        if line == "":
            numbered.append(line)
        else: 
            numbered.append(f"{counter:>6}\t{line}")
            counter += 1
    return numbered

# Read and concatenate file contents
content = ""

for path in args.path:
    with open(path, "r") as f:
        content += f.read()

if content.endswith("\n"):
    content = content[:-1]

# Split content into lines
lines = content.split("\n")

# Output logic

if args.numberNonBlank:
    print("\n".join(number_non_blank(lines)))
elif args.number:
    print("\n".join(number_all(lines)))
else:
    print("\n".join(lines))