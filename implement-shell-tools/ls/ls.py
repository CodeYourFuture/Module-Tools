import argparse

parser = argparse.ArgumentParser(
    prog="py-ls",
    description="A Python implementation of the Unix ls command",
)

parser.add_argument("-1", action="store_true", help="List one file per line")
parser.add_argument("-a", "--all", action="store_true", help="Include directory entries whose names begin with a dot (.)")
parser.add_argument("path", nargs="+", help="The file path to process")

args = parser.parse_args()

