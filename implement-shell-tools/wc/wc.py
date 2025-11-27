import argparse
import os

parser=argparse.ArgumentParser(prog="wc",usage="implement a simple wc in python")
parser.add_argument("path",nargs="+")
args=parser.parse_args()

# print(args.path)
paths=args.path
words_count=0
total_lines=0
total_words=0
total_bytes=0

for file in paths :
    with open(file,"r") as f :
        bytes_count=os.path.getsize(file)
        lines=f.readlines()
        lines_count=len(lines)
        for line in lines :
            words_count+=len(line.split())
        total_lines +=lines_count
        total_bytes += bytes_count
        total_words +=words_count    
        print(lines_count ,words_count , bytes_count, file)
        words_count=0
        
print(total_lines,total_words,total_bytes,"total")        