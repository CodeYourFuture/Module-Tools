import argparse
import glob

parser = argparse.ArgumentParser(
    prog="mycat",
    description="Outputs the content of the given file(s), like the cat command",
)

parser.add_argument("-n", help="Number all lines", action="store_true")
parser.add_argument("-b", help="Number all non-blank lines", action="store_true")
parser.add_argument("path", help="The file to display(allowing wildcards)", nargs="+")

args = parser.parse_args()

file_list = []
for path in args.path:
    file_list.extend(glob.glob(path))

line_number = 1

for filename in file_list:
    try:
        with open(filename, "r") as f:
            for line in f:
                stripped = line.rstrip("\n")

                if args.b:
                    if stripped:
                        print(f"{line_number:>6}\t{stripped}")
                        line_number += 1
                    else:
                        print("")
                elif args.n:
                    print(f"{line_number:>6}\t{stripped}")
                    line_number += 1
                else:
                    print(line, end="")
    except FileNotFoundError:
        print(f"mycat: {filename}: No such file or directory")
