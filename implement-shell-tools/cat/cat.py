import argparse
# -------------------------------------------
# Set up the argument parser
# -------------------------------------------

parser = argparse.ArgumentParser(
    prog ="display-file-content",
    description = "Implement cat command with -n and -b flag support",
    )

parser.add_argument("-n", "--number-all-lines",
                    action="store_true",
                    help="Number every line in the file"
                    )

parser.add_argument("-b", "--number-non-empty-lines",
                    action="store_true",
                    help="Number non empty lines in the file"
                    )

parser.add_argument("paths", nargs="+", help="File paths to process")

args = parser.parse_args()

# -------------------------------------------
#  Implement functionality
# -------------------------------------------

line_number = 1

for filepath in args.paths:
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if args.number_non_empty_lines:
                if line.strip() == "":
                    print(line, end="")
                else:
                    print(f"{line_number} {line}", end="")
                    line_number += 1

            elif args.number_all_lines:
                    print(f"{line_number} {line}", end="")
                    line_number +=1

            else:
                print(line, end="")
