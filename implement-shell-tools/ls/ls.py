import argparse  #for parsing command-line arguments and options
import os        #to interact with the os for listing files and handling paths
import sys       #Allows interaction with the Py runtime env like reading/writing output,exiting.


def list_directory(directory, show_all, one_per_line):
    try:
        files = os.listdir(directory)
    except Exception as e:
        print(f"ls: cannot access '{directory}': {e}", file=sys.stderr)
        return 1

    if not show_all:
        files = [f for f in files if not f.startswith('.')]
    files.sort()

    if one_per_line:
        for file in files:
            print(file)
    else:
        print(' '.join(files))

    return 0

def main():
    parser = argparse.ArgumentParser(description="A simplified ls implementation.")
    parser.add_argument('-1', dest='one_per_line', action='store_true', help='list one file per line')
    parser.add_argument('-a', action='store_true', help='include hidden files')
    parser.add_argument('directory', nargs='?', default='.', help='directory to list (default: current directory)')

    args = parser.parse_args()

    exit_code = list_directory(args.directory, args.a, args.one_per_line)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
