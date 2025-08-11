import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="display-content-of-a-file",
        description="cat is used to display the content of a file or print the content of a file."
    )
    parser.add_argument('-n', action='store_true', help='number output lines')
    parser.add_argument('-b', action='store_true', help='number non-empty output lines')
    parser.add_argument('paths', nargs='+', help="The file path(s) to process")

    options = parser.parse_args()

    combined_data = ""
    for path in options.paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                combined_data += f.read() + "\n"
        except Exception as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()










#python3 cat.py -b sample-files/*  