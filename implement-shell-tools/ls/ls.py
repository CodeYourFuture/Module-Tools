
import sys

args = sys.argv[1:]


def read_and_print_file_content():
    with open(args[0], 'r') as f: 
        content = f.read()
    print(content)

read_and_print_file_content()