import argparse

parser = argparse.ArgumentParser(
    prog="Display items",
    description="Display the contents of a file reminiscent of the cat command"
)

parser.add_argument("-b", action="store_true", help="Numbers the nonempty lines in a file")
parser.add_argument("-n", action="store_true", help="Numbers all lines in a file")
parser.add_argument("path", help="The file to search")

args = parser.parse_args()

with open(args.path, "r") as f:
    content = f.read()

# print(content.splitlines())

counter = 1

for line in content.splitlines():
    if args.n:
        print(f"{counter:6}\t{line}")
        counter += 1
    elif args.b:
        if line.split() == []:
            print('')   
        else:
            print(f"{counter:6}\t{line}")
            counter += 1