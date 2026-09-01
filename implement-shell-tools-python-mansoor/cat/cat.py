import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and display files",
)

parser.add_argument(
    "-n",
    action="store_true",
    help="number all lines",
)

parser.add_argument(
    "-b",
    action="store_true",
    help="number non-empty lines",
)

parser.add_argument(
    "files",
    nargs="+",
    help="the files to read",
)

args = parser.parse_args()

line_number = 1

for filename in args.files:
    try:
        with open(filename) as file:
            for line in file:
                content = line.rstrip("\n")

                if args.b and content == "":
                    print()
                    continue

                if args.n or args.b: 
                    print(f"{line_number}\t{content}")
                    line_number +=1 
                else: 
                    print(content)

    except OSError as error:
        print(f"{error.strerror}")