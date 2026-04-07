import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="wc implementation",
)

parser.add_argument("paths", nargs="+", help="The file to process")
parser.add_argument("-l", action="store_true", help="count lines")
parser.add_argument("-w", action="store_true", help="count words")
parser.add_argument("-c", action="store_true", help="count characters")
args = parser.parse_args()

total = {
    "lines_counter": 0,
    "words_counter": 0,
    "characters_counter": 0,
}
for path in args.paths:

    with open(path, "r") as f:
        content = f.read()

    line_counter = len(content.split("\n")) - 1
    words_counter = len(content.split())
    characters_counter = len(content)
    if not args.l and not args.w and not args.c:
        print(f"{line_counter}  {words_counter}  {characters_counter} {path}")
        total["lines_counter"] += line_counter
        total["words_counter"] += words_counter
        total["characters_counter"] += characters_counter
    else:
        results = []
        if args.l:
            results.append(line_counter)
            total["lines_counter"] += line_counter
        if args.w:
            results.append(words_counter)
            total["words_counter"] += words_counter
        if args.c:
            results.append(characters_counter)
            total["characters_counter"] += characters_counter
        results = " ".join(map(str, results))
        print(results, path)

if len(args.paths) > 1:
    if not args.l and not args.w and not args.c:
        print(
            f"{total['lines_counter']}  {total['words_counter']}  {total['characters_counter']} total"
        )

    else:
        total_with_flags = []

        if args.l:
            total_with_flags.append(total["lines_counter"])
        if args.w:
            total_with_flags.append(total["words_counter"])
        if args.c:
            total_with_flags.append(total["characters_counter"])
        print(" ".join(map(str, total_with_flags))," total")
      
