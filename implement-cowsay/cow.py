import cowsay
import sys
import argparse

listed_animals = cowsay.char_names;

parser = argparse.ArgumentParser(
    prog="cow",
    description="Makes animals say things",
)

parser.add_argument("--animal", default="cow", help="Select an animal to say anything", choices=listed_animals)
parser.add_argument("message", nargs ="+", help="The message that the animal says")

args = parser.parse_args()

message = " ".join(args.message)
animal = args.animal


if animal not in listed_animals:
    print(f"Error: argument --animal: invalid choice: '{animal}'. Choose from: {', '.join(listed_animals)}")
    exit(1)

animal_says = getattr(cowsay, animal)

print(animal_says(message))

