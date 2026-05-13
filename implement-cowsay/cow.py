import argparse
import cowsay

available_animals = cowsay.CHARS

parser = argparse.ArgumentParser(prog="cowsay")
parser.add_argument("message", nargs="+", help="What the animal will say")
parser.add_argument(
    "--animal",
    choices=available_animals.keys(),
    default="cow",
    help="The animal that will say the word",
)

args = parser.parse_args()

message_joined = " ".join(args.message)

animal = args.animal

getattr(cowsay, animal)(message_joined)
