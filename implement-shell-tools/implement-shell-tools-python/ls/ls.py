#!/usr/bin/env python3
import sys
import os
import argparse


def list_directory(path, show_all):
    try:
        entries = os.listdir(path)

    except Exception as e:
        print(f"Error reading directory {path}: {e}", file=sys.stderr)
        sys.exit(1)
    for entry in sorted(entries):
        if not show_all and entry.startswith("."):
            continue
        print(entry)


def main():
    parser = argparse.ArgumentParser(description="List directory contents")
    parser.add_argument("-a", "--all", action="store_true", help="show hidden files")
    parser.add_argument("paths", nargs="*", default=["."], help="directories to list")

    args = parser.parse_args()

    dirs = args.paths

    for i, path in enumerate(dirs):
        if len(dirs) > 1:
            print(f"{path}:")
        list_directory(path, args.all)

        if len(dirs) > 1 and i < len(dirs) - 1:
            print("")


if __name__ == "__main__":
    main()
