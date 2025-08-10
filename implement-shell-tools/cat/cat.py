#!/usr/bin/env python3
import argparse
import sys

def cat_file(file, args):
    try:
        with open(file, "r", encoding="utf-8") as f:
            line_number = 1
            non_blank_line_number = 1
            
            for line in f:  
                line = line.rstrip("\n") 
                
                prefix = ""
                if args.n:
                    prefix = f"{line_number}  "
                elif args.b and line:
                    prefix = f"{non_blank_line_number}  "
                
                print(f"{prefix}{line}")
                
                line_number += 1
                if line:
                    non_blank_line_number += 1
                    
    except FileNotFoundError:
        print(f"Error reading {file}: No such file or directory", file=sys.stderr)
    except PermissionError:
        print(f"Error reading {file}: Permission denied", file=sys.stderr)
    except Exception as error:
        print(f"Error reading {file}: {error}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(
        prog="cat",
        description="Print file contents"
    )
    parser.add_argument("-n", action="store_true", help="Number all lines")
    parser.add_argument("-b", action="store_true", help="Number non-blank lines only")
    parser.add_argument("files", nargs="+", help="Files to read")
    
    args = parser.parse_args()
    
    for file in args.files:
        cat_file(file, args)

if __name__ == "__main__":
    main()
