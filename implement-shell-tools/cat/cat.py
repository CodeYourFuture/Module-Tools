import argparse

parser = argparse.ArgumentParser(prog="cat", description="Prints the output of a file to the console")
parser.add_argument("-n", "--number", help="Displays the lines along with their number")
parser.add_argument("path", help="The file path", nargs="+")

args = parser.parse_args()

text = ""

for file in args.path:
    f = open(file)
    text += f.read()

print(text)