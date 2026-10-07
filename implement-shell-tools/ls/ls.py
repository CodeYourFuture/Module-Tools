import argparse
import os

# Set up command-line argument parser
parser = argparse.ArgumentParser()

# Add supported flags and file/directory paths
parser.add_argument("-a", action="store_true")
parser.add_argument("-1", dest="one", action="store_true")
parser.add_argument("paths", nargs="*")

# Parse the user's command-line arguments
args = parser.parse_args()

flags = []

if args.a:
    flags.append("-a")

if args.one:
    flags.append("-1")

paths = args.paths


# Use the current directory if no path is provided
if not paths:
    paths = ["."]


# Process each path
for path in paths:

    # If the path is a file, print its name
    if os.path.isfile(path):
        print(path)

    # If the path is a directory, get its contents
    elif os.path.isdir(path):
        contents = os.listdir(path)
        if "-a" not in flags:
            contents = [file for file in contents if not file.startswith(".")]
        if "-1" in flags:
            print("\n".join(contents))
        else:
            print(" ".join(contents))
    # Handle invalid paths
    else:
        print(f"No such file or directory: {path}")
