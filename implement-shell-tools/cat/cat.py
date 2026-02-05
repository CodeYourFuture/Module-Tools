import argparse
parser = argparse.ArgumentParser(
    prog="my-cat",
    description="Simple cat clone with -n and -b options",
)

counterNumber = 1
parser.add_argument("-n", action="store_true", help="number all lines")
parser.add_argument("-b", action="store_true", help="The character to search for" )
parser.add_argument("path", nargs="+", help="The file to search")

args = parser.parse_args()

for file_path in args.path:
    with open(file_path, "r") as f:
        content = f.read()
        arrText = content.split("\n")

        if args.b:
            for i in range(len(arrText )):
                if arrText[i].strip() != "":
                    print(counterNumber,arrText[i])
                    counterNumber += 1

        elif args.n:
          for i in range(len(arrText )):
              print(counterNumber, arrText[i])
              counterNumber += 1
        else:
            print(content)