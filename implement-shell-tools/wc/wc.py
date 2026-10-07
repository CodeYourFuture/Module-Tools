import argparse

# Set up command-line argument parser
parser = argparse.ArgumentParser()

# Add supported flags
parser.add_argument("-l", action="store_true")
parser.add_argument("-w", action="store_true")
parser.add_argument("-c", action="store_true")

# Accept one or more file paths
parser.add_argument("paths", nargs="+")

# Parse the user's command-line arguments
args = parser.parse_args()

flags = []

# Store selected flags for the existing logic
if args.l:
    flags.append("-l")

if args.w:
    flags.append("-w")

if args.c:
    flags.append("-c")

paths = args.paths


# Build the output based on the selected flags
def get_output(lines, words, chars, flags):
    output = []

    # Show all counts when no flag is provided
    if len(flags) == 0:
        output = [lines, words, chars]

    else:
        if "-l" in flags:
            output.append(lines)

        if "-w" in flags:
            output.append(words)

        if "-c" in flags:
            output.append(chars)

    return output


total_lines = 0
total_words = 0
total_chars = 0


# Process each file
for file in paths:

    # Read file as bytes
    with open(file, "rb") as f:
        content = f.read()

    # Count lines, words, and characters
    lines = content.count(b"\n")
    words = len(content.split())
    chars = len(content)

    # Create and print output for this file
    output = get_output(lines, words, chars, flags)

    # Print counts with aligned columns
    print(" ".join(f"{value:3}" for value in output), file)

    # Add this file's counts to the totals
    total_lines += lines
    total_words += words
    total_chars += chars


# Print total only when multiple files are provided
if len(paths) > 1:
    total_output = get_output(total_lines, total_words, total_chars, flags)

    # Print aligned total
    print(" ".join(f"{value:3}" for value in total_output), "total")
