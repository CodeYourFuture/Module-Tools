#!/usr/bin/env python3

import os
import sys
import argparse


def list_directory(path, show_all):
    try:
        if os.path.isfile(path):
            # ls file.txt → just print the file name
            print(path)
            return

        if os.path.isdir(path):
            entries = os.listdir(path)
        else:
            print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
            return

    except PermissionError:
        print(f"ls: cannot open directory '{path}': Permission denied", file=sys.stderr)
        return

    # If -a is not provided, hide dotfiles
    if not show_all:
        entries = [e for e in entries if not e.startswith(".")]

    entries.sort()

    for entry in entries:
        print(entry)

def main():
    parser = argparse.ArgumentParser(description="Simple ls implementation")
    parser.add_argument(
        "-a",
        action="store_true",
        help="include directory entries whose names begin with a dot",
    )

    parser.add_argument("path", nargs="?", default=".", help="directory to list")

    args = parser.parse_args()

    list_directory(args.path, show_all=args.a)

if __name__ == "__main__":
    main()
