#!/usr/bin/env python3
import argparse
import sys

def main():
    # Set up command options
    parser = argparse.ArgumentParser(
        prog="cat",
        description="Print file contents"
    )
    parser.add_argument("-n", action="store_true", help="Number all lines")
    parser.add_argument("-b", action="store_true", help="Number non-blank lines only")
    parser.add_argument("files", nargs="+", help="Files to read")
    
    args = parser.parse_args()
    
    # Process each file
    for file in args.files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split("\n")
            line_number = 1
            non_blank_line_number = 1
            
            for i, line in enumerate(lines):
                # Skip the final empty line that split() creates
                if i == len(lines) - 1 and line == "":
                    break
                
                prefix = ""
                
                if args.n:
                    # Number all lines
                    prefix = str(line_number).rjust(6) + "  "
                elif args.b and line != "":
                    # Number only non-blank lines
                    prefix = str(non_blank_line_number).rjust(6) + "  "
                
                print(prefix + line)
                
                line_number += 1
                if line != "":
                    non_blank_line_number += 1
                    
        except FileNotFoundError:
            print(f"Error reading {file}: No such file or directory", file=sys.stderr)
        except PermissionError:
            print(f"Error reading {file}: Permission denied", file=sys.stderr)
        except Exception as error:
            print(f"Error reading {file}: {error}", file=sys.stderr)

if __name__ == "__main__":
    main()