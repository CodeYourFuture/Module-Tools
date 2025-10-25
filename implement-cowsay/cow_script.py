import cowsay
import argparse

animals = [a for a in dir(cowsay) if callable(getattr(cowsay, a)) and not a.startswith("_")]

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things"
)

parser.add_argument(
    "--animal",
    choices=animals,
    help="The animal to be saying things."
)

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say."
)

args = parser.parse_args()
message_to_say = " ".join(args.message)

if args.animal:
    getattr(cowsay, args.animal)(message_to_say)
else:
    cowsay.cow(message_to_say)
