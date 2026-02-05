import argparse
import sys


def read_files(paths):
    lines = []
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines.extend(f.read().splitlines())
        except OSError as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
            sys.exit(1)
    return lines


def main():
    parser = argparse.ArgumentParser(
        prog="display-content-of-a-file",
        description="cat is used to display the content of a file or print the content of a file.",
    )

    parser.add_argument("-n", action="store_true", help="number output lines")
    parser.add_argument("-b", action="store_true", help="number non-empty output lines")
    parser.add_argument("paths", nargs="+", help="The file path(s) to process")

    options = parser.parse_args()

    lines = read_files(options.paths)

    if options.b:
        line_num = 1
        for line in lines:
            if line.strip():
                print(f"{line_num:6} {line}")
                line_num += 1
            else:
                print(line)

    elif options.n:
        for i, line in enumerate(lines, start=1):
            print(f"{i:6} {line}")

    else:
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()

#python3 cat.py -b sample-files/*  