import argparse
import os
import re

def sort_list(file_list):
    return sorted(file_list, key=lambda file_name: re.sub(r"^\.", "", file_name).lower())

def format_list(file_list):
    return [f"\033[1;34m{file}\033[0m" if os.path.isdir(os.path.join(args.path, file)) else file for file in file_list]

parser = argparse.ArgumentParser(
    prog="custom ls in python",
    description="trying to match behaviour as the actual ls"
)

parser.add_argument("-a", "--show_hidden", action="store_true", help="show hidden files")
parser.add_argument("-1", "--one_item", action="store_true", help="show one item per one line")
parser.add_argument("path", help="directory path to process", nargs="?", default=".")

args = parser.parse_args()

files_array = os.listdir(args.path)

sorted_files_array = sort_list(files_array)

hidden_switched_list = [".", "..", *sorted_files_array] if args.show_hidden else [file for file in sorted_files_array if re.match(r"^(?!\.)", file)]

formatted_list = format_list(hidden_switched_list)

separator = "\n" if args.one_item else " "

print(separator.join(formatted_list))
