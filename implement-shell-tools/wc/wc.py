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


count_total_lines = 0
count_total_words = 0
count_total_bytes =  0  

for file_path in args.path:
    with open(file_path, "r") as file:
        content = file.read()

    count_lines = content.count("\n")
    count_words = len(content.split())
    count_bytes=len(content.encode("utf-8")) 

    count_total_lines += count_lines 
    count_total_words += count_words
    count_total_bytes += count_bytes   

    if not (args.l or args.w or args.c):
        print (count_lines, count_words, count_bytes, file_path)
    else:
        line = ""
        if args.l:
            line += f"{count_lines}  "
        if args.w:  
            line += f"{count_words}  "
        if args.c:   
            line += f"{count_bytes}  "
        line += f"{file_path}"
        print(line)
if len(args.path) > 1:
    if not (args.l or args.w or args.c):
        print (count_total_lines, count_total_words, count_total_bytes, " total")
    else:
        line = ""
        if args.l:
            line += f"{count_total_lines}  "
        if args.w:  
            line += f"{count_total_words}  "
        if args.c:   
            line += f"{count_total_bytes}  "
        line += " total"
        print(line)
           






