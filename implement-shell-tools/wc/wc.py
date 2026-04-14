#!/usr/bin/env python3

import argparse
import sys
import os

parser = argparse.ArgumentParser(
    prog='wc',
    description='Displays number of words, lines, and bytes in a file'
)

parser.add_argument('-l', '--lines', action='store_true', help='counts number of lines')
parser.add_argument('-w', '--words', action='store_true', help='counts sequence of characters')
parser.add_argument('-c', '--bytes', action='store_true', help='counts raw size of a file in bytes')
parser.add_argument('files', nargs='+', help='Files to read')

args = parser.parse_args()

if not args.files:
    print(f"wc: missing file to read")
    sys.exit(1)

total_lines, total_words, total_bytes = 0, 0, 0

for file in args.files:
    try:
        with open(file, 'r') as f:
            content = f.read()

        line_count = content.count('\n')
        word_count = len(content.split())
        byte_count = os.path.getsize(file)

        total_lines += line_count
        total_words += word_count
        total_bytes += byte_count

        show_all = not (args.lines or args.words or args.bytes)

        output = ""
        if args.lines or show_all:
            output += f"{line_count:>7} "
        if args.words or show_all:
            output += f"{word_count:>7} "
        if args.bytes or show_all:
            output += f"{byte_count:>7} "
        
        print(f"{output} {file}")

    except FileNotFoundError:
        print(f"wc: {args.path}: No such file or directory.", file=sys.stderr)


if len(args.files) > 1:
    total = ""
    if args.lines or show_all:
        total += f"{total_lines:>7} "
    if args.words or show_all:
        total += f"{total_words:>7} "
    if args.bytes or show_all:
        total += f"{total_bytes:>7} "

    print(f"{total}total")