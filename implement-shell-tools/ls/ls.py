#!/usr/bin/env python3

import locale
import os
import sys


def parse_args(args):
    one_per_line = False
    show_all = False
    paths = []

    for arg in args:
        if arg.startswith("-") and arg != "-":
            for flag in arg[1:]:
                if flag == "1":
                    one_per_line = True
                elif flag == "a":
                    show_all = True
                else:
                    print(f"ls: invalid option -- '{flag}'", file=sys.stderr)
                    sys.exit(1)
        else:
            paths.append(arg)

    if not one_per_line:
        print("Usage: ls.py -1 [-a] [path]", file=sys.stderr)
        sys.exit(1)

    if len(paths) > 1:
        print("Usage: ls.py -1 [-a] [path]", file=sys.stderr)
        sys.exit(1)

    return show_all, (paths[0] if paths else ".")


def list_entries(path, show_all):
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory", file=sys.stderr)
        sys.exit(1)
    except NotADirectoryError:
        print(os.path.basename(path))
        return

    if show_all:
        entries = [".", ".."] + entries
    else:
        entries = [name for name in entries if not name.startswith(".")]

    locale.setlocale(locale.LC_COLLATE, "")
    entries = sorted(entries, key=locale.strxfrm)

    for entry in entries:
        print(entry)


def main():
    show_all, path = parse_args(sys.argv[1:])
    list_entries(path, show_all)


if __name__ == "__main__":
    main()
