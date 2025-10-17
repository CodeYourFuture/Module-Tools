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

# Helper function to print counts in wc style
def print_counts(lines, words, bytes_, filename):
    output = []
    if args.l:
        output.append(str(lines))
    if args.w:
        output.append(str(words))
    if args.c:
        output.append(str(bytes_))
    
    # If no flags are given, print all three counts
    if not output:
        output = [f"{lines:>7}", f"{words:>7}", f"{bytes_:>7}"]
    
    print(" ".join(output), filename)

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

        # Print counts per file
        print_counts(lines, words, tbytes, file)

#to print total output
if multiple_files:
    print_counts(total_lines, total_words, total_bytes, "total")   
                
        
                