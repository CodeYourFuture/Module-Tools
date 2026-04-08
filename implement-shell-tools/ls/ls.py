import argparse

parser = argparse.ArgumentParser(prog="ls", description="List directory contents.  Ignore files and directories starting with a '.' by default")
parser.add_argument("-1", help="List one file per line.", action="store_true")
parser.add_argument("-a", help="Do not ignore hidden files (files with names that start with '.').", action="store_true")
parser.add_argument("path", help="The directory path (optional).", default=".", nargs="?")

args = parser.parse_args()

