import sys

args = sys.argv[1:]

show_n = "-n" in args
show_b = "-b" in args

files = [arg for arg in args if not arg.startswith("-")]

content = ""

for file in files:
    with open(file, "r") as f:
        content += f.read()

lines = content.split("\n")

if lines and lines[-1] == "":
    lines.pop()

output = []

if show_n:
    for i, line in enumerate(lines, start=1):
        output.append(f"{str(i).rjust(6)}  {line}")

elif show_b:
    count = 1

    for line in lines:
        if line != "":
            output.append(f"{str(count).rjust(6)}  {line}")
            count += 1
        else:
            output.append("")

else:
    output = lines

print("\n".join(output))
