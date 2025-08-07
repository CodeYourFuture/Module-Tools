import argparse
import os

parser = argparse.ArgumentParser(description="Python implementation of wc command")

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
        tbytes = len(content.encode("utf-8"))

        
        total_lines += lines
        total_words += words
        total_bytes += tbytes
      
        print(f"{lines:>7} {words:>7} {tbytes:>7} {file}") # to print data from per life

#to print total output
if multiple_files:
    print(f"{total_lines:>7} {total_words:>7} {total_bytes:>7} total")    
                
        
                