import argparse

parser = argparse.ArgumentParser(
    prog="cat shell tool",
    description="making cat tool with oython"
)

parser.add_argument(
    "files",
    nargs="+",
    help="file to read"
)

parser.add_argument(
    "-n",
    "--number",
    action="store_true",
    help="add number to the lines"
)

parser.add_argument(
    "-b",
    "--number_nonblank",
    action="store_true",
    help="does not number the blank lines"
)

args = parser.parse_args()

number_line = 0
for file in args.files:
    with open(file, "r") as f:
        lines = f.readlines()

    for line in lines:
        if args.number_nonblank:
            if line.strip():
                number_line += 1
                print(f"{number_line} {line}", end="")
        elif args.number:
            number_line += 1
            print(f"{number_line} {line}", end="")
        else:
            print(line)
    



