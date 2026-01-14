
import argparse
import os

parser = argparse.ArgumentParser(
    prog="counter",
    description="Counts lines, words or characters in a file (or all files) inside a directory",
)

parser.add_argument("-l", "--line", dest="line", help="The number of lines in each file", action="store_true")
parser.add_argument("-w", "--word", dest="word", help="The number of words in each file", action="store_true")
parser.add_argument("-c", "--char", dest="char", help="The number of characters in each file", action="store_true")
parser.add_argument("paths", help="The file(s)/path(s) to read from", nargs="+")

args = parser.parse_args()


total_lines = 0
total_words = 0
total_characters = 0
file_count = 0


def counter(item):
    lines = len(item.strip().split("\n"))
    words = len(item.split())
    characters = len(item)
    return {"lines": lines, "words": words, "characters": characters}


def process_file(file_path):
    global total_lines, total_words, total_characters, file_count

    with open(path, "r") as f:
        content = f.read()

    stats = counter(content)

    if args.line:
        print(f"{stats['lines']} {file_path}}")
    elif args.word:
        print(f"{stats['words']} {file_path}}")
    elif args.char:
        print(f"{stats['characters']} {file_path}}")
    else:
        print(f"{stats['lines']} {stats['words']} {stats['characters']} {file_path}")

    total_lines += stats['lines']
    total_words += stats['words']
    total_characters += stats['characters']
    file_count += 1




for path in args.paths:
    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                with open(file_path, "r") as f:
                     content = f.read()
                
    

        



if file_count > 1:
    if args.line:
        print(f"{total_lines} total")
    elif args.word:
        print(f"{total_words} total")
    elif args.char:
        print(f"{total_characters} total")
    else:
        print(f"{total_lines} {total_words} {total_characters} total")




