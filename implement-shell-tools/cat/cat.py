import sys

args = sys.argv[1:]

option = "none"
paths = []

# parse args
for arg in args:
    if arg == "-n":
        option = "n"
    elif arg == "-b":
        option = "b"
    else:
        paths.append(arg)

for path in paths:
    with open(path, "r") as file:
        lines = file.readlines()

        line_number = 1

        for line in lines:

            line = line.rstrip("\n")

            if option == "n":
                print(f"{line_number} {line}")
                line_number += 1

            elif option == "b":
                if line != "":
                    print(f"{line_number} {line}")
                    line_number += 1
                else:
                    print("")

            else:
                print(line)