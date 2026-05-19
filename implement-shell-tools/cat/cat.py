import sys

args = sys.argv[1:]

path = args[0]

with open(path, "r") as file:
    content = file.read()
    print(content)