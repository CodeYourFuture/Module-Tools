#!/usr/bin/env python3
import sys
import glob

def cat(files, number_all=False, number_nonblank=False):
    line_num = 1
    for filename in files:
        try:
            with open(filename, "r") as f:
                for line in f:
                    stripped = line.rstrip("\n")

                    if number_all:
                        print(f"{line_num:6}\t{stripped}")
                        line_num += 1
                    elif number_nonblank:
                        if stripped:
                            print(f"{line_num:6}\t{stripped}")
                            line_num += 1
                        else:
                            print()
                    else:
                        print(stripped)
        except FileNotFoundError:
            print(f"cat: {filename}: No such file or directory", file=sys.stderr)

def main():
    args = sys.argv[1:]

    number_all = "-n" in args
    number_nonblank = "-b" in args

    # Remove flags from args
    files = [arg for arg in args if arg not in ("-n", "-b")]

    # Expand globs like *.txt
    expanded_files = []
    for file in files:
        expanded_files.extend(glob.glob(file))

    if not expanded_files:
        print("cat: missing file operand", file=sys.stderr)
        sys.exit(1)

    cat(expanded_files, number_all=number_all, number_nonblank=number_nonblank)

if __name__ == "__main__":
    main()
