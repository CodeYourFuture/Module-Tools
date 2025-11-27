import argparse
import os

parser=argparse.ArgumentParser(prog="wc",usage="implement a simple wc in python")
parser.add_argument("-l",action="store_true",help="count of lines")
parser.add_argument("-w",action="store_true",help="count of words")
parser.add_argument("-c",action="store_true",help="count of bytes")
parser.add_argument("path",nargs="+")
args=parser.parse_args()


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
        if not (args.l or args.w or args.c):
            args.l = True
            args.w = True
            args.c = True 
        print((f"{lines_count:<5}" if args.l else "")+
              (f"{words_count:<5}" if args.w else "")+
              (f"{bytes_count:<5}" if args.c else "")+
              f"{file:<20}")
        words_count=0

if len(paths)>1 :        
    print((f"{total_lines:<5}" if args.l else "")+
        (f"{total_words:<5}" if args.w else "")+
        (f"{total_bytes:<5}" if args.c else "")+
        "total")        