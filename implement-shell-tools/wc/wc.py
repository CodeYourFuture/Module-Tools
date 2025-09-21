#!/usr/bin/env python3
import sys
import glob
import os

def count_file(filename, count_lines, count_words, count_bytes):
    try:
        with open(filename, "rb") as f:  # open in binary to count bytes correctly
            data = f.read()
    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory", file=sys.stderr)
        return None

    text = data.decode(errors="ignore")
    lines = text.splitlines()

    l = len(lines)
    w = len(text.split())
    c = len(data)

    results = []
    if count_lines:
        results.append(str(l))
    if count_words:
        results.append(str(w))
    if count_bytes:
        results.append(str(c))

    if not (count_lines or count_words or count_bytes):
        # default: all three
        results = [str(l), str(w), str(c)]

    return results, filename, (l, w, c)

def main():
    args = sys.argv[1:]

    count_lines = "-l" in args
    count_words = "-w" in args
    count_bytes = "-c" in args

    # remove flags from args
    files = [arg for arg in args if arg not in ("-l", "-w", "-c")]

    if not files:
        print("wc: missing file operand", file=sys.stderr)
        sys.exit(1)

    expanded_files = []
    for f in files:
        expanded_files.extend(glob.glob(f))

    if not expanded_files:
        print("wc: no matching files", file=sys.stderr)
        sys.exit(1)

    total_l, total_w, total_c = 0, 0, 0

    for filename in expanded_files:
        result = count_file(filename, count_lines, count_words, count_bytes)
        if result:
            res, name, (l, w, c) = result
            print(f"{' '.join(res)} {name}")
            total_l += l
            total_w += w
            total_c += c

    if len(expanded_files) > 1:
        total_results = []
        if count_lines:
            total_results.append(str(total_l))
        if count_words:
            total_results.append(str(total_w))
        if count_bytes:
            total_results.append(str(total_c))
        if not (count_lines or count_words or count_bytes):
            total_results = [str(total_l), str(total_w), str(total_c)]
        print(f"{' '.join(total_results)} total")

if __name__ == "__main__":
    main()
