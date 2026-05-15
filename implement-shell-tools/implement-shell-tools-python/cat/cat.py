#!/usr/bin/env python3
import sys
import argparse


def print_file(file_path, options, counter):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.rstrip("\n")

                should_number = options.number_mode == "all" or (
                    options.number_mode == "non-empty" and stripped != ""
                )

                if should_number:
                    print(f"{counter}\t{stripped}")
                    counter += 1
                else:
                    print(stripped)

    except FileNotFoundError:
        print(f"cat: {file_path}: No such file or directory", file=sys.stderr)

    return counter


def main():
    parser = argparse.ArgumentParser(description="Concatenate files and print output")
    parser.add_argument("-n", "--number", action="store_true", help="number all lines")

    parser.add_argument(
        "-b", "--number-nonblank", action="store_true", help="number non-empty lines"
    )

    parser.add_argument("files", nargs="+", help="files to read")

    args = parser.parse_args()

    if args.number_nonblank:
        args.number_mode = "non-empty"
    elif args.number:
        args.number_mode = "all"
    else:
        args.number_mode = "none"

    counter = 1
    for file in args.files:
        counter = print_file(file, args, counter)


if __name__ == "__main__":
    main()
