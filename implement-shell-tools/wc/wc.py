#!/usr/bin/env python3

import sys


def count_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()

        lines = data.count('\n')
        words = len(data.split())
        bytes_count = len(data.encode('utf-8'))

        return lines, words, bytes_count
    except FileNotFoundError:
        print(f"wc: {file}: No such file or directory", file=sys.stderr)
        sys.exit(1)


def selected_keys(options):
    if not any(options.values()):
        return ['lines', 'words', 'bytes']

    keys = []
    if options['lines']:
        keys.append('lines')
    if options['words']:
        keys.append('words')
    if options['bytes']:
        keys.append('bytes')
    return keys


def values_for_keys(counts, keys):
    lines, words, bytes_count = counts
    mapping = {
        'lines': lines,
        'words': words,
        'bytes': bytes_count,
    }
    return [mapping[key] for key in keys]


def print_rows(rows, keys):
    align_columns = len(keys) > 1 or len(rows) > 1

    if not align_columns:
        values, name = rows[0]
        print(f"{values[0]} {name}")
        return

    widths = []
    for index in range(len(keys)):
        max_len = max(len(str(values[index])) for values, _ in rows)
        widths.append(max(3, max_len))

    for values, name in rows:
        formatted_values = " ".join(
            f"{value:>{width}}" for value, width in zip(values, widths)
        )
        print(f"{formatted_values} {name}")

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
    keys = selected_keys(options)
    rows = []

    for file in files:
        lines, words, bytes_count = count_file(file)
        total_lines += lines
        total_words += words
        total_bytes += bytes_count
        rows.append((values_for_keys((lines, words, bytes_count), keys), file))

    if len(files) > 1:
        rows.append((values_for_keys((total_lines, total_words, total_bytes), keys), 'total'))

    print_rows(rows, keys)

if __name__ == "__main__":
    main()