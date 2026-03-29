import argparse
import cowsay
import sys

available_animals = cowsay.char_names

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Uses the cowsay library to show user-supplied text, as said by a specified animal",
)

parser.add_argument("--animal", help="The animal to be saying things", default="cow", choices=available_animals)
parser.add_argument("message", help="The message to say", nargs="*", default=["Hello, World!"])

args = parser.parse_args()

msg = " ".join(args.message)
animal = args.animal.lower()

if not hasattr(cowsay, animal):
    print(f"Invalid choice: '{args.animal}' (choose from: {', '.join(available_animals)})")
    sys.exit(1)

# Dynamically call the cowsay function for the chosen animal
getattr(cowsay, animal)(msg)
