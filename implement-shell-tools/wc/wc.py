
import argparse


parser = argparse.ArgumentParser(
    prog="wc program",
    description="Implements the cat program"
)

parser.add_argument("path", type=str, help="The path to process")

args = parser.parse_args()


def extract_lines(content):
    lines = content.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    return lines


def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
        lines = extract_lines(content)
    return lines

def number_of_lines(lines):
    return len(lines)


def output_lines_words_chars_number():
    lines = read_file_content(args.path)
    print(len(lines), args.path)

output_lines_words_chars_number()