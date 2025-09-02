#!/usr/bin/env python3
import argparse

# implement-shell-tools/cat/cat.py
def main():
    parser = argparse.ArgumentParser(
    prog="cat",
    description="Implements a simple version of the 'cat' command to read and display file contents."
    )

    parser.add_argument("-n", help="Number lines", action="store_true")
    parser.add_argument("-b", help="Number non-blank lines", action="store_true")
    parser.add_argument("path", nargs="+", help="The file to search")

    args = parser.parse_args()

    counter = 1
    
    for file_path in args.path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                lines = content.split("\n")

                for i, line in enumerate(lines):
                    if i == len(lines) - 1 and line == "":  # Skip the last empty line if it exists
                        break
                    prefix = ""
                    if args.b:
                        if line != "":
                            prefix = str(counter).rjust(6) + " "
                            counter += 1
                    elif args.n:
                        prefix = str(counter).rjust(6) + " "
                        counter += 1
                    print(prefix + line)

        except FileNotFoundError:
            print(f"cat: {file_path}: No such file or directory")
        except Exception as e:
            print(f"cat: {file_path}: {e}")

if __name__ == "__main__":
    main()