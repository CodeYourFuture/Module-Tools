import cowsay
import argparse

listed_animals = cowsay.char_names

parser = argparse.ArgumentParser(
    prog="cow",
    description="Makes animals say things",
)

parser.add_argument("--animal", default="cow", help="Select an animal to say anything", choices=listed_animals)
parser.add_argument("message", nargs ="+", help="The message that the animal says")

args = parser.parse_args()

message = " ".join(args.message)
animal = args.animal


animal_says = getattr(cowsay, animal)

print(animal_says(message))

