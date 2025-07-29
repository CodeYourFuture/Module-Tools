#!/usr/bin/env python3
import argparse
import os
import sys

def main():
    # Set up command options
    parser = argparse.ArgumentParser(
        prog="ls",
        description="List directory contents"
    )
    parser.add_argument("-1", dest="one", action="store_true", help="One entry per line")
    parser.add_argument("-a", action="store_true", help="Show hidden files")
    parser.add_argument("dir", nargs="?", default=".", help="Directory to list")
    
    args = parser.parse_args()
    
    # Get directory from arguments or use current directory
    directory = args.dir
    
    try:
        # Read directory contents
        files = os.listdir(directory)
        
        # Add . and .. if using -a
        all_files = [".", ".."] if args.a else []
        
        # Add regular files (filter hidden unless -a is used)
        for file in files:
            if args.a or not file.startswith("."):
                all_files.append(file)
        
        # Output
        if args.one:  # -1 flag
            for file in all_files:
                print(file)
        else:
            print(" ".join(all_files))
            
    except FileNotFoundError:
        print(f"ls: {directory}: No such file or directory", file=sys.stderr)
    except PermissionError:
        print(f"ls: {directory}: Permission denied", file=sys.stderr)
    except Exception as error:
        print(f"ls: {directory}: {error}", file=sys.stderr)

if __name__ == "__main__":
    main()