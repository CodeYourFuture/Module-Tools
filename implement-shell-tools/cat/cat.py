import argparse

def main():
    parser = argparse.ArgumentParser(description="cat with -n option")
    parser.add_argument("-n", action="store_true", help="number all output lines")
    parser.add_argument("files", nargs="+", help="Files to read")
    args = parser.parse_args()

    line_number = 1
    for filename in args.files:
        try:
            with open(filename, "r") as f:
                for line in f:
                    # Remove trailing newline for formatting
                    line_to_print = line.rstrip('\n')
                    if args.n:
                        print(f"{line_number:6}\t{line_to_print}")
                        line_number += 1
                    else:
                        print(line, end="")
        except FileNotFoundError:
            print(f"cat: {filename}: No such file or directory")

if __name__ == "__main__":
    main()
