import argparse
import os

parser = argparse.ArgumentParser(
    prog="Display items",
    description="Display the contents of a file reminiscent of the cat command"
)

parser.add_argument("-1", "--one", action="store_true", help="Lists the items of a folder each in a new line.")
parser.add_argument("-a", action="store_true", help="List the items of a folder including the ones that starts with .")
parser.add_argument("path", help="The file to search")

args = parser.parse_args()

files = os.listdir(args.path)

# print(files)

if args.a and args.one:
    for line in files:
        print(line)
elif args.a:
    print(' '.join(files))
elif args.one:
    for line in files:
        if line.startswith('.'):
            continue
        print(line)
else:
    l = [f for f in files if not f.startswith('.')]
    print(' '.join(l))
