import argparse
import cowsay

available_animals = cowsay.CHARS

parser = argparse.ArgumentParser(prog="cowsay", description="Make animals say things")
parser.add_argument("message", nargs="+", help="here is the message that the animal will say")
parser.add_argument(
    "--animal",
    choices=available_animals.keys(),
    default="cow",
    help="The animal to be saying things.",
)

args = parser.parse_args()

message_joined = " ".join(args.message)

animal = args.animal

getattr(cowsay, animal)(message_joined)