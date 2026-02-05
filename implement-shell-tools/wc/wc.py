import argparse
parser = argparse.ArgumentParser(
    prog="my-wc",
    description="Simple wc clone with -l and -w options",
)
lineCounter = 0
wordCounter = 0
charCounter = 0
parser.add_argument("-l", action="store_true", help="count lines")
parser.add_argument("-w", action="store_true", help="count words")
parser.add_argument("-c", action="store_true", help="count characters")
parser.add_argument("path", nargs="+", default=".", help="The file to count")
args = parser.parse_args()

if not args.l and not args.w and not args.c:
    for file_path in args.path:
        with open(file_path, "r") as f:
            content = f.read()
        arrText = content.split("\n")
        lineCounter += len(arrText)
        arrWords = content.split()
        wordCounter += len(arrWords)
        charCounter += len(content)
    print("Line count:", lineCounter,"lines")
    print("Word count:", wordCounter,"words")
    print("Character count:", charCounter,"characters")
elif args.l and args.w:
    for file_path in args.path:
        with open(file_path, "r") as f:
            content = f.read()
        arrText = content.split("\n")
        lineCounter += len(arrText)
        arrWords = content.split()
        wordCounter += len(arrWords)
    print("Line count:", lineCounter,"lines")
    print("Word count:", wordCounter,"words")
elif args.l and args.c:
    for file_path in args.path:
        with open(file_path, "r") as f:
            content = f.read()
        arrText = content.split("\n")
        lineCounter += len(arrText)
        charCounter += len(content)
    print("Line count:", lineCounter,"lines")
    print("Character count:", charCounter,"characters")
elif args.l:
    for file_path in args.path:
        with open(file_path, "r") as f:
            content = f.read()
        arrText = content.split("\n")
        lineCounter += len(arrText)
    print("Line count:", lineCounter,"lines")

elif args.w:
    for file_path in args.path:
        with open(file_path, "r") as f:
            content = f.read()
        arrText = content.split()
        wordCounter += len(arrText)
    print("Word count:", wordCounter,"words")
elif args.c:
    for file_path in args.path:
        with open(file_path, "r") as f:
            content = f.read()
            charCounter += len(content)
    print("Character count:", charCounter,"characters")