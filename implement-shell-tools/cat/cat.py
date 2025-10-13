import glob
import argparse
from enum import Enum

class Numbering(Enum):
    NONE = 0
    ALL = 1
    NONEMPTY = 2

def cat(filepath, numbering=Numbering.NONE, line_counter=None):
    try:
        with open(filepath) as f:
            for line in f:
                if numbering == Numbering.NONEMPTY:
                    if line.strip():
                        print(f"{line_counter[0]:6}\t{line}", end='')
                        line_counter[0] += 1
                    else:
                        print(line, end='')
                elif numbering == Numbering.ALL:
                    print(f"{line_counter[0]:6}\t{line}", end='')
                    line_counter[0] += 1
                else:
                    print(line, end='')
    except FileNotFoundError:
        print(f"cat: {filepath}: No such file or directory")

def main():
    parser = argparse.ArgumentParser(description="Concatenate files and print on the standard output.")
    parser.add_argument('-n', action='store_true', help='number all output lines')
    parser.add_argument('-b', action='store_true', help='number non-empty output lines')
    parser.add_argument('files', nargs='+', help='files to concatenate')
    args = parser.parse_args()

    files = []
    for pattern in args.files:
        files.extend(glob.glob(pattern) or [pattern])

    line_counter = [1]

    # Determine numbering mode (mutually exclusive)
    if args.n and args.b:
        parser.error("options -n and -b are mutually exclusive")
    elif args.n:
        numbering = Numbering.ALL
    elif args.b:
        numbering = Numbering.NONEMPTY
    else:
        numbering = Numbering.NONE

    for file in sorted(files):
        cat(file, numbering=numbering, line_counter=line_counter)

if __name__ == "__main__":
    main()
