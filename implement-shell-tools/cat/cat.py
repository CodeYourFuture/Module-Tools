import argparse

parser = argparse.ArgumentParser(
    prog="cat.py",
    description="Display contents of files with optional line numbering."
)

group = parser.add_mutually_exclusive_group()

group.add_argument("-n", action="store_true", help="Number all lines")
group.add_argument("-b", action="store_true", help="Number non-blank lines")
parser.add_argument("files", nargs="+", help="Files to display")

args = parser.parse_args()

# Check if user used -n or -b
number_all_lines = args.n
number_non_blank = args.b

# Loop through all file paths
for file_path in args.files:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line_num, line in enumerate(lines, start=1):
            # -n: number all lines
            if number_all_lines:
                print(f"{line_num:6}\t{line}", end="") # 'line_num:6' means align right

            # -b: number only non-blank lines
            elif number_non_blank:
                if line.strip() != "":
                    print(f"{line_num:6}\t{line}", end="")
                else:
                    print(line, end="")

            # No flags: just print the line
            else:
                print(line, end="")
