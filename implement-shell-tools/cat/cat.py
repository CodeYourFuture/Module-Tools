import argparse

def main():
    parser = argparse.ArgumentParser(description="Basic cat command")
    parser.add_argument("files", nargs="+", help="Files to read")
    args = parser.parse_args()

    for filename in args.files:
        try:
            with open(filename, "r") as f:
                for line in f:
                    print(line, end="")
        except FileNotFoundError:
            print(f"my_cat: {filename}: No such file or directory")

if __name__ == "__main__":
    main()