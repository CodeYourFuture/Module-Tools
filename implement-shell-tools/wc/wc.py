import sys
import os
import argparse

# 1. Set up argparse to handle the wc flags
parser = argparse.ArgumentParser(description="A simple Python implementation of the wc command.")

# Add the optional flags (-l, -w, -c)
parser.add_argument("-l", action="store_true", help="Print the newline counts")
parser.add_argument("-w", action="store_true", help="Print the word counts")
parser.add_argument("-c", action="store_true", help="Print the byte counts")

# Add the files argument (nargs="*" means it accepts 0 or more files)
parser.add_argument("files", nargs="*", help="Files to process")

# Parse the arguments
args = parser.parse_args()

# 2. Rename back the variables
show_lines = args.l
show_words = args.w
show_chars = args.c
files = args.files

# If no flags then show all.
show_all = not (show_lines or show_words or show_chars)


# Total counters
total_l, total_w, total_c = 0, 0, 0

for filename in files:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
            # files calculation
            l_count = len(lines)
            w_count = sum(len(line.split()) for line in lines)
            #  os.path.getsize for bytes, in .js I used const bytes = Buffer.byteLength(content);
            c_count = os.path.getsize(filename)
            
            # Update totals
            total_l += l_count
            total_w += w_count
            total_c += c_count
            
            # Printing Logic
            output = []
            if show_lines or show_all: output.append(f"{l_count:>8}")
            if show_words or show_all: output.append(f"{w_count:>8}")
            if show_chars or show_all: output.append(f"{c_count:>8}")
            
            print(f"{''.join(output)} {filename}")

    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory")
    except IsADirectoryError:
        print(f"wc: {filename}: Is a directory")
        print(f"{'0':>8} {'0':>8} {'0':>8} {filename}")

# Print Total if there were multiple files
if len(files) > 1:
    output_total = []
    if show_lines or show_all: output_total.append(f"{total_l:>8}")
    if show_words or show_all: output_total.append(f"{total_w:>8}")
    if show_chars or show_all: output_total.append(f"{total_c:>8}")
    print(f"{''.join(output_total)} total")
