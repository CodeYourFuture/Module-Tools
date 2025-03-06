import argparse
import os


parser = argparse.ArgumentParser(
    prog="The ls program",
    description="Implements the ls program"
)
parser.add_argument('dir', nargs='?', type=str, help="Path to the directory to list", default='.')
parser.add_argument("-1", "--one", action="store_true", help="list the directory files one per line")

parser.add_argument("-a", "--hidden_files", action="store_true", help="list the directory files one per line")

args = parser.parse_args()

def does_not_start_with_do(filename):
    return not filename.startswith('.')

def read_dir():
    one = args.one
    hidden_files = args.hidden_files
    dir = args.dir
    files = os.listdir(dir)

    if hidden_files:
        files.extend(['.', '..'])

    for file in files:
        if hidden_files or not file.startswith('.'):
            if one:
                print(file)
            else:
                print(file, end=' ')
    if not one:
        print()

read_dir()