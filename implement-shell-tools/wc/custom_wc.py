import argparse
import re

def format_number(number_array):
    space_array = [3, 4, 4]
    result = map(lambda number, space: str(number).rjust(space), number_array, space_array)
    return "".join(list(result))

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

total_numbers_row_array = []

for file_path in files_array:
    with open(file_path) as file:
        context = file.read()
        lines  = len(context.split("\n")) - 1
        words = len(re.findall(r"\S+", context))
        characters = len(context)

        numbers_row_array = []
        if (args.lines):
            numbers_row_array.append(lines)
        if (args.words):
            numbers_row_array.append(words)
        if (args.characters):
            numbers_row_array.append(characters)

        if (len(numbers_row_array) == 1 and len(files_array) == 1):
            print(f'{numbers_row_array[0]} {file_path}')
        
        elif (len(numbers_row_array) > 0):
            print(f'{format_number(numbers_row_array)} {file_path}')
        else:
            print(format_number([lines, words, characters]), file_path)

        total_lines += lines
        total_words += words
        total_characters += characters

if (len(files_array) > 1):
    if (args.lines):
        total_numbers_row_array.append(total_lines)
    if (args.words):
        total_numbers_row_array.append(total_words)
    if (args.characters):
        total_numbers_row_array.append(total_characters)
    if (len(total_numbers_row_array) > 0):
        print(f'{format_number(total_numbers_row_array)} total')
    else:
        print(format_number([total_lines, total_words, total_characters]), 'total')