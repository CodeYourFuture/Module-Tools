import argparse
import sys

# def main():
parser = argparse.ArgumentParser(
        prog="Implment cat command",
        description="cat is used to display the content of a file."
    )
parser.add_argument('-n', action='store_true', help='number output lines')
parser.add_argument('-b', action='store_true', help='number non-empty output lines')
parser.add_argument('paths', nargs='+', help="The file path(s) to process")

args = parser.parse_args()

    
for path in args.paths:
    with open(path, 'r') as f:
        content= f.read()

    if args.b:
        line_num = 1
        lines_arr = []

        for line in content.split('\n'):
            if line.strip() == '':
                lines_arr.append(line) 
            else:
                lines_arr.append(f"{line_num:6} {line}")
                line_num += 1
        sys.stdout.write('\n'.join(lines_arr) + '\n')

    elif args.n:
        lines_arr = [
            f"{i+1:6} {line}"
            for i, line in enumerate(content.split('\n'))
        ]
        sys.stdout.write('\n'.join(lines_arr) + '\n')

    else:
        sys.stdout.write(content)
