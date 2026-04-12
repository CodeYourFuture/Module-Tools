#!/usr/bin/env python3

import sys
import os

def count_file(file, options):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()

        lines = data.count('\n') + 1
        words = len(data.split())
        bytes_count = len(data.encode('utf-8'))

        results = []
        if options['lines'] or not any(options.values()):
            results.append(lines)
        if options['words'] or not any(options.values()):
            results.append(words)
        if options['bytes'] or not any(options.values()):
            results.append(bytes_count)

        print(f"{'\t'.join(map(str, results))}\t{file}")

        return lines, words, bytes_count
    except FileNotFoundError:
        print(f"wc: {file}: No such file or directory", file=sys.stderr)
        sys.exit(1)

def main():
    args = sys.argv[1:]
    options = {
        'lines': False,
        'words': False,
        'bytes': False,
    }

    files = []

    for arg in args:
        if arg == '-l':
            options['lines'] = True
        elif arg == '-w':
            options['words'] = True
        elif arg == '-c':
            options['bytes'] = True
        else:
            files.append(arg)

    if not files:
        print("Usage: wc [-l | -w | -c] <file>...", file=sys.stderr)
        sys.exit(1)

    total_lines = 0
    total_words = 0
    total_bytes = 0

    for file in files:
        lines, words, bytes_count = count_file(file, options)
        total_lines += lines
        total_words += words
        total_bytes += bytes_count

    if len(files) > 1:
        total_results = []
        if options['lines'] or not any(options.values()):
            total_results.append(total_lines)
        if options['words'] or not any(options.values()):
            total_results.append(total_words)
        if options['bytes'] or not any(options.values()):
            total_results.append(total_bytes)

        print(f"{'\t'.join(map(str, total_results))}\ttotal")

if __name__ == "__main__":
    main()