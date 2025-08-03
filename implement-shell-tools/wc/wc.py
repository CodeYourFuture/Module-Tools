import os
import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="Counts words in a file that contain a particular character",
)

parser.add_argument("-l",action='store_true', help="The number of lines in each input file is written to the standard output.")
parser.add_argument("-w", action='store_true', help="The number of words in each input file is written to the standard output.")
parser.add_argument("-c", action='store_true', help="The number of bytes in each input file is written to the standard output.")
parser.add_argument("path", nargs="+", help="The path to search")

args = parser.parse_args()

if (not args.w and not args.c and not args.l) :
    args.w = args.c = args.l = True
total = []
for path in args.path:
    output = []
    if args.l or args.w:
        with open(path) as file:
            lines = file.readlines()
            # lines count
            if args.l:
                num_lines = len(lines)
                output.append(num_lines)
            # word count
            if args.w:
                word_count = 0
                for line in lines:   
                    lin = line.rstrip()
                    wds = lin.split()
                    word_count += len(wds)

                output.append(word_count)


    if args.c:
        file_size = os.path.getsize(path)
        output.append(file_size)

    if len(args.path) > 1:
        total.append(output.copy())
    output.append(path)
    string_list = map(str, output)
    print("       ".join(string_list))
if len(args.path) > 1:
    result = [sum(i) for i in zip(*total)]
    string_result_list = map(str, result)
    print("       ".join(string_result_list), "     total")


    