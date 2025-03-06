
import argparse


parser = argparse.ArgumentParser(
    prog="wc program",
    description="Implements the cat program"
)

parser.add_argument("path", type=str, help="The path to process")

args = parser.parse_args()


def extract_lines(content):
    return content.split('\n')


def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
        lines = extract_lines(content)
    return lines

lines = read_file_content(args.path)
print(lines)