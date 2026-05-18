import sys
import os

def main():
    argv = sys.argv[1:]
    
    dash = [arg for arg in argv if arg.startswith('-')]
    paths = [arg for arg in argv if not arg.startswith('-')]
    
    show_all = '-a' in dash
    
    target_dir = paths[0] if paths else '.'
    
    try:
        entries = os.listdir(target_dir)
    except FileNotFoundError:
        print(f"ls: {target_dir}: No such file or directory", file=sys.stderr)
        sys.exit(1)
    
    if show_all:
        result = ['.', '..'] + entries
    else:
        result = [e for e in entries if not e.startswith('.')]
    
    for entry in result:
        print(entry)

if __name__ == "__main__":
    main()

    