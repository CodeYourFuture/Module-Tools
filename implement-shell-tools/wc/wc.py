import argparse
import sys
import os


def calculate_stats(content, display_name, original_bytes=None):
    lines = content.count("\n")
    words = len(content.split())
    # If we have the raw bytes, use that length. Otherwise, encode to get byte length.
    byte_count = (
        original_bytes if original_bytes is not None else len(content.encode("utf-8"))
    )

    return {
        "lineCount": lines,
        "wordCount": words,
        "byteCount": byte_count,
        "displayName": display_name,
    }


def print_formatted_report(stats, args, should_show_all_stats):
    output_columns = []

    def format_col(count):
        return str(count).rjust(4)

    if should_show_all_stats:
        output_columns.append(format_col(stats["lineCount"]))
        output_columns.append(format_col(stats["wordCount"]))
        output_columns.append(format_col(stats["byteCount"]))
    else:
        if args.lines:
            output_columns.append(format_col(stats["lineCount"]))
        if args.words:
            output_columns.append(format_col(stats["wordCount"]))
        if args.bytes:
            output_columns.append(format_col(stats["byteCount"]))

    # Use a single space between the numbers and the name
    print(f"{''.join(output_columns)} {stats['displayName']}")


def main():
    parser = argparse.ArgumentParser(description="A simple Python implementation of wc")
    parser.add_argument("files", nargs="*", help="Files to process")
    parser.add_argument(
        "-l", "--lines", action="store_true", help="print the newline counts"
    )
    parser.add_argument(
        "-w", "--words", action="store_true", help="print the word counts"
    )
    parser.add_argument(
        "-c", "--bytes", action="store_true", help="print the byte counts"
    )

    args = parser.parse_args()
    should_show_all_stats = not (args.lines or args.words or args.bytes)
    all_file_stats = []
    exit_code = 0

    # NEW: Handle Standard Input if no files are provided
    if not args.files:
        stdin_content = sys.stdin.read()
        stats = calculate_stats(stdin_content, "")
        print_formatted_report(stats, args, should_show_all_stats)
        return

    # Process files
    for file_path in args.files:
        try:
            with open(file_path, "rb") as f:
                raw_bytes = f.read()
                content = raw_bytes.decode("utf-8", errors="ignore")
                stats = calculate_stats(content, file_path, len(raw_bytes))

            all_file_stats.append(stats)
            print_formatted_report(stats, args, should_show_all_stats)
        except Exception:
            print(f"wc: {file_path}: No such file or directory", file=sys.stderr)
            exit_code = 1

    # Print total if more than one file
    if len(all_file_stats) > 1:
        grand_totals = {
            "lineCount": sum(s["lineCount"] for s in all_file_stats),
            "wordCount": sum(s["wordCount"] for s in all_file_stats),
            "byteCount": sum(s["byteCount"] for s in all_file_stats),
            "displayName": "total",
        }
        print_formatted_report(grand_totals, args, should_show_all_stats)

    if exit_code != 0:
        sys.exit(exit_code)


if __name__ == "__main__":
    main()
