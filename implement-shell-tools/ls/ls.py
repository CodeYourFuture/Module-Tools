# implement-shell-tools/ls/ls.py
import argparse
import os
import sys
import shutil
import math

def print_columns(items, force_single_column=False):
    """Print items in columns unless -1 is passed or output is not a tty."""
    if force_single_column or not sys.stdout.isatty():
        for item in items:
            print(item)
        return

    # Get terminal width
    term_width = shutil.get_terminal_size((80, 20)).columns

    if not items:
        return

    # Longest filename length + spacing
    max_len = max(len(f) for f in items) + 2
    cols = max(1, term_width // max_len)
    rows = math.ceil(len(items) / cols)

    for r in range(rows):
        row_items = []
        for c in range(cols):
            i = c * rows + r
            if i < len(items):
                row_items.append(items[i].ljust(max_len))
        print("".join(row_items).rstrip())

def main():
    parser = argparse.ArgumentParser(
    prog="ls",
    description="Implements a simple version of the 'ls' command to list files in a directory."
    )

    parser.add_argument("-1", help="List one file per line", action="store_true")
    parser.add_argument("-a", help="Include hidden files", action="store_true")
    parser.add_argument("directory", nargs="?", default=".", help="The directory to search")

    args = parser.parse_args()

    try:
        if os.path.isdir(args.directory):
            files = os.listdir(args.directory)

            if not args.a:
                files = [f for f in files if not f.startswith(".")]
            
            files = sorted(files)

            print_columns(files, force_single_column=args.__dict__["1"])
        else:
            # If it's a file, just print the name
            print(args.directory)

    except FileNotFoundError:
        print(f"ls: {args.directory}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"ls: {args.directory}: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()