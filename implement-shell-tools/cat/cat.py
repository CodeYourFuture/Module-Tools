import sys
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and display files"
)

parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("path", help="File to read")

args = parser.parse_args()


# Read the file 
with open(args.path, "r") as f: 
    content = f.read()
                

# Check if numbering is needed
if args.number:
    lines = content.split("\n")
    numbered_lines = []
    
    for index, line in enumerate(lines):
        line_number = index + 1
        numbered_line = f"{line_number:6}\t{line}"  # Format with tab like real cat
        numbered_lines.append(numbered_line)
    
    print("\n".join(numbered_lines))
else:
    print(content)
