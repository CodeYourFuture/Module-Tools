import sys
def count_file(filename):
    try:
        with open (filename, 'r', encoding='utf-8') as f:
            content =f.read()

            lines = content.splitlines()
            words = content.split()
            characters = content

            print(f"{len(lines)} {len(words)} {len(characters)} {filename}")
    except FileNotFoundError:
        print(f"wc:{filename}: no such file or directory")


if __name__ == "__main__":
    args = sys.argv[1:]
    for file in args:
        count_file(file)