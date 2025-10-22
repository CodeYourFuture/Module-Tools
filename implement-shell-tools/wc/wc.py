import argparse


parser = argparse.ArgumentParser(
    prog="Implment wc command",
    description="Count lines, words, and characters in text files."
)

parser.add_argument("paths", nargs='+', type=str, help="The path to process")
parser.add_argument('-l', action="store_true", help='Ouput number of lines')
parser.add_argument('-w', action="store_true", help='Ouput number of words')
parser.add_argument('-c', action="store_true", help='Ouput number of characters')

args = parser.parse_args()
is_lines_option = args.l
is_words_option = args.w
is_chars_option = args.c
output_list = []
output_total=[]
total_lines = 0
total_words = 0
total_chars = 0
    
for path in args.paths:
    with open(path, 'r') as f:
        content= f.read()

    line_count = content.count('\n')
    word_count = len(content.split())
    char_count = len(content)
    
    total_lines += line_count
    total_words += word_count
    total_chars += char_count

    file_output = []

    if not (args.l or args.w or args.c):
        file_output = [str(line_count), str(word_count), str(char_count)]
    else:
        if args.l:
            file_output.append(str(line_count))
        if args.w:
            file_output.append(str(word_count))
        if args.c:
            file_output.append(str(char_count))

    file_output.append(path)
    output_list.append(" ".join(file_output))

print("\n".join(output_list))



if len(args.paths) > 1:
    if not (args.l or args.w or args.c):
        output_total = [str(total_lines), str(total_words), str(total_chars)]

    else:
        if args.l:
            output_total.append(str(total_lines))
        if args.w:
            output_total.append(str(total_words))
        if args.c:
            output_total.append(str(total_chars))
        
    output_total.append("total")
    print(" ".join(output_total))
   