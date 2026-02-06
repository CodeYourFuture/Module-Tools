import sys

def cat_file(filename, flag):
    try:
        with open(filename, 'r') as file:
            if not flag:
                for line in file:
                    print(line, end="")

            elif flag == "-n":
                for index, line in enumerate(file, start=1):
                    print(f"{index:6}\t{line}", end="")

            elif flag == "-b":
                line_number = 1
                for line in file:
                    if line.strip() == "":
                        print(line, end="")
                    else:
                        print(f"{line_number:6}\t{line}", end="")
                        line_number += 1

    except FileNotFoundError:
        print(f"cat: {filename}: No such file or directory", file=sys.stderr)
    
def main():
    args = sys.argv[1:]

    flag = False 
    
    if "-n" in args:
        flag = "-n"
        args.remove("-n")
    elif "-b" in args:
        flag = "-b"
        args.remove("-b")

    for filename in args:
        cat_file(filename, flag)

if __name__ == "__main__":
    main()