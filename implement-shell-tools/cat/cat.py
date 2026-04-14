#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(
    prog='cat',
    description='CLI tool to concatenate and print files', 
)

parser.add_argument('-n', '--number', action='store_true', help='Number all outputs, starting at 1')
parser.add_argument('-b', '--nonBlank', action='store_true', help='Number only non-blank lines, starting at 1')
parser.add_argument('files', nargs='*', help='Files to read')

args = parser.parse_args()
# print(args.number, args.nonBlank, args.files)
# print(sys.argv[0], sys.argv[1])


for file in args.files:
    count = 1
    try:
        with open(file, 'r') as f:
            for line in f:
                if args.nonBlank:
                    if line.strip():
                        print(f"{str(count).rjust(6)}\t{line}", end='')
                        count += 1
                    else:
                        print(line, end="")
                elif args.number:
                    print(f"{str(count).rjust(6)}\t{line}", end='')
                    count +=1
                else:
                    print(f"{line}", end="")
   
    except FileNotFoundError:
        print(f"cat: {file}: No such file or directory.", file=sys.stderr)