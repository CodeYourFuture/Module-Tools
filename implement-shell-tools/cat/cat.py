import sys

def cat(files, number_all=False, number_nonblank=False):
    line_number = 1
    for file in files:
        try:
            with open(file, 'r') as f:
                for line in f:
                    if number_nonblank:
                        if line.strip() != "":
                            print(f"{line_number}\t{line}", end='')
                            line_number += 1
                        else:
                            print(line, end='')
                    elif number_all:
                        print(f"{line_number}\t{line}", end='')
                        line_number += 1
                    else:
                        print(line, end='')
        except FileNotFoundError:
            print(f"cat: {file}: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    args = sys.argv[1:]
    number_all = False
    number_nonblank = False
    files = []

    for arg in args:
        if arg == '-n':
            number_all = True
        elif arg == '-b':
            number_nonblank = True
        else:
            files.append(arg)

    # -b overrides -n
    if number_nonblank:
        number_all = False

    cat(files, number_all, number_nonblank)
