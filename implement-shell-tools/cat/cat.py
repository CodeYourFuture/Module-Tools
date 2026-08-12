import argparse
import glob

def main():
    parser = argparse.ArgumentParser(description="cat with -n and -b options")
    parser.add_argument("-n", action="store_true", help="Number all output lines")
    parser.add_argument("-b", action="store_true", help="Number non-blank lines (overrides -n)")
    parser.add_argument("files", nargs="+", help="Files to read (supports *.txt)")
    args = parser.parse_args()

    # -b overrides -n
    number_all = args.n
    number_nonblank = args.b
    if number_all and number_nonblank:
        number_all = False

    # Expand wildcard patterns (e.g. *.txt)
    file_list = []
    for pattern in args.files:
        matched_files = glob.glob(pattern)
        if matched_files:
            file_list.extend(matched_files)
        else:
            file_list.append(pattern)

    # Print contents of each file
    line_number = 1
    for filename in file_list:
        try:
            with open(filename, "r") as f:
                for line in f:
                    text = line.rstrip("\n")
                    if number_nonblank:
                        if text.strip():  # only number non-blank lines
                            print(f"{line_number:6}\t{text}")
                            line_number += 1
                        else:
                            print()
                    elif number_all:
                        print(f"{line_number:6}\t{text}")
                        line_number += 1
                    else:
                        print(text)
        except FileNotFoundError:
            print(f"cat: {filename}: No such file or directory")

if __name__ == "__main__":
    main()
