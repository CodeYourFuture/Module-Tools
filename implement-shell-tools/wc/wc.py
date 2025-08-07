import argparse

def count_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.count("\n")
            words = len(content.split())
            bytes_ = len(content.encode("utf-8"))
            return lines, words, bytes_
    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory")
        return 0, 0, 0

def main():
    parser = argparse.ArgumentParser(description="Python version of wc")
    parser.add_argument("files", nargs="+", help="Files to count")
    args = parser.parse_args()

    for filename in args.files:
        lines, words, bytes_ = count_file(filename)
        print(f"{lines:7} {words:7} {bytes_:7} {filename}")

if __name__ == "__main__":
    main()
