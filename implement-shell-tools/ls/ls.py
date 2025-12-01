import argparse
import os

parser = argparse.ArgumentParser(
    prog="list-files-in-directory",
    description="List all files and directories in a directory",
)

parser.add_argument("-1", "--one", dest="one", help="Output one entry per line", action="store_true")
parser.add_argument("-a", help="List all files & directories, including hidden ones", action="store_true")
parser.add_argument("path", help="The file path to read from")

args = parser.parse_args()

content = os.listdir(args.path)

all_content = content

if not args.a:
    all_content = list(filter(lambda name: not name.startswith("."), content))

for item in all_content:
    if args.one:
        print(item)
    else:
        print(item + " ")





    
