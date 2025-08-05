import argparse

def wc(path, count_lines, count_words, count_bytes):
    try:
        with open(path, 'r') as f:
            content = f.read()
        lines = content.splitlines()
        words = content.split()
        bytes_ = len(content.encode('utf-8'))

        parts = []
        if count_lines: parts.append(str(len(lines)))
        if count_words: parts.append(str(len(words)))
        if count_bytes: parts.append(str(bytes_))

        if not parts:
            parts = [str(len(lines)), str(len(words)), str(bytes_)]
        print(' '.join(parts), path)

    except FileNotFoundError:
        print(f"wc: {path}: No such file or directory")
    except IsADirectoryError:
        print(f"wc: {path}: Is a directory")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', action='store_true', help='Count lines')
    parser.add_argument('-w', action='store_true', help='Count words')
    parser.add_argument('-c', action='store_true', help='Count bytes')
    parser.add_argument('paths', nargs='+', help='Files to count')
    args = parser.parse_args()

    for path in args.paths:
        wc(path, args.l, args.w, args.c)

if __name__ == "__main__":
    main()