import sys

args = sys.argv[1:]

for path in args:
    with open(path, "r") as file:
        content = file.read()

    lines = content.split("\n")
    words = content.split(" ")
    chars = content

    print(len(lines), len(words), len(chars), path)