import argparse
import os

parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and print files",
)

parser.add_argument(
    "-n", action="store_true", help="Number the output lines, starting at 1"
)
parser.add_argument(
    "-b", action="store_true", help="Number the non-blank output lines, starting at 1"
)
parser.add_argument("path", nargs="+", help="The path to search")

args = parser.parse_args()
for path in args.path:
    if os.path.isfile(path):
        with open(path) as file:
            lines = file.readlines()
            line_num = 1
            for line in lines:
                lin = line.rstrip("\n")
                if args.b:
                    if lin == "":
                        print()
                    else:
                        print(line_num, lin)
                        line_num += 1
                elif args.n:
                    print("    ", line_num, lin)
                    line_num += 1

                else:
                    print(lin)
    else:
        print(f"cat: {path}: Is a directory")
