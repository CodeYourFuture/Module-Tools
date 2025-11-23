import sys
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and display files"
)

parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty lines only")
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

elif args.number_nonblank:
    lines = content.split("\n")
    numbered_lines = []
    line_number = 0
    
    for line in lines:
        if line.strip() == "":  # Empty line
            numbered_lines.append(line)  # Don't number it
        else:  # Non-empty line
            line_number = line_number + 1
            numbered_line = f"{line_number:6}\t{line}"
            numbered_lines.append(numbered_line)
    
    print("\n".join(numbered_lines))    
    
else:
    print(content)
