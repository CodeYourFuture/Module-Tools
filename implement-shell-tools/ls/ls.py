import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="wc",
    description="wc implementation",
)

parser.add_argument("path", nargs="?", help="The file to process", default=".")
parser.add_argument("-1", "--one_per_line",action="store_true", help="one file per line")
parser.add_argument("-a", action="store_true", help="Show hidden files")


args = parser.parse_args()

path = Path(args.path)  # path is an object represent a location on disk
   
# else:
#  for item in path.iterdir():  # iterdir is a method reads directory  contents
#     if args.a:
#         print(item.name)
#     else:
#         if not item.name.startswith("."):
#             print(item.name)  # each item is a Path object
items =[]
for item in sorted(path.iterdir()):
    if args.a or not item.name.startswith("."):
        items.append(item.name)

if(args.one_per_line):
    for name in items:
        print(name)
else:
    print(" ".join(items))