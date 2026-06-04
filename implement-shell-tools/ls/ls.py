import os
import sys
import argparse

# 1. Set up argparse to handle the ls flags
parser = argparse.ArgumentParser(description="A simple Python implementation of the ls command.")

# Add the -a and -1 flags
parser.add_argument("-a", action="store_true", help="Do not ignore entries starting with .")
parser.add_argument("-1", action="store_true",dest="one_column", help="List one file per line")

# Add the path argument (nargs="?" means it's optional, default is current directory ".")
parser.add_argument("path", nargs="?", default=".", help="Directory path to list")

# Parse the arguments
args = parser.parse_args()

# 2. rename back  variables
show_all = args.a
one_column = args.one_column
path = args.path

try:
    # Get directory contents
    entries = os.listdir(path)

    # Handle the -a flag 
    if show_all:
        entries.extend([".", ".."])
    
    # 5. Sort alphabetically
    entries.sort()

    # Printing Logic 
    for entry in entries:
        # Skip hidden files unless -a is passed
        if not show_all and entry.startswith("."):
            continue
            
        if one_column:
            # -1 flag: Print vertically
            print(entry)
        else:
            # Standard: Print horizontally with spaces
            print(entry, end="  ")

    #  newline only if we not print horizontally
    if not one_column:
        print()

except FileNotFoundError:
    print(f"ls: cannot access '{path}': No such file or directory")
except NotADirectoryError:
    # if a file  ls just prints the filename
    print(path)
