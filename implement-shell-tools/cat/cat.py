import argparse
import glob

# create argument parser
parser = argparse.ArgumentParser(description="Simple cat tool")

parser.add_argument("files", nargs="+", help="files to read")
parser.add_argument("-n", action="store_true", help="number all lines")
parser.add_argument("-b", action="store_true", help="number non-empty lines")

args = parser.parse_args()

# if -b is used, ignore -n
if args.b:
    args.n = False

line_number = 1


# expand *.txt into real file names
def get_files(file_patterns):
    files = []
    for pattern in file_patterns:
        matched = glob.glob(pattern)

        if matched:
            files.extend(matched)
        else:
            files.append(pattern)

    return files


def print_file(file_name):
    global line_number

    try:
        with open(file_name, "r") as f:
            for line in f:

                # -b → number only non-empty lines
                if args.b:
                    if line.strip():   # not empty
                        print(f"{line_number}\t{line}", end="")
                        line_number += 1
                    else:
                        print(line, end="")

                # -n → number all lines
                elif args.n:
                    print(f"{line_number}\t{line}", end="")
                    line_number += 1

                # no flags
                else:
                    print(line, end="")

    except FileNotFoundError:
        print(f"Error: {file_name} not found")


# main program
files = get_files(args.files)

for file in files:
    print_file(file)