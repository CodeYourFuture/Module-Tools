import cowsay
import argparse

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things"
)

parser.add_argument("--animal", help="The animal to be saying things.")
parser.add_argument("message", nargs="+", help="The message to say.")

args = parser.parse_args()

# cowsay.cow(" ".join(sys.argv[1:]))


animals = cowsay.char_names

print(animals)