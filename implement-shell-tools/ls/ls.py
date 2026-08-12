import os
import sys

args = sys.argv[1:]

show_all = "-a" in args

directory = "."

for arg in args:
    if not arg.startswith("-"):
        directory = arg

files = sorted(os.listdir(directory))

if show_all:
    files = [".", ".."] + files
else:
    files = [file for file in files if not file.startswith(".")]

for file in files:
    print(file)
