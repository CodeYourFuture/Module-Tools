import argparse

parser = argparse.ArgumentParser(
    prog="wc shell tool",
    description="making wc tool with python"
)

parser.add_argument(
    "files",
    nargs="+",
    help="file or files to work on"
)
parser.add_argument(
    "-w",
    action="store_true",
    help="counting words"
)
parser.add_argument(
    "-l",
    action="store_true",
    help="counting lines"
)
parser.add_argument(
    "-c",
    action="store_true",
    help="counting char"
)

args = parser.parse_args()

for file in args.files:
    try:
        with open(file, "r") as f:
            content = f.read()
            word_count= len(content.split())
            line_count = content.count("\n")
            char_count = len(content)
            if args.w:
                print(f"word count of file {file} is : ", word_count)
            elif args.l:
                
                print(f"line count of file {file} is : ", line_count)
            elif args.c:
                
                print(f"char count of file {file} is : ", char_count)
            else:
                print(f"line: {line_count}, word: {word_count}, char: {char_count},  {file}")
    except FileNotFoundError:
        print(f"wc: {file}: file or directory not found")


