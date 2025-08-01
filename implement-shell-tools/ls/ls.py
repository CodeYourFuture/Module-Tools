import os
import argparse

def ls(path='.', one_column=False, show_hidden=False):
    try:
        files = os.listdir(path)
        if not show_hidden:
            files = [f for f in files if not f.startswith('.')]
        files.sort()
        
        if one_column:
            print(*files, sep='\n')
        else:
            print(*files)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-1', action='store_true', help='list one file per line')
    parser.add_argument('-a', action='store_true', help='show hidden files')
    parser.add_argument('path', nargs='?', default='.', help='directory to list')
    args = parser.parse_args()
    
    ls(args.path, args.__dict__['1'], args.a)

if __name__ == "__main__":
    main()