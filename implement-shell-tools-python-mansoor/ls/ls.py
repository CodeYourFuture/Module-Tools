import argparse
import os

parser = argparse.ArgumentParser(
    prog = "ls",
    description = "List directory content"
)

parser.add_argument(
    "paths",
    nargs = "*",
    default=["."],
    help= "the directory path to process",
)

parser.add_argument(
    "-1",
    "--one",
    action="store_true",
    help="list one file per line",

)

parser.add_argument(
    "-a",
    "--all",
    action="store_true",
    help="List all files including hidden files such as '.' and  '..' "
)

args = parser.parse_args()

for target_dir in args.paths:
    try:
        files = os.listdir(target_dir)

        if args.all:
            file_list = sorted([".", ".."] + files)
        else:
            file_list = []
            for name in files:
                if not name.startswith("."):
                    file_list.append(name)
            file_list.sort()

        if args.one: 
            for name in file_list:
                print(name)
        else: 
            print(" ".join(file_list))
    except OSError as error:
        print(f"{error.strerror}")