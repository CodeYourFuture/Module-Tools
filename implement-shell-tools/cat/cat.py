import sys
import argparse

# 1. Set up argparse to handle flags and files
parser = argparse.ArgumentParser(description="A simple Python implementation of the cat command.")

# Add the optional flags (-n and -b)
parser.add_argument("-n", action="store_true", help="Number all output lines")
parser.add_argument("-b", action="store_true", help="Number nonempty output lines, overrides -n")

# Add the files argument (nargs="*" means it accepts 0 or more files)
parser.add_argument("files", nargs="*", help="Files to read")

# Parse the arguments
args = parser.parse_args()

show_all_numbers = args.n
show_non_blank_numbers = args.b
files = args.files


if not files:
    print("Usage: python3 cat.py [-n] [-b] <filenames>")
    sys.exit()

line_count = 1
# 3. Process each file 
for filename in files:
    try:
        with open(filename, "r") as file:
            for line in file:
                # Logic for -b 
                if show_non_blank_numbers:
                    if line.strip(): # If line is not empty
                        print(f"{line_count:>6}\t{line}", end="")
                        line_count += 1
                    else:
                        # Standard cat no flags
                        print(line, end="")
                
                # Logic for -n 
                elif show_all_numbers:
                    print(f"{line_count:>6}\t{line}", end="")
                    line_count += 1
                
                # Standard cat no flags
                else:
                    print(line, end="")
                    
    # throw clear errors                
    except FileNotFoundError:
        print(f"Error: {filename}: No such file or directory")
    except IsADirectoryError:
        print(f"Error: {filename}: Is a directory")
