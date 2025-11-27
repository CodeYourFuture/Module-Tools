import argparse

parser=argparse.ArgumentParser(prog="wc",usage="implement a simple wc in python")
parser.add_argument("path",nargs="+")
args=parser.parse_args()

print(args.path)
paths=args.path
for path in paths :
    with open(path,"r") as f :
        lines=f.readlines()
        print(len(lines) , path)