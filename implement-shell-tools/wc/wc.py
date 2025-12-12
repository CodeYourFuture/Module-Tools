import argparse
import sys
import re


def main():
    # --------------------------------------------------------
    #  Set up argparse
    # --------------------------------------------------------
    parser= argparse.ArgumentParser(
        prog="wc",
        description ="wc command implementation in python"
    )

    parser.add_argument("-l", action="store_true", help ="show number of lines only")
    parser.add_argument("-w", action="store_true", help="show number of words only")
    parser.add_argument("-c", action="store_true", help="show number of characters only")

    parser.add_argument("paths", nargs="*", help="file paths to process")

    args = parser.parse_args()

    # --------------------------------------------------------
    #  Ensures at least one path exists
    # --------------------------------------------------------
    if len(args.paths) == 0:
        print("wc: no file specified", file=sys.stderr)
        sys.exit(1)

    totals= {"lines": 0, "words": 0, "chars": 0}

    # --------------------------------------------------------
    #  Loop over each file path and process it
    # --------------------------------------------------------
    for file_path in args.paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError as err:
            print(f"wc: cannot read file'{file_path}': {err}", file=sys.stderr)
            continue

        # --------------------------------------------------------
        #  Count values
        # --------------------------------------------------------
        line_count = len(content.split("\n"))

        words = [w for w in re.split(r"\s+", content) if w]
        word_count = len(words)

        char_count = len(content)

        totals["lines"] += line_count
        totals["words"] += word_count
        totals["chars"] +=char_count

        # --------------------------------------------------------
        #  Decide what to print based on flags
        # --------------------------------------------------------
        no_flags = not args.l and not args.w and not args.c

        if no_flags:
            print(f"{line_count} {word_count} {char_count} {file_path}")
            continue

        if args.l:
            print(f"{line_count} {file_path}" )

        if args.w:
            print(f"{word_count} {file_path}")

        if args.c:
            print(f"{char_count} {file_path}")


    # --------------------------------------------------------
    #  Print totals if there are multiple files
    # --------------------------------------------------------
    if len(args.paths) > 1:
        no_flags = not args.l and not args.w and not args.c

        if no_flags:
            print(f"{totals['lines']} {totals['words']} {totals['chars']} total")

        if args.l:
            print(f"{totals['lines']} total")
        if args.w:
            print(f"{totals['words']} total")
        if args.c:
            print(f"{totals['chars']} total")

if __name__ == "__main__":
    main()
