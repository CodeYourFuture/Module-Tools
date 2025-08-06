import argparse
import sys
from cowpy import cow

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="uses the cowsay library to show user-supplied text, as said by a specified animal",
)

parser.add_argument("--animal", help="The animal to be saying things", default="cowacter")
parser.add_argument("message", help="The message to say", nargs="*", default=["Hello, World!"])

args = parser.parse_args()


available_animals = {name.lower(): name for name in cow.Cowacter.cowacters} # List of all characters

msg = " ".join(args.message)
animal = args.animal.lower()

if animal not in available_animals:
    print(f"Invalid choice: '{animal}' (choose from {', '.join(available_animals)})")
    sys.exit(1)

animal_class_name = available_animals[animal]
AnimalClass = getattr(cow, animal_class_name)
print(AnimalClass().milk(msg))