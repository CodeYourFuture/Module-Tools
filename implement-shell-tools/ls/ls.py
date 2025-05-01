import os
import sys

show_all ="-a" in sys.argv

paths = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if not paths:
    paths =["."]

for path in paths:
    if os.path.isdir(path):
        try:
            entries = sorted(os.listdir(path))
            for entry in entries:
                if show_all or not entry.startswith("."):
                    print(entry)
        except Exception as e:
            print(f"ls: cannot access '{path}': {e}")
    elif os.path.isfile(path):
        print(os.path.basename(path))
    else:
        print (f"ls:'{path}': no such file or directory")




