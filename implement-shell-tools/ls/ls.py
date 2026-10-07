import sys
import os

args = sys.argv[1:]

one_line = False
show_hidden = False
targets = []

for arg in args:
    if arg == "-1":
        one_line = True
    elif arg == "-a":
        show_hidden = True
    else:
        targets.append(arg)

if len(targets) == 0:
    targets.append(".")


def list_directory(directory):
    files = os.listdir(directory)

    if not show_hidden:
        files = [file for file in files if not file.startswith(".")]

    files.sort()

    if one_line:
        print("\n".join(files))
    else:
        print("  ".join(files))


def list_target(target):
    try:
        if os.path.isdir(target):
            list_directory(target)
        else:
            print(target)

    except Exception:
        print(f"ls: cannot access '{target}': No such file or directory")


for target in targets:
    list_target(target)