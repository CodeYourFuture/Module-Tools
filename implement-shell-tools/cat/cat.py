import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    usage="implement a simple cat"
)

# Flag to number all lines
parser.add_argument(
    "-n",
    action="store_true",
    help="Number all output lines"
)

# Flag to number only non-blank lines
parser.add_argument(
    "-b",
    action="store_true",
    help="Number non-blank output lines"
)

# Positional argument for files to read
parser.add_argument(
    "path",
    nargs="*",
    help="Files to read"
)

args = parser.parse_args()
# print(args)
line_number=1
for per_file in args.path :
    with open(per_file,"r") as f:
        if args.n or args.b :
            lines=f.readlines()
            for line in lines :
                if line=="\n" and args.b :
                    print(line,end="")
                else :   
                    print(line_number,line,end="")
                    line_number=line_number+1
        else :
            print(f.read(),end="")
        