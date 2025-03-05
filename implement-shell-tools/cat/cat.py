import sys

args = sys.argv[1:]

def read_and_print_file_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    print(content)

contents = map(read_and_print_file_content, args)
print(list(contents))