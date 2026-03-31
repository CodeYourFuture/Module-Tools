import argparse
import os
import re

parser = argparse.ArgumentParser(
    prog="custom ls in python",
    description="trying to match behaviour as the actual ls"
)

parser.add_argument("-a", "--show_hidden", help="show hidden files")
parser.add_argument("path", help="directory path to process", nargs="?", default=".")

args = parser.parse_args()

files_array = os.listdir(args.path)

if (not args.show_hidden):
    filtered_list = [file for file in files_array if re.match(r"^(?!\.)", file)]
    sorted_file_list = sorted(filtered_list, key=lambda file_name: file_name.lower())
    formatted_list = [f"\033[1;34m{file}\033[0m" if os.path.isdir(os.path.join(args.path, file)) else file for file in sorted_file_list]
    print("  ".join(formatted_list))
