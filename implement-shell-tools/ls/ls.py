import sys
import os

args = sys.argv[1:]

# default folder = current folder
path = "."

# if user gives a folder
if len(args) > 1:
    path = args[1]

files = os.listdir(path)

for file in files:
    print(file)