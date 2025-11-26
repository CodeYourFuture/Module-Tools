import os
import argparse

parser=argparse.ArgumentParser(prog="cat",usage="implement a simple ls python")
parser.add_argument("-1",dest="one",action="store_true")
parser.add_argument("-a",action="store_true")
parser.add_argument("path",nargs="*",help="path to list files")
args=parser.parse_args()

paths=args.path
if len(paths)==0 : paths=["."]

for path in paths :
    files_list=os.listdir(path)
    files_list.sort(key=str.lower)
for item in files_list :
  if args.one and args.a :
     print(item)
  elif args.one :
      if not item.startswith(".") : 
        print(item)
