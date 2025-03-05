import sys

args = sys.argv[1:]

def read_and_print_file_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content
contents = map(read_and_print_file_content, args)

for content in contents:
    if content is not None:
        print(content)