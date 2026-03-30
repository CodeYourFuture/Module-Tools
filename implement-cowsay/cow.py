import argparse
import cowsay

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things"
)

parser.add_argument(
    "--animal",
    choices=cowsay.char_names,
    default="cow",
    help="The animal to be saying things."
)

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say."
)

args = parser.parse_args()

message = " ".join(args.message)
animal_func = getattr(cowsay, args.animal)
animal_func(message)