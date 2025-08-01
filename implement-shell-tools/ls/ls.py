import os
import argparse
import sys

parser = argparse.ArgumentParser(
    prog="ls",
    description="list directory contents",
)

parser.add_argument("-1",dest="one",action='store_true', help="list one file per line")
parser.add_argument("-a", action='store_true', help="Used to list all files, including hidden files, in the current directory")
parser.add_argument("path", nargs="?", default=".", help="The path to search")

args = parser.parse_args()

def arguments_proceeding(files):
    if args.one:
        files.sort()
        for f in files:
            print(f)

    if not args.a:
        files = [f for f in files if not f.startswith(".")]


def path_proceeding(path_argument):
    if os.path.isfile(path_argument):
        print(path_argument)
    elif os.path.isdir(path_argument):
        files = os.listdir(path_argument)
        arguments_proceeding(files)
#     elif not path_argument:
#         print("no")

# if not args.path:
#     print("no")
path_proceeding(args.path)



