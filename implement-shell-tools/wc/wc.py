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

l = True
w = True
c = True

dict = {}
adict = {}

for file in args.path:
    f = open(file)
    dict[file] = f.read().split("\n")
    adict[file] = f.read()

for file in args.path:
    f = open(file)
    adict[file] = f.read()

def print_helper(line, word, byte, file_name):
    text = [" "]
    if l == True:
        text.append(str(line))
        text.append(" ")
    if w == True:
        text.append(str(word))
        text.append(" ")
    if c == True:
        text.append(str(byte))
        text.append(" ")
    text.append(file_name)
    print("".join(text))
    
for f in dict:
    word_per_line = 0
    byte_per_line = 0
    for line in dict[f]:
        word_per_line += len(line.split())
    for line in adict[f]:
        byte_per_line += len(line.encode("utf-8"))
    lines += len(dict[f]) - 1
    words += word_per_line
    bytes += byte_per_line
    print_helper(len(dict[f]) - 1, word_per_line, byte_per_line, f)

if len(args.path) > 1:
    print_helper(lines, words, bytes, "total")