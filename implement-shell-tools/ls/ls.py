import sys
import os

args = sys.argv[1:]

show_all = False
path = "."

for arg in args:

    if arg == "-a":
        show_all = True

    elif arg != "-1":
        path = arg

files = os.listdir(path)

for file in files:

    if not show_all and file.startswith("."):
        continue

    print(file)