import argparse

parser = argparse.ArgumentParser(prog="wc", description="Print  newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.")
parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
parser.add_argument("-l", "--line", help="print the newline counts", action="store_true")
parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
parser.add_argument("path", help="The file path", nargs="+")

args = parser.parse_args()

lines = 0
words = 0
bytes = 0

dict = {}

for file in args.path:
    f = open(file)
    # text = []
    # text.append(f.read().split("\n"))
    # print(f.read().split("\n"))
    dict[file] = f.read().split("\n")
# print(dict)
for f in dict:
    word_per_line = 0
    byte_per_line = 0
    for l in dict[f]:
        word_per_line += len(l.split())
        byte_per_line += len(l.encode("utf-8"))
    # print(byte_per_line)
    print(str(len(dict[f]) - 1) + " " + str(word_per_line) + " " + f)

