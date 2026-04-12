#!/usr/bin/env python3

import sys

def cat_file(file, options, line_number):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            if options['number_non_blank'] and line.strip():
                print(f"{line_number:6}\t{line}", end='')
                line_number += 1
            elif options['number_all']:
                print(f"{line_number:6}\t{line}", end='')
                line_number += 1
            else:
                print(line, end='')

        return line_number
    except FileNotFoundError:
        print(f"cat: {file}: No such file or directory", file=sys.stderr)
        sys.exit(1)

def main():
    args = sys.argv[1:]
    options = {
        'number_all': False,
        'number_non_blank': False,
    }

    files = []

    for arg in args:
        if arg == '-n':
            options['number_all'] = True
        elif arg == '-b':
            options['number_non_blank'] = True
        else:
            files.append(arg)

    if not files:
        print("Usage: cat [-n | -b] <file>...", file=sys.stderr)
        sys.exit(1)

    line_number = 1
    for file in files:
        line_number = cat_file(file, options, line_number)

if __name__ == "__main__":
    main()