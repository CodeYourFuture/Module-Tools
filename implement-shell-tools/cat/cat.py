import sys

args = sys.argv[1:]

number_all = "-n" in args
number_nonblank = "-b" in args

files = [arg for arg in args if arg not in ("-n", "-b")]

line_number = 1

for filename in files:
    try:
        with open(filename, "r") as file:
            content = file.read()

            lines = content[:-1].split("\n") if content.endswith("\n") else content.split("\n")

            for line in lines:
                if number_all:
                    print(f"{line_number:6}\t{line}")
                    line_number += 1

                elif number_nonblank and line != "":
                    print(f"{line_number:6}\t{line}")
                    line_number += 1

                else:
                    print(line)

    except Exception as err:
        print(f"cat: {filename}: {err}")
        