import argparse
import re

def format_number(number_array):
    return [str(number).rjust(4) for number in number_array]

parser = argparse.ArgumentParser(
    prog="custom wc in python",
    description="trying to match behaviour in the actual wc"
)

parser.add_argument("-l", "--lines", action="store_true", help="count how many lines")
parser.add_argument("-w", "--words", action="store_true", help="count how many words")
parser.add_argument("-c", "--characters", action="store_true", help="count how many characters")
parser.add_argument("path", nargs="+", help="path to process")

args = parser.parse_args()

files_array = args.path

total_lines = 0
total_words = 0
total_characters = 0

numbers_row_array = []

for file_path in files_array:
    with open(file_path) as file:
        context = file.read()
        lines  = len(context.split("\n")) - 1
        words = len(re.findall(r"\S+", context))
        characters = len(context)

        if (args.lines):
            numbers_row_array.append(lines)
        if (args.words):
            numbers_row_array.append(words)
        if (args.characters):
            numbers_row_array.append(characters)
        
        if (len(numbers_row_array) > 0):
            print(numbers_row_array)
        else:
            print(lines, words, characters, file_path)
        total_lines += lines
        total_words += words
        total_characters += characters

if (len(files_array) > 1):
    print(total_lines, total_words, total_characters, 'total')