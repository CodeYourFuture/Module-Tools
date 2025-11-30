import argparse

parser = argparse.ArgumentParser(
    prog = "cat-command",
    description = "cat shell command in python "
)

parser.add_argument("-n",  action="store_true", help="Display all lines numbers")
parser.add_argument("-b",  action="store_true", help="Display numbers non-empty lines")
parser.add_argument("path", nargs="+", help="The file to search")

args = parser.parse_args()

for file_path in args.path:
    with open(file_path, "r") as f:
        content = f.readlines()

    if args.n:
        number = 1
        for line in content:
            print(f"{number}\t{line.strip()}")
            number +=1
    elif args.b:
        number = 1
        for line in content:
            if line.strip() !="":
                print(f"{number}\t{line.strip()}")
                number +=1
            else: 
                print("")
    else:
        print("".join(content))
   
               


# if args.b:
#     number=1
#     for line in content:
#         print

# print(content)