import argparse

parser = argparse.ArgumentParser(
    prog="py-cat",
    description="A Python implementation of the Unix cat command",
)

parser.add_argument("-n", "--number", help="Number all output lines")
parser.add_argument("-b", "--numberNonBlank", help="Numbers only non-empty lines. Overrides -n option")
parser.add_argument("path", nargs="+", help="The file path to process")

args = parser.parse_args()

    