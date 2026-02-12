import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="Implment wc command",
        description="Count lines, words, and characters in text files."
    )

    parser.add_argument("paths", nargs='+', type=str, help="The path to process")
    parser.add_argument('-l', action="store_true", help='Ouput number of lines')
    parser.add_argument('-w', action="store_true", help='Ouput number of words')
    parser.add_argument('-c', action="store_true", help='Ouput number of characters')
    return parser.parse_args()

    
def wc(path):
    with open(path, 'r') as f:
        content= f.read()

    line_count = content.count('\n')
    word_count = len(content.split())
    char_count = len(content)
    return line_count, word_count, char_count

    
def format_output(path, counts, args):
    line_count, word_count, char_count = counts
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
    return(" ".join(file_output))


def main():
    args = parse_arguments()
    total_lines = total_words = total_chars = 0
    output_lines =[]

    for path in args.paths:
        line_count, word_count, char_count = wc(path)
        total_lines += line_count
        total_words += word_count
        total_chars += char_count
        output_lines.append(format_output(path, (line_count, word_count, char_count), args))
    
    print("\n".join(output_lines))

    if len(args.paths) > 1:
        output_total =[]
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
   

if __name__ == "__main__":
        main()