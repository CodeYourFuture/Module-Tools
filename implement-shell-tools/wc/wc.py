import argparse
import os

parser = argparse.ArgumentParser(description="wc command")
parser.add_argument("file", help="File or directory to read")
parser.add_argument("-l", dest="lines", action="store_true", help="count the number of lines")
parser.add_argument("-w", dest="words", action="store_true", help="count the number of words")
parser.add_argument("-c", dest="chars", action="store_true", help="count the number of characters")
args = parser.parse_args()

def output(line_count ,word_count ,char_count,filename,args):
    if not(args.lines or args.words or args.chars):
        return f"{line_count}\t{word_count}\t{char_count}\t{filename}"
    output=[]
    if args.lines:
        output.append(str(line_count))
    if args.words:
        output.append(str(word_count))    
    if args.chars:
        output.append(str(char_count))
    output.append(filename)  
    return "\t".join(output)    

def count_file(path):
    with open(path) as f:
        text = f.read()
    return (
        len(text.splitlines()),
        len(text.split()),
        len(text),
    )

if os.path.isdir(args.file):
    files = os.listdir(args.file)
    for f in files:
        path = os.path.join(args.file, f)
        if os.path.isfile(path):
            line_count, word_count, char_count = count_file(path)
            print(output(line_count, word_count, char_count, path, args))
else:
    line_count, word_count, char_count = count_file(args.file)
    print(output(line_count, word_count, char_count, args.file, args))