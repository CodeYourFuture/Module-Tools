import argparse
import sys

def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="cat",
        description="Concatenate and display files, optionally numbering lines."
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--number", action="store_true", help="Number all output lines, starting at 1.")
    group.add_argument("-b", "--number-nonblank", action="store_true", help="Number non-empty output lines, starting at 1.")
    parser.add_argument("paths", nargs='+', help="Files to read ('-' for stdin).")

    return parser.parse_args()

def read_file_content(path):
    try:
        if path == "-":
            return sys.stdin.read()
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return ""

def extract_content_lines(content):
    return content.splitlines()

def output_lines(lines, number_all, number_nonblank):
    line_number = 1
    for line in lines:
        if number_all:
            print(f"{line_number:6}\t{line}")
            line_number += 1
        elif number_nonblank:
            if line.strip() != "":
                print(f"{line_number:6}\t{line}")
                line_number += 1
            else:
                print()
        else:
            print(line)

def main():
    args = setup_arguments()
    all_lines = []

    for path in args.paths:
        content = read_file_content(path)
        lines = extract_content_lines(content)
        all_lines.extend(lines)

    output_lines(all_lines, args.number, args.number_nonblank)

if __name__ == "__main__":
    main()
