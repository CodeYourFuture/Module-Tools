import argparse
import os

parser = argparse.ArgumentParser(description="wc command")
parser.add_argument("file", help="File or directory to read")
parser.add_argument("-l", dest="lines", action="store_true", help="count the number of lines")
parser.add_argument("-w", dest="words", action="store_true", help="count the number of words")
parser.add_argument("-c", dest="chars", action="store_true", help="count the number of characters")
args = parser.parse_args()

if os.path.isdir(args.file):
    files = os.listdir(args.file)
    for f in files:
        path = os.path.join(args.file, f)
        if os.path.isfile(path):
            with open(path, "r") as file_obj:
                text = file_obj.read()
            line_count = len(text.splitlines())
            word_count = len(text.split())
            char_count = len(text)
           
            if not (args.lines or args.words or args.chars):
                print(f"{line_count}\t{word_count}\t{char_count}\t{path}")
                continue
            output = []
            if args.lines:
                output.append(str(line_count))
            if args.words:
                output.append(str(word_count))
            if args.chars:
                output.append(str(char_count))
            output.append(path)
            print("\t".join(output))
else:
   
    with open(args.file, "r") as f:
        text = f.read()
    line_count = len(text.splitlines())
    word_count = len(text.split())
    char_count = len(text)
    if not (args.lines or args.words or args.chars):
        print(f"{line_count}\t{word_count}\t{char_count}\t{args.file}")
    else:
        output = []
        if args.lines:
            output.append(str(line_count))
        if args.words:
            output.append(str(word_count))
        if args.chars:
            output.append(str(char_count))
        output.append(args.file)
        print("\t".join(output))







            
            





