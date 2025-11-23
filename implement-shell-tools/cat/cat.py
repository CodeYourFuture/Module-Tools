import sys
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and display files"
)

parser.add_argument("-n", "--number", action="store_true", help="Number all output lines")
parser.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty lines only")
parser.add_argument("paths", nargs='+', help="Files to read")

args = parser.parse_args()

line_number = 0  # Shared counter across all files

# Process each file
for path in args.paths:  # LEVEL 1: for loop starts
    with open(path, "r") as f:  # LEVEL 2: inside for loop
        content = f.read()  # LEVEL 3: inside with block
    
    # Check if numbering is needed
    if args.number:  # LEVEL 2: inside for loop
        lines = content.split("\n")  # LEVEL 3: inside if
        numbered_lines = []
        
        for index, line in enumerate(lines):  # LEVEL 3: inside if
            line_number = line_number + 1  # LEVEL 4: inside inner for
            numbered_line = f"{line_number:6}\t{line}"
            numbered_lines.append(numbered_line)
        
        print("\n".join(numbered_lines))  # LEVEL 3: inside if
    
    elif args.number_nonblank:  # LEVEL 2: inside for loop
        lines = content.split("\n")  # LEVEL 3: inside elif
        numbered_lines = []
        
        for line in lines:  # LEVEL 3: inside elif
            if line.strip() == "":  # LEVEL 4: inside inner for
                numbered_lines.append(line)
            else:
                line_number = line_number + 1
                numbered_line = f"{line_number:6}\t{line}"
                numbered_lines.append(numbered_line)
        
        print("\n".join(numbered_lines))
    
    else:  # LEVEL 2: inside for loop
        print(content)  # LEVEL 3: inside else