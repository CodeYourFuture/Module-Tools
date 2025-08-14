import argparse
import glob
import os

def count_file(file_path, count_lines=False, count_words=False, count_bytes=False):
    lines = words = bytes_count = 0
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            lines += 1
            words += len(line.split())
    bytes_count = os.path.getsize(file_path)

    if not (count_lines or count_words or count_bytes):
        return lines, words, bytes_count

    return (
        lines if count_lines else None,
        words if count_words else None,
        bytes_count if count_bytes else None
    )

def main():
    parser = argparse.ArgumentParser(description="count lines, words, and bytes like the wc command")
    parser.add_argument("-l", action="store_true", help="Count lines")
    parser.add_argument("-w", action="store_true", help="Count words")
    parser.add_argument("-c", action="store_true", help="Count bytes")
    parser.add_argument("path", nargs="+", help="Files to count")

    args = parser.parse_args()

    total_lines = total_words = total_bytes = 0
    file_list = []
    for pattern in args.path:
        file_list.extend(glob.glob(pattern))

    for file_path in file_list:
        counts = count_file(file_path, args.l, args.w, args.c)

        if not (args.l or args.w or args.c):
            lines, words, bytes_count = counts
            print(f"{lines:>7} {words:>7} {bytes_count:>7} {file_path}")
            total_lines += lines
            total_words += words
            total_bytes += bytes_count
        else:
            count_strings = []
            if counts[0] is not None:
                count_strings.append(f"{counts[0]:>7}")
                total_lines += counts[0]
            if counts[1] is not None:
                count_strings.append(f"{counts[1]:>7}")
                total_words += counts[1]
            if counts[2] is not None:
                count_strings.append(f"{counts[2]:>7}")
                total_bytes += counts[2]
            print(" ".join(count_strings), file_path)

    if len(file_list) > 1:
        if not (args.l or args.w or args.c):
            print(f"{total_lines:>7} {total_words:>7} {total_bytes:>7} total")
        else:
            total_strings = []
            if args.l:
                total_strings.append(f"{total_lines:>7}")
            if args.w:
                total_strings.append(f"{total_words:>7}")
            if args.c:
                total_strings.append(f"{total_bytes:>7}")
            print(" ".join(total_strings), "total")

if __name__ == "__main__":
    main()
