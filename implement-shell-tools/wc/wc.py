import sys

args = sys.argv[1:]

show_lines = "-l" in args
show_words = "-w" in args
show_bytes = "-c" in args

files = [arg for arg in args if not arg.startswith("-")]

def get_stats(text):
    return {
        "lines": text.count("\n"),
        "words": len(text.split()),
        "bytes": len(text.encode("utf-8"))
    }

def format_num(num):
    return str(num).rjust(8)

total_lines = 0
total_words = 0
total_bytes = 0

for file in files:
    with open(file, "r") as f:
        content = f.read()

    stats = get_stats(content)

    total_lines += stats["lines"]
    total_words += stats["words"]
    total_bytes += stats["bytes"]

    output = []

    if show_lines:
        output.append(format_num(stats["lines"]))
    elif show_words:
        output.append(format_num(stats["words"]))
    elif show_bytes:
        output.append(format_num(stats["bytes"]))
    else:
        output.extend([
            format_num(stats["lines"]),
            format_num(stats["words"]),
            format_num(stats["bytes"])
        ])

    output.append(file)

    print(" ".join(output))

if len(files) > 1:
    output = []

    if show_lines:
        output.append(format_num(total_lines))
    elif show_words:
        output.append(format_num(total_words))
    elif show_bytes:
        output.append(format_num(total_bytes))
    else:
        output.extend([
            format_num(total_lines),
            format_num(total_words),
            format_num(total_bytes)
        ])

    output.append("total")

    print(" ".join(output))
