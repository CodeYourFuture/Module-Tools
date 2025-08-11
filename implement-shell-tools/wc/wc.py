import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description="Count lines, words, and bytes in files (like wc)")
    parser.add_argument("-l", action="store_true", help="count lines")
    parser.add_argument("-w", action="store_true", help="count words")
    parser.add_argument("-c", action="store_true", help="count bytes")
    parser.add_argument("files", nargs="+", help="files to read")
    options = parser.parse_args()

    total_lines = total_words = total_bytes = 0

    for file_path in options.files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = f.read()
            
            lines = data.count("\n")
            words = len(data.split())
            bytes_ = len(data.encode("utf-8"))

            total_lines += lines
            total_words += words
            total_bytes += bytes_

            print(format_output(lines, words, bytes_, os.path.basename(file_path), options))
        except Exception as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)

    if len(options.files) > 1:
        print(format_output(total_lines, total_words, total_bytes, "total", options))

if __name__ == "__main__":
    main()
