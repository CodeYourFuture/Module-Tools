import argparse
import sys

def read_files(paths):
    lines = []
    for path in paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines.extend(f.read().splitlines())
        except OSError as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
            sys.exit(1)
    return lines
 
def main():
    parser = argparse.ArgumentParser(
        prog="display-content-of-a-file",
        description="cat is used to display the content of a file or print the content of a file."
    )
    parser.add_argument('-n', action='store_true', help='number output lines')
    parser.add_argument('-b', action='store_true', help='number non-empty output lines')
    parser.add_argument('paths', nargs='+', help="The file path(s) to process")

    options = parser.parse_args()

    combined_data = ""
    for path in options.paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                combined_data += f.read() + "\n"
        except Exception as e:
            print(f"Error reading {path}: {e}", file=sys.stderr)
            sys.exit(1)

    # If user used -b
    if options.b:
        line_num = 1
        numbered_lines = []
        for line in combined_data.split('\n'):
            if line.strip() == '':
                numbered_lines.append(line)  # Keep empty lines unnumbered
            else:
                numbered_lines.append(f"{line_num:6} {line}")
                line_num += 1
        sys.stdout.write('\n'.join(numbered_lines) + '\n')

    # If user used -n
    elif options.n:
        numbered_lines = [
            f"{i+1:6} {line}"
            for i, line in enumerate(combined_data.split('\n'))
        ]
        sys.stdout.write('\n'.join(numbered_lines) + '\n')

    # If user didn't use -n or -b
    else:
        sys.stdout.write(combined_data)

if __name__ == "__main__":
    main()










#python3 cat.py -b sample-files/*  