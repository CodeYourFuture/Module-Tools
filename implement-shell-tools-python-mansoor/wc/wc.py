import argparse

parser = argparse.ArgumentParser(
    prog ="wc",
    description ="my word, line and byte count",
)

parser.add_argument(
    "-l",
    "--lines",
    action="store_true",
    help="count lines"
)

parser.add_argument(
    "-w",
    "--words",
    action="store_true",
    help="count words",
)

parser.add_argument(
    "-c",
    "--bytes",
    action ="store_true",
    help="count bytes",
)

parser.add_argument(
    "files",
    nargs="+",
    help=" the files to process",
)

args = parser.parse_args()

if not args.lines and not args.words and not args.bytes:
    show_line = True
    show_words = True
    show_bytes = True
else:
    show_line = args.lines
    show_words = args.words
    show_bytes = args.bytes

total_lines = 0
total_words = 0
total_bytes = 0


for filename in args.files:
    try:
        with open(filename, "rb") as f:
            content = f.read()

        lines = content.count(b"\n")
        words = len(content.split())
        bytes_count = len(content)

        total_lines += lines
        total_words += words
        total_bytes += bytes_count

        output = []
        if show_line:
            output.append(str(lines))
        if show_words:
            output.append(str(words))
        if show_bytes:
            output.append(str(bytes_count))
        output.append(filename)
        print("\t".join(output))

    except OSError as error:
        print(f"{error.strerror}")

if len(args.files) > 1:
    total_output = []
    if show_line:
        total_output.append(str(total_lines))
    if show_words:
        total_output.append(str(total_words))
    if show_bytes:
        total_output.append(str(total_bytes))
    total_output.append("total")
    print("\t".join(total_output))