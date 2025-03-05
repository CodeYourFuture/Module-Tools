import argparse

parser = argparse.ArgumentParser(
    prog="cat program implementation",
    description="Implements the cat program",
)

parser.add_argument("-n", "--number", help="The number for the line")
parser.add_argument("paths", nargs='+', help="The files to search")


args = parser.parse_args()

def read_and_print_file_content(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content
contents = map(read_and_print_file_content, args.paths)

for content in contents:
    if content is not None:
        print(content)
