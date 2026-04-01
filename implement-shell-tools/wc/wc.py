import argparse
import glob

def count_file(filename):
    line_count = 0
    word_count = 0
    byte_count = 0

    try:
        with open(filename, "rb") as f:
            content = f.read()
            byte_count = len(content)
            text = content.decode("utf-8", errors="replace")
            lines = text.splitlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

        return (line_count, word_count, byte_count)
    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory")
        return None

def main():
    parser = argparse.ArgumentParser(description="Python version of wc")
    parser.add_argument("-l", action="store_true", help="Count lines")
    parser.add_argument("-w", action="store_true", help="Count words")
    parser.add_argument("-c", action="store_true", help="Count bytes")
    parser.add_argument("files", nargs="+", help="Files to read (supports wildcards)")
    args = parser.parse_args()

    # If no flag is given, show all
    show_lines = args.l
    show_words = args.w
    show_bytes = args.c
    if not (show_lines or show_words or show_bytes):
        show_lines = show_words = show_bytes = True

    file_list = []
    for pattern in args.files:
        matched = glob.glob(pattern)
        if matched:
            file_list.extend(matched)
        else:
            file_list.append(pattern)

    total_lines = total_words = total_bytes = 0
    for filename in file_list:
        result = count_file(filename)
        if result is None:
            continue
        lines, words, bytes_ = result
        total_lines += lines
        total_words += words
        total_bytes += bytes_

        output = []
        if show_lines:
            output.append(f"{lines:7}")
        if show_words:
            output.append(f"{words:7}")
        if show_bytes:
            output.append(f"{bytes_:7}")
        output.append(filename)
        print(" ".join(output))

    if len(file_list) > 1:
        output = []
        if show_lines:
            output.append(f"{total_lines:7}")
        if show_words:
            output.append(f"{total_words:7}")
        if show_bytes:
            output.append(f"{total_bytes:7}")
        output.append("total")
        print(" ".join(output))

if __name__ == "__main__":
    main()
