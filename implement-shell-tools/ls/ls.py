import argparse
import os


parser = argparse.ArgumentParser(
    prog="The ls program",
    description="Implements the ls program"
)
parser.add_argument('dir', nargs='?', type=str, help="Path to the directory to list", default='.')
parser.add_argument("-1", "--one", action="store_true", help="list the directory files one per line")

args = parser.parse_args()

def read_dir():
    one = args.one
    dir = args.dir
    contents = os.listdir(dir)
    for content in contents:
        if one:
            print(content)
    if not one:
        print(' '.join(contents))
    

read_dir()