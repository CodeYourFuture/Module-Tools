import argparse
import os

def show_unhidden_files(listDir):
    for file in listDir:
        if not file.startswith('.'):
            print(file)
def show_all_files(listDir):
    for file in listDir:
        print(file)


parser = argparse.ArgumentParser(
    prog="my-ls",
    description="Simple ls clone with -a and -l options",
)

parser.add_argument("-a", action="store_true", help="include hidden files")
parser.add_argument("-1", dest="one" ,action="store_true", help="use a long listing format")
parser.add_argument("path", nargs="?", default=".", help="The directory to list")
args = parser.parse_args()





fn = args.path
listDir = os.listdir(fn)
if  fn!="":
    if args.a and args.one:
        show_all_files(listDir)
    elif args.a:
        show_all_files(listDir)
    elif args.one:
        show_unhidden_files(listDir)
   
    else:
        show_unhidden_files(listDir)

