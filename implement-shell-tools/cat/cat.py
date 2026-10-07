import argparse
import os

parser = argparse.ArgumentParser(prog="cat",
                                 description="simple cat clone")

parser.add_argument("-n",
                    "--number",
                    dest="number_all",
                    action="store_true",
                    help="number all output lines")

parser.add_argument("-b",
                    "--number-nonblank",
                    dest="number_nonblank",
                    action="store_true",
                    help="number non-empty output lines")

parser.add_argument("paths", nargs="+", help="file(s) to process")

args = parser.parse_args()

def process_line(line_number, line):
    if args.number_nonblank:
        if line == "\n":
            print(line, end="")
            return line_number
        
        print(f"{line_number:6}\t{line}", end="")
        return line_number + 1
    
    if args.number_all:
        print(f"{line_number:6}\t{line}", end="")
        return line_number + 1
    
    print(line, end="")
    return line_number

for path in args.paths:
    if os.path.isdir(path):
        print(f"cat: {path}: Is a directory")
        continue

    try:
        with open(path, "r") as file:
            line_number = 1
        
            for line in file:
                line_number = process_line(line_number, line)

    except FileNotFoundError:
        print(f"cat: {path}: No such file or directory")
