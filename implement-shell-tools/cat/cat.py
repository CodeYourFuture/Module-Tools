import argparse

parser = argparse.ArgumentParser(
    prog="cat program implementation",
    description="Implements the cat program",
)

parser.add_argument("-n", "--number", action="store_true", help="Number the output lines, starting at 1.")
parser.add_argument("path", help="The files to search")


args = parser.parse_args()
number_lines = args.number
print(args)
print(number_lines)


def read_and_print_file_content(file_path, number_lines):
    count = 0
    with open(file_path, 'r') as f:
        content = f.read()
    lines = content.split('\n')
    for line in lines:
        if number_lines:
            count+=1
            print(count, line)
        else:
            print(line)
        
        


read_and_print_file_content(args.path, number_lines)
# contents = map(read_and_print_file_content, args.paths)

# for content in contents:
#     if content is not None:
#         print(content)
