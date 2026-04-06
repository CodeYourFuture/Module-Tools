import argparse

parser = argparse.ArgumentParser(
    prog="custom cat in python",
    description="trying to match behaviour in actual cat"
)

parser.add_argument("-b", "--non_blank", action="store_true", help="add number at the beginning of non blank line")
parser.add_argument("-n", "--number", action="store_true", help="add number at the beginning of each line")
parser.add_argument("file_path", nargs="+", help="file path to process")

args = parser.parse_args()

count = 1

for path in args.file_path:
    with open(path, "r") as file:
        context = file.read().rstrip().split("\n")
        for line in context:
            if (args.non_blank):
                if (len(line) != 0):
                    print(f'{str(count).rjust(6, " ")}  {line}')
                    count += 1
                else:
                    print(line)
            elif (args.number):
                print(f'{str(count).rjust(6, " ")}  {line}')
                count += 1
            else:
                print(line)