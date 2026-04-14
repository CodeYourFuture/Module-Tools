#!/usr/bin/env python3

import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog='ls',
    description='CLI tool to list contents of a directory'
)

parser.add_argument('-1', '--one', action='store_true', help='Force output to be entry per line')
parser.add_argument('-a','--all', action='store_true', help='Include hidden files')
parser.add_argument('path', nargs='?', default='.', help='Directories to list')

args = parser.parse_args()

try:
    entries = os.listdir(args.path)
    # print(entries)
    if not args.all:
        entries = [entry for entry in entries if not entry.startswith('.')]
    entries.sort(key=str.lower)
    # print(entries)
    
    if args.one:
        for entry in entries:
            print(entry)

    else:
        print(f" ".join(entries))

except FileNotFoundError:
    print(f"ls: {args.path}: No such file or directory.", file=sys.stderr)