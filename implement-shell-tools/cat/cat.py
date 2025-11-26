import sys
import glob
import argparse

parser=argparse.ArgumentParser(prog="cat",
                               usage="implement a simple cat")
parser.add_argument("-n",action="store_true",help="number the output lines")
parser.add_argument("-b",action="store_true",help="number the output lines without blank ones")
parser.add_argument("path",nargs="*",help="files to read")
args=parser.parse_args()
print(args)
for per_file in args.path :
    with open(per_file,"r") as f:
     print(f.read())
        