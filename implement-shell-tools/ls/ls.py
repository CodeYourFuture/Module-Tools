import argparse
import os

# create parser
parser = argparse.ArgumentParser(description="Simple ls tool")

parser.add_argument("-1", dest="one", action="store_true", help="one item per line")
parser.add_argument("-a", action="store_true", help="show hidden files")
parser.add_argument("path", nargs="?", default=".", help="directory path")

args = parser.parse_args()


def list_files(path):
    try:
        files = os.listdir(path)

        # if -a is NOT used, hide files starting with "."
        if not args.a:
            files = [f for f in files if not f.startswith(".")]

        # sort like real ls
        files.sort()

        # print results
        if args.one:
            for f in files:
                print(f)
        else:
            print("  ".join(files))

    except FileNotFoundError:
        print(f"Error: {path} not found")


# run
list_files(args.path)