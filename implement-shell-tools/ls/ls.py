import argparse
import os


parser = argparse.ArgumentParser(
    prog="The ls program",
    description="Implements the ls program"
)
parser.add_argument('dir', nargs='?', type=str, help="Path to the directory to list", default='.')
parser.add_argument("-1", "--one", action="store_true", help="list the directory files one per line")

args = parser.parse_args()

def does_not_start_with_do(filename):
    return not filename.startswith('.')

def read_dir():
    one = args.one
    dir = args.dir
    files = os.listdir(dir)
    non_hidden_files_or_dirs = list(filter(does_not_start_with_do,files ))
    print(non_hidden_files_or_dirs, 'filtered elements')
    for content in files:
        if one:
            print(content)
    if not one:
        print(' '.join(files))
    

read_dir()