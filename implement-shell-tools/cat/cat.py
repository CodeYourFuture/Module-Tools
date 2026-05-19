import sys

args = sys.argv[1:]

show_numbers = False
paths = []

# separate flags and paths
for arg in args:
    if arg == "-n":
        show_numbers = True
    else:
        paths.append(arg)

for path in paths:
    with open(path, "r") as file:
        lines = file.readlines()

        if show_numbers:
            i = 1
            for line in lines:
                print(f"{i} {line.rstrip()}")
                i += 1
        else:
            print("".join(lines))