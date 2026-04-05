import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+")
parser.add_argument("-l", action="store_true", help="show line count")
parser.add_argument("-w", action="store_true", help="show word count")
parser.add_argument("-c", action="store_true", help="show byte count")

args = parser.parse_args()

show_lines = args.l
show_words = args.w
show_bytes = args.c

if not show_lines and not show_words and not show_bytes:
    show_lines = True
    show_words = True
    show_bytes = True

total_lines = 0
total_words = 0
total_bytes = 0

for file in args.files:
    try:
        f = open(file, "rb")
        content = f.read()
        f.close()

        line_count = content.count(b"\n")
        word_count = len(content.split())
        byte_count = len(content)

        total_lines += line_count
        total_words += word_count
        total_bytes += byte_count

        output = []

        if show_lines:
            output.append(str(line_count))
        if show_words:
            output.append(str(word_count))
        if show_bytes:
            output.append(str(byte_count))

        output.append(file)
        print(" ".join(output))

    except OSError:
        print("wc:", file, "not found")

if len(args.files) > 1:
    output = []

    if show_lines:
        output.append(str(total_lines))
    if show_words:
        output.append(str(total_words))
    if show_bytes:
        output.append(str(total_bytes))

    output.append("total")
    print(" ".join(output))