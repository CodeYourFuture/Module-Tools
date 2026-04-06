import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="wc implementation",
)

parser.add_argument("path", help="The file to process")
parser.add_argument("-l", action="store_true", help="count lines")
parser.add_argument("-w", action="store_true", help="count words")
parser.add_argument("-c", action="store_true", help="count characters")


args =parser.parse_args()
with open(args.path,"r") as f:
    content = f.read()

line_counter = len(content.split("\n"))-1
words_counter = len(content.split())
characters_counter = len(content)
if(not args.l and not args.w and not args.c):
 print(f"{line_counter}  {words_counter}  {characters_counter} {args.path}")

else:
 results = []
 if(args.l):results.append(line_counter)
 if(args.w):results.append(words_counter)
 if(args.c):results.append(characters_counter)
 results=" ".join(map(str,results))
 print(results,args.path)
