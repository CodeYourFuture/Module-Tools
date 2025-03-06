
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

def extract_words(content):
    return content.split(' ')

def extract_chars(content):
    return list(content)

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def output_lines_words_chars_number():
    content = read_file_content(args.path)
    lines = extract_lines(content)
    words = extract_words(content)
    chars = extract_chars(content)
    print(len(lines), len(words), len(chars), args.path)

output_lines_words_chars_number()