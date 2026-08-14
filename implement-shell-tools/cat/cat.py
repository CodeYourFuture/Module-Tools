import argparse
import sys

parser = argparse.ArgumentParser(prog="cat")
parser.add_argument("-n", action="store_true")
parser.add_argument("-b", action="store_true")
parser.add_argument("files", nargs="+")

args = parser.parse_args()

for file in args.files:
    line_number = 1

    with open(file) as f:
        for line in f:
            should_number = args.n or (args.b and line.strip())

            if should_number:
                print(f"{line_number:6}\t{line}", end="")
                line_number += 1
            else:
                print(line, end="")