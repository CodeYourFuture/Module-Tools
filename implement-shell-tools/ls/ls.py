import argparse
import os

parser = argparse.ArgumentParser(prog="ls")
parser.add_argument("-1", dest="one", action="store_true")
parser.add_argument("-a", action="store_true")
parser.add_argument("paths", nargs="*", default=["."])

args = parser.parse_args()


def get_files(path):
    files = sorted(os.listdir(path))

    if args.a:
        return [".", ".."] + files

    return [f for f in files if not f.startswith(".")]


# Print all files first
for path in args.paths:
    if not os.path.isdir(path):
        if args.one:
            print(path)
        else:
            print(path, end="     ")
print()

# Print directories
for path in args.paths:
    if os.path.isdir(path):

        if len(args.paths) > 1:
            print(f"\n{path}:")

        files = get_files(path)

        if args.one:
            for file in files:
                print(file)
        else:
            print("   ".join(files))