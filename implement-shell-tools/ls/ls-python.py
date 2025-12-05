import sys
import os

def main():
    args = sys.argv[1:]
    
    path = "."
    one_per_line = False
    show_hidden = False
    
    for arg in args:
        if arg == "-a":
            show_hidden = True
        elif arg == "-1":
            one_per_line = True
        elif not arg.startswith("-"):
            path = arg

    entries = os.listdir(path)

    entries.sort()

    if not show_hidden:
        entries = [f for f in entries if not f.startswith(".")]
    
    if one_per_line:
        for entry in entries:
            print(entry)
    else:
        print(" ".join(entries))

if __name__ == "__main__":
    main()