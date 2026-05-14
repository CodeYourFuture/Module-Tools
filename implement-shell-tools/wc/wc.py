import argparse
import sys

def calculate_stats(content, display_name, original_bytes=None):
    lines = content.count("\n")
    words = len(content.split())
    # Use raw bytes if provided, otherwise encode
    byte_count = (
        original_bytes if original_bytes is not None else len(content.encode("utf-8"))
    )

    return {
        "lineCount": lines,
        "wordCount": words,
        "byteCount": byte_count,
        "displayName": display_name,
    }


def print_formatted_report(stats, active_flags):
    output_parts = []

    for flag in active_flags:
        # Standard wc uses a width of 8 for numbers
        output_parts.append(str(stats[flag]).rjust(8))

    # Join the numbers and add the display name at the end
    result = "".join(output_parts)
    print(f"{result} {stats['displayName']}")


def main():
    parser = argparse.ArgumentParser(description="A simple Python implementation of wc")
    parser.add_argument("files", nargs="*", help="Files to process")
    parser.add_argument("-l", "--lines", action="store_true", help="print the newline counts")
    parser.add_argument("-w", "--words", action="store_true", help="print the word counts")
    parser.add_argument("-c", "--bytes", action="store_true", help="print the byte counts")

    args = parser.parse_args()

    # RESOLVE FLAGS HERE: Create a simple list of keys to display
    active_flags = []
    if args.lines: active_flags.append("lineCount")
    if args.words: active_flags.append("wordCount")
    if args.bytes: active_flags.append("byteCount")

    # Default behavior: show all if no flags are provided
    if not active_flags:
        active_flags = ["lineCount", "wordCount", "byteCount"]

    all_file_stats = []
    exit_code = 0

    # Handle Standard Input
    if not args.files:
        stdin_content = sys.stdin.read()
        stats = calculate_stats(stdin_content, "")
        print_formatted_report(stats, active_flags)
        return

    # Process files
    for file_path in args.files:
        try:
            with open(file_path, "rb") as f:
                raw_bytes = f.read()
                content = raw_bytes.decode("utf-8", errors="ignore")
                stats = calculate_stats(content, file_path, len(raw_bytes))

            all_file_stats.append(stats)
            print_formatted_report(stats, active_flags)
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
        print_formatted_report(grand_totals, active_flags)

    if exit_code != 0:
        sys.exit(exit_code)

if __name__ == "__main__":
    main()