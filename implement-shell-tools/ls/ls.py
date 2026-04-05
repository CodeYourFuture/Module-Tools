import argparse
import os


def get_files(directory):
    files = os.listdir(directory)
    files.extend([".", ".."])
    files.sort(key=str.lower)
    return files


def display_files(files, show_all=False, one_per_line=False):
    if not show_all:
        files = [f for f in files if not f.startswith(".")]

    if one_per_line:
        for file in files:
            print(file)
    else:
        print("  ".join(files))


parser = argparse.ArgumentParser()
parser.add_argument("directory", nargs="?", default=".")
parser.add_argument("-1", dest="one_per_line", action="store_true", help="list one file per line")
parser.add_argument("-a", dest="show_all", action="store_true", help="include hidden files")

args = parser.parse_args()

try:
    files = get_files(args.directory)
    display_files(files, show_all=args.show_all, one_per_line=args.one_per_line)
except OSError as e:
    print(f"ls: {e}")