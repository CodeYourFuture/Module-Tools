import argparse
import os

parser = argparse.ArgumentParser(description="Python implementation of cat command")

parser.add_argument("files", nargs="+", help="Files to read")

args = parser.parse_args()

line_number = 1

for file in args.files:
    if not os.path.isfile(file):
        print(f"cat: {file}: No such file or directory")
        continue


    with open(file, "r") as f:
        for line in f:
            print(line, end ="")
