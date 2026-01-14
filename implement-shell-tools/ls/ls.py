import argparse
import os

parser = argparse.ArgumentParser(
    prog="list-files-in-directory",
    description="List all files and directories in a directory",
)

parser.add_argument("-1", "--one", dest="one", help="Output one entry per line", action="store_true")
parser.add_argument("-a", help="List all files & directories, including hidden ones", action="store_true")
parser.add_argument("paths", nargs="*", default=["."], help="The file path to read from")

args = parser.parse_args()

if os.path.isdir(path):
    items = os.listdir(path)

    if args.a:
        items = ['.', '..'] + items

    if not args.a:
        items = [item for item in items if not item.startswith(".")]
    

    for i, item in enumerate(items):
        if args.one:
            print(item)
        else:
            print(item, end=" ")
    if not args.one:
        print()
    else:
        print(path)

    





    
