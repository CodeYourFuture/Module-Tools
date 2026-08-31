import argparse
import os

parser = argparse.ArgumentParser(prog="wc",
                                 description="simple wc clone")

parser.add_argument("-w",
                    "--words",
                    dest="show_words",
                    action="store_true",
                    help="print word count")

parser.add_argument("-l",
                    "--lines",
                    dest="show_lines",
                    action="store_true",
                    help="print line count")

parser.add_argument("-c",
                    "--bytes",
                    dest="show_bytes",
                    action="store_true",
                    help="print byte count")

parser.add_argument("paths", nargs="+")

args = parser.parse_args()

if not args.show_lines and not args.show_words and not args.show_bytes:
    args.show_lines = True
    args.show_words = True
    args.show_bytes = True

def format_count(content, path):
    outputs = []

    word_count = str(len(content.split()))
    line_count = str(content.count(b"\n"))
    byte_count = str(len(content))

    if args.show_lines:
        outputs.append(line_count)

    if args.show_words:
        outputs.append(word_count)

    if args.show_bytes:
        outputs.append(byte_count)

    outputs.append(path)

    return "\t".join(outputs)

outputs = []

for path in args.paths:
    if os.path.isdir(path):
            print(f"wc: {path}: Is a directory")
            continue
        
    with open(path, "rb") as file:
        content = file.read()
        output = format_count(content, path)
        outputs.append("\t" + output)

result = "\n".join(outputs)
print(result)
