import argparse

parser = argparse.ArgumentParser(prog="cat", description="Prints the output of a file to the console")
parser.add_argument("-n", "--number", help="Displays the lines along with their number", action="store_true")
parser.add_argument("-b", "--nonblank", help="Displays the lines along with their number skipping the blank lines", action="store_true")
parser.add_argument("path", help="The file path", nargs="+")

args = parser.parse_args()

show_lines = args.number
non_blank = args.nonblank

text = ""
i = 1

for file in args.path:
    f = open(file)
    text += f.read()

text_list = text.split("\n")
text_list.pop(len(text_list) - 1)

if (show_lines == False and non_blank == False):
    print("\n".join(text_list))
    exit()

for line in text_list:
    if non_blank == True and line != "":
        print("     " + str(i) + " " + line)
        i += 1
    elif non_blank == False:
        print("     " + str(i) + " " + line)
        i += 1
    else:
        print("")