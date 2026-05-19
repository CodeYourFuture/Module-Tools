import sys

args = sys.argv[1:]

option = "all"
paths = []

for arg in args:
    if arg == "-l":
        option = "l"
    elif arg == "-w":
        option = "w"
    elif arg == "-c":
        option = "c"
    else:
        paths.append(arg)

for path in paths:
    with open(path, "r") as file:
        content = file.read()

    lines = len(content.split("\n"))
    words = len(content.split(" "))
    chars = len(content)

    if option == "l":
        print(lines, path)
    elif option == "w":
        print(words, path)
    elif option == "c":
        print(chars, path)
    else:
        print(lines, words, chars, path)