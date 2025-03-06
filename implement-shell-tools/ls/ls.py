import argparse
import os


parser = argparse.ArgumentParser(
    prog="The ls program",
    description="Implements the ls program"
)
parser.add_argument('dir', nargs='?', type=str, help="Path to the directory to list", default='.')
parser.add_argument("-1", "--one", action="store_true", help="list the directory files one per line")

args = parser.parse_args()
print(args)

def read_dir():
    dir = args.dir
    contents = ' '.join(os.listdir(dir))
    print(contents)
    

read_dir()