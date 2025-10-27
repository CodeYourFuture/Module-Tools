import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        prog="Implement ls command in Python",
        description="List files in a directory"
        )
    parser.add_argument("paths", nargs='+', help="Path(s) to process")
    parser.add_argument("-a", action="store_true", help="Display all files include hidden files")
    parser.add_argument("-1", action="store_true", help="list one file per line")
    parser.add_argument("dir", nargs="?", default=".", help="Directory to list, default curent directory")

    args = parser.parse_args()

    
    total_lines = total_words = total_chars = 0
    outputs = []

    for path in args.paths:
        line_count, word_count, char_count = wc(path)
        total_lines += line_count
        total_words += word_count
        total_chars += char_count
        outputs.append(format_output((line_count, word_count, char_count), path, args))

    print("\n".join(outputs))

    # Print totals if multiple files
    if len(args.paths) > 1:
        totals = []
        if not (args.l or args.w or args.c):
            totals = [str(total_lines), str(total_words), str(total_chars)]
        else:
            if args.l:
                totals.append(str(total_lines))
            if args.w:
                totals.append(str(total_words))
            if args.c:
                totals.append(str(total_chars))
        totals.append("total")
        print(" ".join(totals))

def wc(path):
    """Return (line_count, word_count, char_count) for the given file."""
    with open(path, 'r') as f:
        content = f.read()
    line_count = content.count('\n')
    word_count = len(content.split())
    char_count = len(content)
    return line_count, word_count, char_count


def format_output(counts, path, args):
    """Format output for a single file based on provided flags."""
    line_count, word_count, char_count = counts
    parts = []

    if not (args.l or args.w or args.c):
        parts = [str(line_count), str(word_count), str(char_count)]
    else:
        if args.l:
            parts.append(str(line_count))
        if args.w:
            parts.append(str(word_count))
        if args.c:
            parts.append(str(char_count))

    parts.append(path)
    return " ".join(parts)

if __name__ == "__main__":
    main()