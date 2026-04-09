import argparse

parser = argparse.ArgumentParser(prog="wc", description="Print  newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.")
parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
parser.add_argument("-l", "--line", help="print the newline counts", action="store_true")
parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
parser.add_argument("path", help="The file path", nargs="+")

args = parser.parse_args()

dict = {}

for file in args.path:
    f = open(file)
    text = []
    text.append(f.read())
    dict[file] = text

for f in dict:
    print(dict[f])

# print(dict)