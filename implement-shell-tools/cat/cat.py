import argparse
import os

# set argument parser
parser = argparse.ArgumentParser(description="Python implementation of cat command")

# to number all lines
parser.add_argument("-n", action="store_true", help="Number all lines")
# To raed files
parser.add_argument("files", nargs="+", help="Files to read")

args = parser.parse_args()

line_number = 1

for file in args.files:
    if not os.path.isfile(file):
        print(f"cat: {file}: No such file or directory")
        continue


    with open(file, "r") as f:
        for line in f:
            if args.n:
                print(f"{line_number:6}\t{line}", end="")  # to print number all lines
                line_number += 1
            else:    
                print(line, end ="")  # to print content of files
