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


def calculate_output(counts, flags, label):
    """Helper to build consistent formatted output lines."""
    l_flag, w_flag, c_flag = flags
    count_strings = []

    # If no flags are set, show all counts
    if not (l_flag or w_flag or c_flag):
        lines, words, bytes_count = counts
        count_strings = [f"{lines:>7}", f"{words:>7}", f"{bytes_count:>7}"]
    else:
        if counts[0] is not None:
            count_strings.append(f"{counts[0]:>7}")
        if counts[1] is not None:
            count_strings.append(f"{counts[1]:>7}")
        if counts[2] is not None:
            count_strings.append(f"{counts[2]:>7}")

    return f"{' '.join(count_strings)} {label}"


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
        total_lines += counts[0] or 0
        total_words += counts[1] or 0
        total_bytes += counts[2] or 0

        print(calculate_output(counts, (args.l, args.w, args.c), file_path))

    if len(file_list) > 1:
        total_counts = (
            total_lines if args.l or not (args.l or args.w or args.c) else None,
            total_words if args.w or not (args.l or args.w or args.c) else None,
            total_bytes if args.c or not (args.l or args.w or args.c) else None,
        )
        print(calculate_output(total_counts, (args.l, args.w, args.c), "total"))


if __name__ == "__main__":
    main()
