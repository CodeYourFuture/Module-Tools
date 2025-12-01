import argparse

parser = argparse.ArgumentParser(
    prog="py-wc",
    description="A Python implementation of the Unix wc command",
)

parser.add_argument("-l", "--lines", help="Print the newline counts")
parser.add_argument("-w", "--words", action="store_true", help="Print the word counts")
parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte counts")
parser.add_argument("path", nargs="?", default=".", help="Directory to list")

args = parser.parse_args()

