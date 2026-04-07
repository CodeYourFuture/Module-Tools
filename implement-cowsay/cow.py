import cowsay
import argparse

# get valid animals dynamically from the library
animals = [
    name for name in dir(cowsay)
    if name.islower() and callable(getattr(cowsay, name))
]

parser = argparse.ArgumentParser(description="Make animals say things")

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say."
)

parser.add_argument(
    "--animal",
    choices=animals,
    default="cow",
    help="The animal to be saying things."
)

args = parser.parse_args()

message = " ".join(args.message)

getattr(cowsay, args.animal)(message)