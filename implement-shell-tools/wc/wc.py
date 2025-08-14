import argparse
import os

parser = argparse.ArgumentParser(description="Python implementation of wc command")

parser.add_argument("-l", action="store_true", help="Print line count")

parser.add_argument("-w", action="store_true", help="Print word count")

parser.add_argument("-c", action="store_true", help="Print byte count")

parser.add_argument("files", nargs="+", help="Files to process")

args = parser.parse_args()

total_lines = 0
total_words = 0
total_bytes = 0

multiple_files = len(args.files) > 1 # to store totals if muliple files

for file in args.files:
    if not os.path.isfile(file):
        print(f"wc: {file}: No such file or directory")
        continue

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.count("\n")
        words = len(content.split())
        tbytes = os.path.getsize(file)

    
        
        total_lines += lines
        total_words += words
        total_bytes += tbytes

        if args.l:
            print(f"{lines:} {file}")

        elif args.w:
            print(f"{words:} {file}")

        elif args.c:
            print(f"{tbytes:} {file}")        

        else:
            print(f"{lines:>3} {words:>3} {tbytes:>3} {file}") # to print data from per file

#to print total output
if multiple_files:
    if args.l:
        print(f"{total_lines:} total")

    elif args.w:
        print(f"{total_words:} total")

    else:
        print(f"{total_lines:>3} {total_words:>3} {total_bytes:>3} total")    
                
        
                