import argparse

parser = argparse.ArgumentParser(
    prog="check-for-cat",
    description="Implement my own version of cat in Python",
)

parser.add_argument("paths", nargs="+", help="The file paths to process")
parser.add_argument("-n", action="store_true", help="Number lines")
parser.add_argument("-b", action="store_true", help="Number non-blank lines")

args = parser.parse_args()

paths = args.paths
show_n = args.n
show_b = args.b

line_number = 1

for path in paths:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")

        if show_b:
            if line == "":
                print()
            else:
                numbered = str(line_number).rjust(6) + "\t" + line
                print(numbered)
                line_number += 1

        elif show_n:
            numbered = str(line_number).rjust(6) + "\t" + line
            print(numbered)
            line_number += 1

        else:
            print(line)