import argparse
import os

parser = argparse.ArgumentParser(
    prog="ls",
    description="List directory contents",
)
parser.add_argument("-1", action="store_true", help="Force output to be one entry per line.")
parser.add_argument("-a", action="store_true", help="Include directory entries whose names begin with a dot (`.`).")
parser.add_argument("paths", nargs="*", default=["."], help="Paths to list")
args = parser.parse_args()

for i, path in enumerate(args.paths):
    read_children = os.listdir(path)
    children = []
    longest = 0
    if args.a:
        children.extend([".", ".."])
    for child in sorted(read_children):
        if args.a or not child.startswith("."):
            children.append(child)
            longest = max(longest, len(child))
    padTo = longest + (0 if longest % 8 == 0 else 8 - (longest % 8))
    if i > 0:
        print()
    if len(args.paths) > 1:
        print(f"{path}:")
    if getattr(args, "1"):
        print("\n".join(children))
    else:
        print("".join(map(lambda child: child.ljust(padTo), children)).rstrip())
