import cowsay
import argparse

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things",
)

valid_animal = cowsay.char_names

parser.add_argument(
    "--animal",
    choices=valid_animal,
    default="cow",
    help=" The animal to be saying things."
)
parser.add_argument(
    "message", 
    nargs="+", 
    help="The message to say"
)

args = parser.parse_args()

# to compose full msg
message = " ".join(args.message)

# Call selected cowsay func
getattr(cowsay, args.animal)(message)
