#!/usr/bin/env python3
import argparse
import sys

def count_stats(text):
    """Count lines, words, and bytes in text"""
    lines = text.split("\n")
    line_count = len(lines) - 1
    
    # Count words (split by whitespace, filter out empty strings)
    words = text.strip().split()
    word_count = len([word for word in words if word])
    
    # Count bytes (UTF-8 encoding)
    byte_count = len(text.encode("utf-8"))
    
    return {
        "lines": line_count,
        "words": word_count,
        "bytes": byte_count
    }

def format_output(stats, filename, options):
    """Format output line based on options"""
    output = ""
    show_all = not (options.l or options.w or options.c)
    
    if options.l or show_all:
        output += str(stats["lines"]).rjust(7)
    if options.w or show_all:
        output += str(stats["words"]).rjust(7)
    if options.c or show_all:
        output += str(stats["bytes"]).rjust(7)
    
    return output + " " + filename

def main():
    # Set up command options
    parser = argparse.ArgumentParser(
        prog="wc",
        description="Word, line, and byte count"
    )
    parser.add_argument("-l", action="store_true", help="Print the newline counts")
    parser.add_argument("-w", action="store_true", help="Print the word counts")
    parser.add_argument("-c", action="store_true", help="Print the byte counts")
    parser.add_argument("files", nargs="+", help="Files to read")
    
    args = parser.parse_args()
    
    # Initialize totals
    total = {"lines": 0, "words": 0, "bytes": 0}
    
    # Process each file
    for file in args.files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()
            
            stats = count_stats(text)
            
            # Add to totals
            total["lines"] += stats["lines"]
            total["words"] += stats["words"]
            total["bytes"] += stats["bytes"]
            
            # Print stats for this file
            print(format_output(stats, file, args))
            
        except FileNotFoundError:
            print(f"wc: {file}: No such file or directory", file=sys.stderr)
        except PermissionError:
            print(f"wc: {file}: Permission denied", file=sys.stderr)
        except Exception as error:
            print(f"wc: {file}: {error}", file=sys.stderr)
    
    # Print totals if multiple files
    if len(args.files) > 1:
        print(format_output(total, "total", args))

if __name__ == "__main__":
    main()