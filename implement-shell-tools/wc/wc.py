import argparse
import os


# Set up argument parser for wc command
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

# Function to print counts for a file or total
def print_wc(lines, words, bytes_, name):
    # Print selected counts in formatted columns
    print(
        (f"{lines:<5}" if args.l else "") +
        (f"{words:<5}" if args.w else "") +
        (f"{bytes_:<5}" if args.c else "") +
        f"{name:<20}"
    )

# Loop through all files
for file in paths :
    with open(file,"r") as f :
        # Get file size in bytes
        bytes_count=os.path.getsize(file)
         # Read all lines
        lines=f.readlines()
        lines_count=len(lines)
        for line in lines :
            # Count words in file
            words_count+=len(line.split())
        
        # Update totals
        total_lines +=lines_count
        total_bytes += bytes_count
        total_words +=words_count   

        # If no flags provided, default to showing all counts
        if not (args.l or args.w or args.c):
            args.l = True
            args.w = True
            args.c = True 
        # Print counts for this file    
        print_wc(lines_count, words_count, bytes_count, file)

# If multiple files, print totals at the end
if len(paths)>1 :        
   print_wc(total_lines, total_words, total_bytes, "total")      
    
