import sys

args = sys.argv[1:]
path = args[0]

with open(path, "r") as file:
    content = file.read()

lines = content.split("\n")
words = content.split(" ")
chars = content

print(len(lines), len(words), len(chars))