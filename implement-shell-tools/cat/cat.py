import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+")
parser.add_argument("-n", action="store_true")
parser.add_argument("-b", action="store_true")

args = parser.parse_args()

line_number = 1

for file in args.files:
    try:
        f = open(file, "r")

        for line in f:
            if args.b and line.strip() != "":
                print(f"     {line_number}", line, end="")
                line_number += 1
            elif args.n and not args.b:
                print(f"     {line_number}", line, end="")
                line_number += 1
            else:
                print(line, end="")

        f.close()

    except:
        print("cat:", file, "not found")