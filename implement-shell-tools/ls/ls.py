#!/usr/bin/env python3
import sys
import os

def list_dir(path=".", show_all=False):
    try:
        entries = os.listdir(path)
        if not show_all:
            entries = [e for e in entries if not e.startswith(".")]
        return sorted(entries)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        return []
    except NotADirectoryError:
        # If it's a file, just return it
        return [path]

def main():
    args = sys.argv[1:]

    # Flags
    show_one_per_line = "-1" in args
    show_all = "-a" in args

    # Remove flags from args
    paths = [arg for arg in args if arg not in ("-1", "-a")]

    if not paths:
        paths = ["."]  # default to current directory

    for i, path in enumerate(paths):
        entries = list_dir(path, show_all=show_all)

        if len(paths) > 1:
            print(f"{path}:")

        for entry in entries:
            if show_one_per_line:
                print(entry)
            else:
                print(entry, end="  ")
        if not show_one_per_line:
            print()  # newline after the row

        if i < len(paths) - 1:
            print()

if __name__ == "__main__":
    main()
