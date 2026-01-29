import os
import argparse

parser=argparse.ArgumentParser(prog="ls",usage="implement a simple ls python")
parser.add_argument("-1",dest="one",action="store_true")
parser.add_argument("-a",action="store_true")
parser.add_argument("path",nargs="*",help="path to list files")
args=parser.parse_args()

paths=args.path
if len(paths)==0 : paths=["."]

for path in paths :
    files_list=os.listdir(path)
    files_list.sort(key=str.lower)

    # Divide into hidden and non-hidden
    non_hidden = [f for f in files_list if not f.startswith(".")]
    hidden = [f for f in files_list if f.startswith(".")]

    # Sort each list
    non_hidden.sort(key=str.lower)
    hidden.sort(key=str.lower)

    # Add '.' and '..' at the start if -a
    if args.a:
        files_list = ['.', '..'] + non_hidden + hidden
    else:
        files_list = non_hidden

if args.one :           
    for item in files_list :
        print(item)
else:
    print("  ".join(files_list))        


