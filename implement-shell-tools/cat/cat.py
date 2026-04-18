import sys
import argparse

def read_and_output_files():
    # 1. Setup Argument Parser (Equivalent to 'commander')
    parser = argparse.ArgumentParser(description="Python implementation of a basic cat-like utility")
    parser.add_argument("-n", "--number", action="store_true", help="number all output lines")
    parser.add_argument("-b", "--number-nonblank", action="store_true", help="number only non-empty lines")
    parser.add_argument("files", nargs="+", help="files to read")

    args = parser.parse_args()

    try:
        # 2. Read all file contents (Equivalent to Promise.all / fs.readFile)
        file_contents = []
        for file_path in args.files:
            with open(file_path, "r", encoding="utf-8") as f:
                file_contents.append(f.read())
        
        concatenated_content = "".join(file_contents)

        # 3. Process Logic
        if args.number:
            # -n logic: number all lines
            lines = concatenated_content.split("\n")
            output = []
            for index, line in enumerate(lines, start=1):
                # rjust(6) is equivalent to padStart(6)
                output.append(f"{str(index).rjust(6)}  {line}")
            sys.stdout.write("\n".join(output))

        elif args.number_nonblank:
            # -b logic: number only non-empty lines
            lines = concatenated_content.split("\n")
            output = []
            nonblank_line_number = 0
            for line in lines:
                if line.strip() == "":
                    output.append(line)
                else:
                    nonblank_line_number += 1
                    output.append(f"{str(nonblank_line_number).rjust(6)}  {line}")
            sys.stdout.write("\n".join(output))

        else:
            # No flags: standard output
            sys.stdout.write(concatenated_content)

    except Exception as err:
        print(f"Error reading multiple files: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    read_and_output_files()
