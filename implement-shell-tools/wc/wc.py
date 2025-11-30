import argparse

parser = argparse.ArgumentParser(
    prog = "wc-count words, lines, characters",
    description = "wc shell command on python"
)

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Counts bytes")
parser.add_argument("path", nargs="+", help="The file to search")

args = parser.parse_args()

for file_path in args.path:
    with open(file_path, "r") as f:
        content = f.readlines()

    text = "".join(content)
    count_lines = len(content)
    count_words = len(text.split())
    count_bytes=len(text.encode("utf-8")) 

    if not (args.l or args.w or args.c):
        print (count_lines, count_words, count_bytes, file_path)
    if args.l:
        print (count_lines, file_path)
    if args.w:  
        print (count_words, file_path)
    if args.c:   
        print (count_bytes, file_path)
           






