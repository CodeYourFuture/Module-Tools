import os
import argparse

# Setup argument parser
parser = argparse.ArgumentParser(
    prog="ls",
    description="Lists contents of a directory"
)

parser.add_argument("-1", dest="one_column", action="store_true", help="List one file per line")
parser.add_argument("path", nargs='?', default=".", help="Directory to list (default: current directory)")

args = parser.parse_args()

# List directory contents
files = os.listdir(args.path)

# Print each file
for file in files:
    print(file)