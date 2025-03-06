
import argparse


parser = argparse.ArgumentParser(
    prog="wc program",
    description="Implements the cat program"
)

parser.add_argument("paths", nargs='+', type=str, help="The path to process")

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


def get_lines_words_chars_count(file_path):
    content = read_file_content(file_path)
    lines = extract_lines(content)
    words = extract_words(content)
    chars = extract_chars(content)
    return  [len(lines), len(words), len(chars)]


def output_lines_words_chars_count(file_path):
    lines_words_chars_count = get_lines_words_chars_count(file_path)
    lines_count = lines_words_chars_count[0]
    words_count = lines_words_chars_count[1]
    chars_count = lines_words_chars_count[2]
    print(lines_count, words_count, chars_count, args.paths[0])

lines_words_chars_count = []
if len(args.paths) == 1:
    output_lines_words_chars_count(args.paths[0])
else:
    for file_path in args.paths:
        result = get_lines_words_chars_count(file_path)
        lines_words_chars_count.append(result)

#print(lines_words_chars_count)