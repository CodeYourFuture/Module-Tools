import argparse
import os

# implement-shell-tools/ls/ls.py
def main():
    parser = argparse.ArgumentParser(
    prog="ls",
    description="Implements a simple version of the 'ls' command to list files in a directory."
    )

    parser.add_argument("-1", help="", action="store_true")
    parser.add_argument("-a", help="", action="store_true")
    parser.add_argument("directory", nargs="?", default=".", help="The directory to search")

    args = parser.parse_args()

    try:
        files = os.listdir(args.directory)

        if not args.a:
            files = [f for f in files if not f.startswith(".")]
        
        files = sorted(files)

        for f in files:
            print(f)

    except FileNotFoundError:
        print(f"ls: {args.directory}: No such file or directory")
    except NotADirectoryError:
        print(args.directory)
    except Exception as e:
        print(f"ls: {args.directory}: {e}")

if __name__ == "__main__":
    main()