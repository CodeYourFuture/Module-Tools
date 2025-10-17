import argparse
import os

# set argument parser
parser = argparse.ArgumentParser(description="Python implementation of cat command")

# to number all lines
parser.add_argument("-n", action="store_true", help="Number all lines")

# to number non-blank lines
parser.add_argument("-b", action="store_true", help="Number non-blank lines (overrides -n)")

# To raed files
parser.add_argument("files", nargs="+", help="Files to read")

args = parser.parse_args()

if args.n and args.b:
    args.n = False

line_number = 1

for file in args.files:
    if not os.path.isfile(file):
        print(f"cat: {file}: No such file or directory")
        continue


    with open(file, "r") as f:
        for line in f:
            if args.b:
                if line.strip():      #to number non blank lines only
                    print(f"{line_number:6}\t{line}", end="")
                    line_number += 1
                else:
                    print(line, end="") # to print blank line with number
                       
            elif args.n:
                print(f"{line_number:6}\t{line}", end="")  # to print number all lines
                line_number += 1
            else:    
                print(line, end ="")  # to print content of files
