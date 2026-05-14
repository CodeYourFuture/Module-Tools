import sys
import argparse

def read_and_output_files():
    # Setup Argument Parser (Equivalent to 'commander')
    parser = argparse.ArgumentParser(description="Python implementation of a basic cat-like utility")
    parser.add_argument("-n", "--number", action="store_true", help="number all output lines")
    parser.add_argument("-b", "--number-nonblank", action="store_true", help="number only non-empty lines")
    parser.add_argument("files", nargs="+", help="files to read")

    args = parser.parse_args()

    line_number = 1

    for file_path in args.files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    # 1. Handle -b logic (number only non-blank lines)
                    if args.number_nonblank:
                        # A truly blank line is JUST a newline character (\n or \r\n)
                        if line == "\n" or line == "\r\n":
                            sys.stdout.write(line)
                        else:
                            # Standard cat uses a tab (\t) after the line number
                            sys.stdout.write(f"{str(line_number).rjust(6)}\t{line}")
                            line_number += 1

                    # 2. Handle -n logic (number all lines)
                    elif args.number:
                        sys.stdout.write(f"{str(line_number).rjust(6)}\t{line}")
                        line_number += 1

                    # 3. Handle standard output
                    else:
                        sys.stdout.write(line)
                        
        except Exception as err:
            print(f"cat: {file_path}: {err}", file=sys.stderr)

if __name__ == "__main__":
    read_and_output_files()