import argparse


def run(args):
    for file_path in args.path:
        counter_number = 1

        with open(file_path, "r") as f:
            lines = f.readlines()

        if args.b:
            for line in lines:
                if line.strip() != "":
                    print(counter_number, line, end="")
                    counter_number += 1
                else:
                    print(line, end="")

        elif args.n:
            for line in lines:
                print(counter_number, line, end="")
                counter_number += 1

        else:
            for line in lines:
                print(line, end="")


def main():
    parser = argparse.ArgumentParser(
        prog="my-cat",
        description="Simple cat clone with -n and -b options",
    )

    parser.add_argument("-n", action="store_true", help="number all lines")
    parser.add_argument("-b", action="store_true", help="The character to search for")
    parser.add_argument("path", nargs="+", help="The file to search")

    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
